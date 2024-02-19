# Introdução a Go - Parte 1

Tendo conseguido instalar, configurar, compilar e executar o primeiro programa em Go na última aula, vamos agora começar a entender os conceitos iniciais da linguagem.

O objetivo deste curso não é realizar uma formação completa em Go. Não falaremos de tópicos importantes para a linguagem, como goroutines ou interfaces. Na [página principal da disciplina](/ed/ed.md) você verá uma lista de conteúdos complementares que te ajudarão nisso.

Para este curso, focaremos nos conceitos básicos necessários para conseguirmos trabalhar, de forma eficiente, o aprendizado das estruturas de dados que veremos. Portanto, recomendo muito que você dê continuidade aos estudos da linguagem, utilizando os conteúdos complementares sugeridos e outros disponíveis online.

Esta nota de aula não apresenta exercícios. Como prática, sugiro que refaça exercícios de disciplinas passadas (como Programação Estruturada e Programação Orientada a Objetos).

### Importante: Formatando o código

Antes de começarmos a falar de código, vamos comentar um pouco sobre como escrever programas em Go. A linguagem possui um guia de estilo oficial, desenvolvido e mantido pela equipe do Go dentro do Google. Este guia de estilo está disponível no link https://google.github.io/styleguide/go/. Neste curso, não analisaremos tão a fundo o guia de estilo, mas adotaremos boas práticas que já vêm sido discutidas nos semestres passados em outras disciplinas.

Existe um comando que simplifica o processo de formatação de arquivos em Go. Na linha de comando, envie a instrução `go fmt <nomeDoArquivo>.go para formatar automaticamente o arquivo.

Um ponto importante do guia de estilo em Go é que, ao contrário de outras linguagens já vistas durante a graduação, como Python e Java, aqui utilizamos tabs para indentação. Tendo a extensão do Go instalada no VSCode, isso não deve ser um problema.

### Índice

- [Introdução a Go - Parte 1](#introdução-a-go---parte-1)
    - [Importante: Formatando o código](#importante-formatando-o-código)
    - [Índice](#índice)
  - [Entendendo o primeiro programa](#entendendo-o-primeiro-programa)
  - [Comentários](#comentários)
  - [Tipos de dados](#tipos-de-dados)
    - [Dados numéricos inteiros](#dados-numéricos-inteiros)
    - [Dados numéricos decimais](#dados-numéricos-decimais)
    - [Dados booleanos](#dados-booleanos)
    - [Texto](#texto)
    - [Dados "nulos"](#dados-nulos)
  - [Variáveis e constantes](#variáveis-e-constantes)
  - [Operadores](#operadores)
  - [Funções](#funções)
    - [Passagem por valor vs por referência](#passagem-por-valor-vs-por-referência)
  - [Estruturas de decisão](#estruturas-de-decisão)
    - [`if/else`](#ifelse)
    - [`switch/case`](#switchcase)
  - [Estruturas de repetição](#estruturas-de-repetição)

## Entendendo o primeiro programa

Vamos retomar o código que implementamos no primeiro programa, dentro do arquivo `olaMundo.go`:

``` go
package main

import "fmt"

func main() {
	fmt.Println("Olá, mundo!")
}
```

O primeiro ponto a se observar é o formato do nome do arquivo. Em Go trabalhamos com o padrão _snakeCase_. Ou seja, todas as palavras são escritas sem separação, e a primeira letra de cada palavra é maiúscula. No caso de arquivos, a primeira letra do nome do arquivo é minúscula.

Todo programa em Go é organizado em pacotes. Mesmo que só exista um arquivo no programa, o pacote precisa ser necessariamente declarado, usando a instrução `package`.

Por padrão, após a compilação o programa sempre começará sua execução pela função `main()` contida no pacote `main`. Portanto, o nosso código rodou pois existe uma função `main` (que é declarada usando a instrução `func`), que possui um bloco de código, separado por chaves (`{}`).

No arquivo, as dependências (uso de outros pacotes) são administradas na segunda linha de código, utilizando a instrução `import`, seguida pelo conjunto de pacotes que se deseja utilizar no pacote em questão, sempre entre aspas. Utilize parênteses (`()`) para incluir mais de um pacote, como no exemplo abaixo:

``` go
import (
    "fmt"
    "math/rand"
)
```

Neste exemplo, estamos utilizando o pacote `fmt` e o subpacote `rand`, que faz parte do pacote `math`. Ao utilizar um pacote ou subpacote, sempre utilize apenas o nível mais baixo de pacotes. Por exemplo, caso eu deseje utilizar a função `Intn()` do subpacote `math/rand`, o código seria escrito dessa forma:

``` go
rand.Intn(10)
```

Em Go, não é possível importar pacotes que não são utilizados no código. Caso isso seja feito, o código não vai compilar e um erro será apresentado.

``` go
package main

import (
    "fmt"
    "math/rand"
)

func main() {
	fmt.Println("Olá, mundo!")
}
```

``` cmd
# command-line-arguments
olaMundo.go:5:5: "math/rand" imported and not used
```

Você verá que isso acontece não só na hora de importar pacotes, mas também em variáveis, contantes e outros elementos da linguagem.

Entendendo o que foi apresentado acima, o último elemento que precisa ser compreendido é a função `fmt.Println()`. Essa função imprime uma nova linha no console, encerrando a linha com uma quebra de linha. É possível incluir diversos parâmetros na função, como no exemplo abaixo:

``` go
package main

import "fmt"

func main() {
    fmt.Println("Aline é", "veterinária e possui", 25, "anos.")
}
```

``` cmd
Aline é veterinária e possui 25 anos.
```

Veja que a função inclui espaços em branco entre cada parâmetro passado. Observe que a função `fmt.Println()`, bem como a função `rand.Intn()`, começam com letra maiúscula. A convenção de iniciar funções (e variáveis, constantes, etc.) com letra maiúscula tem o propósito de indicar que aquele elemento é público e pode ser acessado por outros pacotes. Caso deseje que um elemento de código seja privado (i.e., restrito apenas ao pacote em que está inserido), inicie com letra minúscula.

## Comentários

Podemos inserir comentários em Go de duas formas:

* Comentários em linha: utilizamos duas barras (`//`);
* Comentários em bloco: inserimos os caracteres `/*` ao início do bloco, e `*/` ao final do bloco de comentário.

``` go
// Comentário de linha, usado para complementar alguma informação de código

/*
Comentário de bloco, usado para descrever comportamento de funções, documentar pacotes,
entre outras informações relevantes que vão ocupar mais de uma linha.
*/
```

## Tipos de dados

Go possui uma enorme variedade de tipos de dados. Aqui não trabalharemos com todos, mas sim traremos alguns exemplos e os tipos mais comuns para iniciarmos a programar na linguagem.

### Dados numéricos inteiros

Os dados numéricos inteiros principais são oito, listados na tabela abaixo:

| **Tipo** | **Tamanho** |                  **Faixa de valores**                  |
|:--------:|:-----------:|:------------------------------------------------------:|
|   int8   |      8b     | -128 a 127                                             |
|   uint8  |      8b     | 0 a 255                                                |
|   int16  |     16b     | -32.768 a 32.767                                       |
|  uint16  |     16b     | 0 a 65.535                                             |
|   int32  |     32b     | -2.147.483.648 a 2.147.483.647                         |
|  uint32  |     32b     | 0 a 4.294.967.295                                      |
|   int64  |     64b     | -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807 |
|  uint64  |     64b     | 0 a 18.446.744.073.709.551.615                         |

Go possui um tipo inteiro genérico, chamado `int`, que normalmente é mais usado que os 8 apresentado acima, principalmente quando não sabemos o tamanho do dado que será armazenado no momento. O tipo `int` ocupa 32 ou 64 bits de memória, a depender da arquiteutra da máquina em que o código está sendo executado. O tipo `uint` possui comportamento similar, porém não aceitando números negativos.

Para declarações implícitas de números inteiros, sempre é considerado o tipo `int`.

Além disso, a linguagem também possui o tipo `byte`, que é um atalho para o tipo `uint8`; e o tipo `rune`, que é um atalho para o tipo `int32` e é usado principalmente para armazenar valores numéricos que representam caracteres [Unicode](https://home.unicode.org/).

### Dados numéricos decimais

Go possui dois tipos principais para números decimais, ou de ponto flutuante. Utilizamos `float32` ou `float64` para números com 32 ou 64 bits de armazenamento em memória. A diferença entre eles é o número de dígitos na precisão, sendo o `float64` mais preciso que o `float32`. É sempre necessário especificar a alocação de um número decimal. Para declarações implícitas (ver adiante), é considerado sempre `float64`.

Como nas demais linguagens de programação, utiliza-se o ponto (`.`) como separador decimal, ao invés da vírgula tradicional no português.

A linguagem ainda possui dois tipos de números complexos, `complex64` e `complex128`, ocupando 64 e 128 bits na memória, respectivamente. A representação de números complexos é sempre incluindo uma parte real e uma imaginária, seguindo pelo símbolo `i`, como no exemplo abaixo:

``` go
fmt.Println(12.3 + 45.12i)
```

### Dados booleanos

Os dados booleanos de verdadeiro e falso são representados pelas palavras reservadas `true` e `false`, com letras minúsculas. Elas ocupam apenas 1 bit. Utiliza-se o tipo `bool` para representar dados booleanos.

É importante reforçar que Go é uma linguagem de tipagem forte e estática. Isso significa que não é possível fazer comparações de valores inteiros e booleanos como normalmente fazemos em Python. Isso se aplica a qualquer comparação entre tipos diferentes.

``` go
package main

import "fmt"

func main() {
    fmt.Println(1 == true) // vai gerar um erro de compilação
}
```

### Texto

Em Go utilizamos o tipo `string` para representar dados de texto. Cada caractere do tipo `string` ocupa 8 bits. Não existe o tipo `char` na linguagem, mas podemos usar o tipo `rune` para representar caracteres unicode normalmente.

### Dados "nulos"

Go não possui um dado que represente um nulo de fato, como `None` em Python. Em vez disso, a linguagem possui um valor `nil`, que representa valores de referência que não possuem um valor válido ou ainda não foram inicializados. Isso é muito comum em retornos de função ou uso de tipos (structs), que veremos mais adiante.

## Variáveis e constantes

As variáveis e as constantes podem ser declaradas dentro ou fora de funções. Utiliza-se a instrução `var` para variáveis e `const` para constantes.

Variáveis e constantes que funcionem apenas no escopo do pacote, sejam elas locais ou globais, são inicializadas com letra minúscula. Caso possuam escopo além do pacote, configurando como um dado público, devem iniciar com letra maiúscula. Isso não é uma convenção, é uma condição que o compilador leva em consideração para considerar o elemento como público ou privado.

Variáveis podem ser declaradas em Go de três formas:

* Declaração completa: utiliza-se a instrução `var`, seguida pelo nome da variável e do tipo do dado. O dado deve ser inicializado em uma linha posterior;
* Declaração implícita: utiliza-se a instrução `var`, seguida pelo nome da variável e de uma operação de atribuição. O compilador infere qual será o tipo do dado, e considera os tipos `bool`, `int`, `float64` e `string` respectivamente para dados booleanos, numéricos inteiros, numéricos decimais e de texto;
* Declaração curta: utiliza-se o operador `:=` para realizar declarações curtas. Nesse caso, não é necessário usar a instrução `var`. O compilador já infere o tipo do dado, da mesma forma que a declaração implícita.

Para constantes, é recomendado usar a declaração implícita, usando a instrução `const` ao invés de `var`. Não é possível realizar declarações curtas para constantes.

É possível declarar mais de uma variável ao mesmo tempo. Caso a declaração seja completa, todas as variáveis precisam ser do mesmo tipo, e este é colocado ao final da linha. Caso a declaração seja implícita ou curta, é necessário que todas as variáveis sejam inicializadas.

Variáveis e constantes, quando de escopo local (i.e., inicializadas com letra minúscula e dentro de funções), precisam necessariamente ser utilizadas dentro do pacote, caso contrário o compilador subirá um erro no momento da compilação.

``` go
package main

import "fmt"

// variáveis de escopo do pacote
var linguagem string // declaração completa
var soma, subt float64 // declaração completa, múltiplas variáveis
var x, y = 4, 10 // declaração implícita, múltiplas variáveis

// constante pública, declarada implicitamente
const Pi = 3.14

func main() {
    // as declarações implícita e curta possibilitam inicializar variáveis com mais de um tipo
    var msg1, num = "Olá, mundo", 4.5
    msg2, ePositivo := "Bom dia!", false

    // precisamos usar variáveis locais declaradas!
    fmt.Println(msg1, num)
    fmt.Println(msg2, ePositivo)
}
```

## Operadores

Até o momento já vimos o operador básico de atribuição (`=`) e o de declaração (`:=`). Além destes, durante o curso vamos trabalhar principalmente com os seguintes operadores:

* Aritméticos: soma, subtração, multiplicação, divisão e resto da divisão (`+`, `-`, `*`, `/`, `%`);
* Atribuição: análogos aos aritméticos (`+=`, `-=`, `*=`, `/=`, `%=`);
* Comparação: igualdade, desigualdade, menor que, maior que, menor ou igual a, maior ou igual a (`==`, `!=`, `<`, `>`, `<=`, `>=`);
* Lógicos: E, OU, NÃO (`&&`, `||`, `!`)

Go ainda possui suporte aos operadores unários `++` e `--`, sempre em pós-incremento. Ou seja, o operador deve vir após a definição da variável a ser incrementada ou decrementada.

``` go
var x = 5

x++ // x passa a valer 6
x-- // x volta a valer 5
```

A linguagem ainda possui outros operadores que não serão discutidos aqui, como operadores Bitwise ou de memória e canal. Dois outros operadores, ponteiro e referência (`*` e `&`) serão discutidos posteriormente.

## Funções

As funções em Go possuem a mesma aplicação que em outras linguagens estruturadas, a de organizar e componentizar o código em blocos autocontidos e de responsabilidade limitada, facilitando manutenção, evolução e escalabilidade dos projetos de software. A sintaxe básica é apresentada a seguir:

``` cmd
func nomeFuncao([param1 tipo1, param2 tipo2]) [(tipoRetorno1, tipoRetorno2)] {
    // código da função
    return [dados] // [dados] são do mesmo tipo especificados na assinatura da função
}
```

Não é necessário inserir parâmetros nas funções. Da mesma forma, não é necessário que a função retorne alguma coisa. Se a função não possui nenhum dado de retorno, o uso do `return` é completamente opcional. Caso a função apresente mais de um retorno, os tipos de retorno precisam estar entre parênteses.

Os parâmetros de entrada podem ser agrupados pelo tipo. Nesse caso, o tipo só precisa ser inserido uma vez, ao final dos parâmetros daquele tipo. Por fim, a nomenclatura das funções segue a mesma regra de variáveis: iniciar com letra minúscula para funções de escopo restrito ao pacote, e com letra maiúscula para funções públicas.

Veja abaixo alguns exemplos de funções:

``` go
// função pública
func OlaMundo() {
    fmt.Println("Olá, mundo!")
}

func soma(a int, b int) int {
    return a + b
}

func mensagem(msg1, msg2 string) {
    fmt.Println(msg1, msg2)
}

func trocaValores(a, b int, msg string) (int, int) {
    fmt.Println(msg)
    return b, a
}
```

Em projetos de maior escala, é recomendado documentar a função adequadamente, usando comentários de bloco.

``` go
/*
Soma dois valores inteiros.

Parâmetros:
* a, b: valores inteiros a serem somados.

Retorno:
* int: soma dos valores a e b.
*/
func soma(a, b int) int {
    return a + b
}
```

Go ainda possui o conceito de funções anônimas, parecidas com o `lambda` em Python. Aqui, elas são chamadas de `closures` e podem ser usadas como valores e passadas como argumentos para outras funções.

``` go
func anonima() {
	dobra := func(x int) int {
		return x * 2
	}

	resultado := dobra(5)
	fmt.Println(resultado)

	// Função anônima como argumento para outra função
	calcular := func(f func(int) int, x int) int {
		return f(x)
	}

	resultado = calcular(dobra, 3)
	fmt.Println(resultado)
}
```

### Passagem por valor vs por referência

Em Go, a forma como os parâmetros são passados para as funções é realmente importante para entender como trabalhar com funções e dados dentro do seu código. Nesta linguagem, os parâmetros são sempre passados por valor. Isso significa que, quando você passa uma variável para uma função, o que é passado é uma cópia do valor dessa variável. Portanto, se a função modificar o valor do parâmetro, essa modificação não afetará a variável original fora da função.

## Estruturas de decisão

Em Go, temos duas estruturas de decisão possíveis: `if/else` e `switch/case`.

### `if/else`

A estrutura é bem similar às outras linguagens. A diferença principal é que usualmente não precisamos incluir parênteses para limitar os testes lógicos nas condições de cada bloco. O uso do parênteses só é necessário quando precisamos comparar dados mais complexos, como tipos. Como em outras linguagens, o uso de `else if` e `else` é totalmente opcional.

``` go
package main

import "fmt"

func main() {
    var x = 10

    if x > 18 {
        fmt.Println("Você é maior de idade.")
    } else if x < 0 {
        fmt.Println("Valor inválido.")
    } else {
        fmt.Println("Você é menor de idade")
    }
}
```

### `switch/case`

Nesta estrutura, utiliza-se a instrução `case` para indicar cada um dos possíveis valores da variável usada na decisão. É possível incluir mais de um valor para cada `case`. Utiliza-se a instrução `default` (opcional) para incluir uma operação para o caso da variável de comparação não ser igual a nenhum dos casos apresentados.

``` go
package main

import "fmt"

func main() {
	var dia = "segunda"

	switch dia {
	case "segunda", "terça", "quarta", "quinta", "sexta":
		fmt.Println("Dia útil.")
	case "sábado", "domingo":
		fmt.Println("Final de semana.")
	default:
		fmt.Println("Dia inválido.")
	}
}
```

É possível usar a estrutura `switch` com operadores de comparação, como no exemplo abaixo:

``` go
package main

import (
	"fmt"
)

func main() {
	var numero int
	fmt.Println("Digite um número:")
	fmt.Scanln(&numero)

	switch {
	case numero > 0:
		fmt.Println("positivo")
	case numero < 0:
		fmt.Println("negativo")
	default:
		fmt.Println("zero")
	}
}
```

## Estruturas de repetição

Em Go, a única estrutura de repetição que temos é o `for`. Ela possui três possíveis formas de aplicação, sendo que uma delas só veremos na seção sobre [arrays](#arrays).

O primeiro caso é bem similar ao uso do `for` dentro de linguagens como C ou Java. Neste caso, temos três componentes na declaração da estrutura:

* Inicialização da variável de contagem;
* Condição de parada da estrutura de repetição;
* Incremento da variável de contagem após cada iteração.

Veja no exemplo abaixo:

``` go
package main

import "fmt"

func main() {
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }
}
```

Essa operação imprimirá na tela os números de 0 a 4, um em cada linha. Veja que, para a inicialização da variável de contagem, usamos a declaração curta pois a variável `i` ainda não havia sido declarada. É possível utilizar uma variável já declarada anteriormente, e dentro do `for` apenas realizar a atribuição para o valor inicial. No entanto, isso não é tão comum.

É importante ressaltar que, caso seja usada uma declaração curta na inicialização da variável de contagem, esta variável possui um escopo limitado ao `for`. Quando a estrutura de repetição se encerrar, a variável também é desalocada da memória do computador.

Já o segundo caso de uso do `for` que veremos no momento é quando se deseja obter um comportamento similar ao `while` disponível em outras linguagens. Inclui-se uma condição de análise que é validada ao início de cada iteração. Enquanto esta condição for verdadeira, uma nova iteração é executada. A estrutura de repetição para quando a condição passa a ser falsa. O exemplo abaixo exibe todos os números inteiros de 5 a 1:

``` go
package main

import "fmt"

func main() {
    var x = 5
    for x > 0 {
        fmt.Println(x)
        x--
    }
}
```
