# Introdução a Go - Parte 2

Nesta nota de aula veremos alguns assuntos mais avançados em Go. Novamente, não é objetivo aqui trazer uma abordagem completa da linguagem, com todas as suas nuances e aplicações. Caso tenha interesse em se aprofundar em Go (o que recomendo muito), consulte os materiais complementares na página principal da disciplina.

### Índice

- [Introdução a Go - Parte 2](#introdução-a-go---parte-2)
    - [Índice](#índice)
  - [Input e output de dados](#input-e-output-de-dados)
    - [Lendo dados](#lendo-dados)
    - [Formatando dados de saída](#formatando-dados-de-saída)
  - [Arrays e slices](#arrays-e-slices)
    - [Arrays](#arrays)
      - [Operações com arrays](#operações-com-arrays)
    - [Slices](#slices)
      - [Alocação e capacidade de slices](#alocação-e-capacidade-de-slices)
      - [Comportamento de slices na passagem de parâmetros de funções](#comportamento-de-slices-na-passagem-de-parâmetros-de-funções)
      - [Operações com slices](#operações-com-slices)
  - [Tipos](#tipos)
  - [Ponteiros](#ponteiros)
    - [O que são ponteiros?](#o-que-são-ponteiros)
    - [Aplicação básica](#aplicação-básica)
    - [Erro comum: nil pointer dereference](#erro-comum-nil-pointer-dereference)
    - [Uso em funções](#uso-em-funções)
    - [Uso em métodos](#uso-em-métodos)
  - [Pacotes](#pacotes)
    - [Estrutura de um Pacote](#estrutura-de-um-pacote)
    - [Visibilidade em Pacotes](#visibilidade-em-pacotes)
    - [Uso de Pacotes](#uso-de-pacotes)
    - [Organização de Pacotes](#organização-de-pacotes)

## Input e output de dados

Parte essencial do desenvolvimento de um programa é como vamos receber e retornar os dados. Aqui no curso, boa parte dos dados vão ser processados através de uma interface por linha de comando, ou CLI (_command-line interface_). Neste caso, trabalhamos com o input e output de dados ocorrendo através de um terminal (como o Power Shell).

### Lendo dados

Para trabalharmos com isso, usamos três pacotes, o `fmt`, o `os` e o `bufio`. Para o output de dados, utilizamos normalmente a função `fmt.Println()`, que já estamos usando normalmente. Para ler os dados, podemos usar principalmente a função `fmt.Scanln()`. Essa função lê um conjunto de dados inseridos no terminal, separados por espaço, e atribui para as variáveis indicadas nos parâmetros da função. Veja o exemplo abaixo:

``` go
var x, y, z int

fmt.Println("Informe um valor inteiro e pressione enter:")
fmt.Scanln(&x)

fmt.Println("Informe outros dois valores inteiros e pressione enter:")
fmt.Scanln(&y, &z)

fmt.Println("Os números informados foram:", x, y, z)
```

Veja que, no `fmt.Scanln()` com duas variáveis, separamos cada uma por vírgulas. Além disso, usamos o operador de referência, `&`, para fazer uma referência em memória. Veremos esse operador com mais profundidade logo mais.

Um ponto importante do `fmt.Scanln()` é que, quando chamada, a função lê exatamente o número de dados equivalente ao número de variáveis dentro dos parâmetros, e considera o espaço como um separador de dados. Isso não é um problema quando estamos lidando com valores numéricos (como foi o caso), mas quando precisamos lidar com elementos de texto que possuem espaços, usar essa função limita um pouco a nossa capacidade de ler dados.

Para contornar esse problema, podemos usar a função `bufio.NewReader()`, que vai receber o caminho padrão para entrada de dados, ou `os.Stdin`. Essa função retorna um buffer, em que podemos ficar lendo strings indefinidamente, configurando qual será o separador que interrompe a string que queremos analisar (normalmente uma quebra de linha, ou `\n`). Veja o exemplo abaixo:

``` go
leitor := bufio.NewReader(os.Stdin)
fmt.Println("Informe o seu nome:")
nome, _ := leitor.ReadString('\n')

fmt.Println(nome)
```

A função `bufio.NewReader()` inicia um novo buffer, que pode ser usado quantas vezes for necessário para ler dados do input. Já a função `ReadString()` da variável `leitor` retorna duas informações, o conteúdo de fato (atribuído para a variável `nome`) e um dado do tipo `error`, que aqui não está sendo armazenado em nenhuma variável (daí o uso do `_` na segunda posição). Deve ser incluído o caractere de encerramento da string que está sendo lida. Usualmente trabalhamos com a quebra de linha, mas você pode considerar outros caracteres, como `;`.

### Formatando dados de saída

Podemos melhorar a nossa saída de dados ao formatar algumas informações. Normalmente queremos exibir uma mensagem de texto, seguida por valores que foram processados no código. Neste caso, é interessante usarmos a função `fmt.Printf()`. Essa função possui vários caracteres especiais usados para formatar dados. [Este tutorial](https://yourbasic.org/golang/fmt-printf-reference-cheat-sheet/) possui algumas dicas de como utilizar corretamente. Veja o exemplo abaixo para ter uma ideia de como aplicar:

``` go
var y float64

fmt.Println("Informe um número float:")
fmt.Scanln(&y)

fmt.Printf("O valor inserido foi %.2f\n", y)
```

Veja que usamos o padrão `%.2f` para indicar que a variável `y` precisa ser representada com duas casas decimais. Podemos usar esses "templates" sem necessariamente imprimir na tela as informações, usando a função `fmt.Sprintf()` no lugar do `fmt.Printf`.

## Arrays e slices

### Arrays

Arrays são coleções de elementos do mesmo tipo, com um tamanho fixo definido durante a sua declaração. Os arrays serão a base dos nossos estudos de estruturas de dados ao longo deste curso.

A definição do tamanho do array é realizada em sua declaração, em tempo de compilação. Isso significa que os arrays são sempre de tamanho fixo e não podem ser redimensionados. Portanto, para podermos declarar um array, precisamos necessariamente definir seu tamanho, seja explicitamente (passando um valor numérico), seja através de constantes. Além disso, o array precisa ter o tipo dos seus elementos indicados no momento da declaração. Um array de dados tipo `string`, por exemplo, não pode conter dados numéricos inteiros.

``` go
const TAM_MAX = 5

var filmes [5]string
var numeros [TAM_MAX]int
```

Ao declarar um array, caso ele não seja inicializado, todos os seus elementos são considerados vazios ou nulos, de acordo com o tipo de dado da estrutura. Por exemplo, um array de inteiros é inicializado com todos os elementos tendo um valor igual a zero. Já um array de strings possuem valores iguais a `""`, e um array de structs (que veremos mais adiante) possuem valores inicializados iguais a `nil`.

É possível inicializar um array no momento da sua declaração, utilizando declarações curtas:

``` go
numeros := [4]int{1, 3, 6, 10}
```

O acesso aos elementos do array se dá através do uso de colchetes (`[]`). É necessário indicar o índice do elemento desejado, considerando que o primeiro elemento possui índice `0`.

``` go
fmt.Println(numeros[2])
```

#### Operações com arrays

Para iterarmos sobre arrays, é necessário utilizar a estrutura de repetição `for`. Ela pode ser aplicada de duas formas: a tradicional, com três parâmetros (contador, critério de parada e incremento), sendo que o contador vai indicar o índice do array; ou utilizando a palavra reservada `range`, que vai estabelecer uma variável para o índice e outra para o valor do elemento do array a cada nova iteração.

No exemplo abaixo, ambos os blocos `for` vão escrever na tela os números de 1 a 5:

``` go
numeros := [5]int{1, 2, 3, 4, 5}

for i := 0; i < len(numeros); i++ {
  fmt.Printf("Índice %d - valor %d\n", i, numeros[i])
}

for indice, valor := range numeros {
  fmt.Printf("Índice %d - valor %d\n", indice, valor)
}
```

Veja que, no exemplo acima, foi utilizada a função `len()`

### Slices

Já slices são segmentos de arrays, que podem ou não ter sido definidos previamente. Eles possuem dimensão dinâmica.

``` go
var outrosNumeros []int // criando um slice vazio

outrosNumeros = numeros[1:]  // selecionando um slice a partir do elemento 1 (inclusive) até o final
outrosNumeros = numeros[1:3] // selecionando um slice a partir do elemento 1 (inclusive) até 3 (exclusive)
```

Também é possível inicializar um slice utilizando a função `make()` ou utilizando declarações curtas:

``` go
numeros := make([]int, 5) // aloca memória para 5 inteiros
maisNumeros := []int{1, 2, 3, 4, 5}
```

#### Alocação e capacidade de slices

Todo slice possui três componentes:

* Ponteiro: veremos esse assunto mais à frente, e aponta para o início do segmento do array ao qual o slice se refere;
* Tamanho (length, função `len()`): representa o número de elementos que ele contém no momento;
* Capacidade (capacity, função `cap()`): representa o número máximo de elementos que o slice pode conter antes de uma nova alocação de memória ser necessária.

Quando você adiciona elementos a um slice e excede sua capacidade, o Go automaticamente aloca um novo array com uma capacidade maior e copia os elementos do array antigo para o novo. Este processo é conhecido como "realocação" e aumenta a capacidade do slice.

A nova capacidade de um slice realocado não segue uma regra estritamente definida, mas geralmente, o Go tenta dobrar a capacidade do slice para o próximo tamanho adequado para evitar realocações frequentes. Isso é feito para equilibrar o uso de memória e desempenho. No entanto, o algoritmo exato de crescimento pode variar dependendo do tamanho atual do slice e das especificidades da implementação do runtime do Go.

#### Comportamento de slices na passagem de parâmetros de funções

No caso de tipos de dados como slices e outros que não veremos aqui, o que é passado por valor na associação entre funções é o ponteiro para o dado real. Isso pode dar a impressão de que os dados estão sendo passados por referência, pois modificações nesses dados dentro da função podem afetar os dados originais. Mas tecnicamente, ainda é uma passagem por valor, só que o valor é um ponteiro para o dado. Vamos ver mais sobre ponteiros logo abaixo.

#### Operações com slices

O processo de iteração sobre slices é idêntico ao de arrays. Outras operações possíveis com slices são:

* Incluir novos elementos: utiliza-se a função `append()` para criar um novo slice, combinando o slice anterior com um novo elemento;
* Segmentação de slices: é possível atribuir a slices segmentos de um outro slice, utilizando dois pontos (`:`) dentro dos colchetes, de forma bem similar ao que se tem em Python (p.ex., `x := y[:3]` para atribuir a `x` os elementos de índices 0, 1 e 2 de `y`);
* Copiar slices: a função `copy()` serve para fazer uma cópia "rasa", ou seja, apenas os valores são copiados para uma nova referência.

Muitas outras operações são possíveis. Slices são um dos tipos mais dinâmicos e customizáveis em Go, e vale a pena explorá-lo mais.

## Tipos

**Tipos** são elementos em Go utilizados para agrupar informações dentro de uma mesma abstração. Criamos tipos quando temos diversos dados que dizem respeito a um mesmo objeto. Por exemplo, se formos criar em um projeto de gestão acadêmica, faz sentido que tenhamos que criar dados referentes às disciplinas de um curso, como o seu código, o professor que leciona a disciplina, o horário e o período que essa disciplina se encontra no curso.

Sem o uso de tipos, precisaríamos de algo do tipo:

``` go
disciplinaNome := "Cálculo I"
disciplinaCodigo := 1234
disciplinaProfessor := "Victor"
disciplinaHorario := "7h30"
disciplinaPeriodo := 1
```

Todas essas variáveis poderiam ser armazenadas em uma lista (talvez num mapa, que não vimos aqui no curso), mas ainda assim o acesso aos dados seria complicado.

Portanto, Go se inspirou em linguagens como C e criou os **tipos**. Com um tipo, podemos juntar todas essas informações em uma única variável. Além disso, o tipo é replicável, simplificando assim o processo de criação de múltiplas variáveis com as mesmas informações:

``` go
// Os dados dentro de um tipo são chamados de campos
type Disciplina struct {
  Nome      string
  Codigo    int
  Professor string
  Horario   string
  Periodo   int8
}

disc1 := Disciplina{
  Nome:      "Cálculo",
  Codigo:    1234,
  Professor: "Victor",
  Horario:   "7h30",
  Periodo:   1,
}

fmt.Println(disc1.Codigo) // Exibe o código da disciplina na tela
```

Os tipos são uma forma bem rudimentar do que temos na Orientação a Objetos. Apesar de não termos vários elementos deste paradigma, como herança e polimorfismo, podemos pensar em tipos como uma versão simplificada de uma classe.

Go ainda suporta a criação de **métodos** para tipos, que são funções criadas para serem usadas especificamente por dados daquele tipo. Veja o caso abaixo, onde criamos um método para o cálculo da área de um círculo:

``` go
// Primeiro precisamos criar um tipo
type Circulo struct {
  Raio  float64
}

// Para o método, inserimos a indicação do tipo antes do nome da função, entre parênteses
func (c Circulo) Area() float64 {
  return math.Pi * c.Raio * c.Raio
}

circ := Circulo{Raio: 4.5}
fmt.Println(circ.Area()) // Usamos um método da mesma forma que usamos um campo do tipo
```

Caso você queira alterar as propriedades do tipo que está sendo usado no método, é necessário utilizar ponteiros, que veremos logo abaixo.

Veja que utilizamos letras maiúsculas tanto para os campos quanto para o método. Essa convenção é a mesma das variáveis e funções: letras maiúsculas indicam que os elementos são públicos e compartilhados por outros pacotes, letras minúsculas são específicas do pacote em que foram declaradas.

Tipos são muito utilizados em Go. Basicamente qualquer estrutura complexa precisa ser configurada em um tipo, de forma a simplificar a interação com os dados durante a execução do código.

## Ponteiros

### O que são ponteiros?

Como falamos durante a [seção de funções](002-intro_go_1.md#funções), em Go todos os dados são transmitidos entre funções utilizando passagem por valor. Isso significa que, no momento em que uma função é executada, o programa faz uma cópia de todos os dados dos parâmetros, que são utilizados na execução do programa.

Portanto, até o momento não conseguimos alterar os dados de estruturas passadas como parâmetros. Isso gera alguns complicadores, como a cópia excessiva de dados (que pode penalizar muito a eficiência do programa) e a dificuldade em retornar muitas informações em uma mesma função.

Como uma forma de dar mais controle para o desenvolvedor com relação ao que é realmente passado entre funções, em Go temos o conceito de **ponteiros**, representados pelo asterisco (`*`). Ponteiros são variáveis que indicam endereços na memória, fazendo referências a outros dados. Eles podem ocupar 32 ou 64bits, dependendo da arquitetura do sistema. Um ponteiro é um tipo de dado em Go, e seu dado não inicializado é `nil`. Vamos usar ponteiros em dois principais cenários:

* Quando queremos alterar o valor de um determinado dado em uma função ou método;
* Quando queremos ganhar desempenho, evitando a cópia de dados muito grandes.

Existem outras aplicações de ponteiros, mas não veremos neste curso introdutório.

### Aplicação básica

Considere, por exemplo, esse cenário:

``` go
x := 5
y := x
fmt.Println(x, y) // 5, 5

x = 6
fmt.Println(x, y)
```

Nesse bloco de código, a variável `y` recebeu o valor de `x`, ou seja, o valor 5. Quando `x` é alterado para 6, a variável `y` mantém seu valor original, já que a atribuição foi feita para o valor de `x` naquele momento. Portanto, a última linha vai imprimir `6, 5` na tela.

Agora, considere esse caso:

``` go
x := 5
z := &x
fmt.Println(x, *z) // 5, 5

x = 6
fmt.Println(x, *z)
```

Neste caso, a variável `z` **faz uma referência** a x, ou seja, a variável `z` está recebendo o endereço de memória de `x`. Quando utilizamos o operador `&`, dizemos que **`z` faz referência a `x`**. Já nas linhas de impressão, utilizamos o operador `*`. Neste momento, estamos dizendo ao Go para consultar o endereço de memória disponível na variável `z` e trazer o valor que está armazenado ali. Neste momento, estamos **dereferenciando `z`**.

Portanto, na primeira linha de impressão, o programa vai consultar o endereço de memória armazenado na variável `z` e vai identificar que ele está apontando para a variável `x`, então vai imprimir o valor `5` na tela (resultando `5, 5`). Na segunda impressão o programa faz exatamente a mesma coisa: consulta o endereço de memória armazenado na variável `z`, e identifica que este endereço aponta para a variável `x`, que está valendo `6` no momento. Logo, a função `fmt.Println()` vai exibir na tela o valor `6, 6`.

Veja que no exemplo acima o ponteiro `z` não tem o mesmo valor de `x`, ele apenas **aponta** para `x`. Se chamarmos a função `fmt.Println(z)` vamos ver que será exibido na tela algo como `0xc0000b6058`. Esse valor nada mais é que o endereço da memória que está sendo indicado pela variável `z`. Se quisermos ver o valor que está armazenado neste endereço, precisamos usar o operador asterisco, ou `*z`.

### Erro comum: nil pointer dereference

Um erro muito comum em linguagens que utilizam ponteiros, como Go e C, é a dereferência de um ponteiro nulo. Considere o seguinte caso:

``` go
var w *int

fmt.Println(w)
fmt.Println(*w)
```

Na primeira linha, estamos criando uma variável `w`, que é um ponteiro para um inteiro (lembre-se que ponteiros são um tipo específico de dado!). Na linha seguinte, exibimos na tela o valor de `w`. No entanto, como ainda não inicializamos a variável, essa linha vai exibir o valor nulo, ou `nil` em Go.

Na linha seguinte, o programa vai tentar dereferenciar `w`, que vale `nil`. No entanto, como `w` ainda não aponta para nada, isso faz com que o programa entre em um estado que chamamos em Go de **panic**. O programa não sabe como proceder, então ele aborta a operação e é encerrado. Esse é um erro muito comum, principalmente quando ainda não estamos familiarizados com o uso de ponteiros.

### Uso em funções

Podemos utilizar ponteiros em funções quando queremos fazer uma passagem por referência dos parâmetros. Isso é muito útil principalmente quando queremos passar dados muito extensos. Pense num cenário extremo: você está processando um array de 1000 elementos, em que cada elemento é um tipo que ocupa cerca de 100kB de memória. Isso dá quase 100MB de espaço em memória. Se você fizer uma passagem por valor (que é o padrão nas funções), o programa vai ter que copiar esses 100MB de dados novamente, dobrando o espaço em memória ocupado pelo programa no computador, e gerando uma ineficiência enorme!

Para evitar esse custo no programa, podemos usar ponteiros como parâmetros de funções, ao invés dos valores usuais. Veja o caso abaixo:

``` go
func alteraMensagem(msg *string) {
  novaMensagem := *msg
  novaMensagem = strings.ReplaceAll(novaMensagem, "mundo", "turma")
  *msg = novaMensagem
}

func main() {
  mensagem := "Olá, mundo"
  alteraMensagem(&mensagem)
  fmt.Println(mensagem)
}
```

Na função `main()`, quando chamamos a função `alteraMensagem()`, estamos passando a referência da variável `mensagem`, ou seja, o seu endereço de memória. Por sua vez, dentro da função `alteraMensagem()` o programa referencia o ponteiro `msg` e passa o resultado para `novaMensagem`. Esta variável é, portanto, do tipo `string` e vale `"Olá, mundo"`.

Na linha seguinte, há uma substituição da variável `novaMensagem`, para `"Olá, turma"`. Veja que, como esta variável é uma string, o valor de `*msg` permanece como `"Olá, mundo"`. `*msg` só muda de valor na última linha da função, em que fazemos uma atribuição de valor.

### Uso em métodos

O uso em métodos é bem similar ao de funções. Utilizamos o ponteiro quando queremos alterar o valor original do dado, através de uma passagem da referência ao invés do valor:

``` go
type Numero struct {
  Valor int
}

func (n *Numero) Adiciona1(x int) {
  n.Valor += x
}

func (n Numero) Adiciona2 (x int) {
  n.Valor += x
}

func main() {
  n1 := Numero{Valor: 5}

  n1.Adiciona2(5)
  fmt.Println(n1)
  n1.Adiciona1(5)
  fmt.Println(n1)
}
```

Rode este bloco e veja o seu comportamento nos dois métodos. O que mudou?

## Pacotes

Em Go, a organização de código é feita através de pacotes. Um pacote é um conjunto de arquivos Go no mesmo diretório que compartilham o mesmo package name no cabeçalho do arquivo. O package name determina a identidade do pacote e como ele será referenciado por outros pacotes.

Os pacotes são a unidade básica de encapsulamento em Go, fornecendo um mecanismo para agrupar código relacionado e controlar sua visibilidade. Isso promove a reutilização de código e torna mais fácil a manutenção e o desenvolvimento de programas em larga escala.

### Estrutura de um Pacote

Um pacote em Go consiste em um ou mais arquivos Go que contêm declarações de código, como variáveis, funções, tipos e constantes. A estrutura básica de um pacote é a seguinte:

```go
package nome_do_pacote

import (
    "pacote1"
    "pacote2"
)

// declarações de código
```

* `package nome_do_pacote`: Esta declaração define o package name do pacote. O nome do pacote é exclusivo dentro do escopo do projeto e determina como o pacote será referenciado em outros arquivos Go e pacotes.
* `import ("pacote1" "pacote2")`: A declaração `import` é usada para importar outros pacotes que o pacote atual depende. Isso permite que o pacote atual use as funcionalidades fornecidas por esses pacotes importados.

### Visibilidade em Pacotes

Em Go, a visibilidade de identificadores (variáveis, funções, tipos, etc.) é controlada pelo uso de letras maiúsculas ou minúsculas no início do nome. A regra é simples:

* Identificadores que começam com letra maiúscula são visíveis fora do pacote, ou seja, são exportados. Por exemplo, `Nome` é exportado e pode ser acessado de outros pacotes.
* Identificadores que começam com letra minúscula são visíveis apenas dentro do pacote em que são declarados e não são exportados. Por exemplo, `idade` não é exportado e só pode ser acessado dentro do mesmo pacote.

### Uso de Pacotes

Para usar um pacote em um arquivo Go, basta importá-lo usando a declaração import. Por exemplo:

``` go
package main

import (
    "fmt"
    "math/rand"
)

func main() {
    fmt.Println("Número Aleatório:", rand.Intn(100))
}
```

Neste exemplo, estamos importando os pacotes `fmt` e `math/rand`. O pacote `fmt` é usado para formatação de saída, enquanto o pacote `math/rand` é usado para geração de números aleatórios.

### Organização de Pacotes

A organização de pacotes em um projeto Go geralmente segue uma estrutura hierárquica de diretórios. Por exemplo:

```
meu_projeto/
├── pacote1/
│   ├── arquivo1.go
│   └── arquivo2.go
├── pacote2/
│   ├── arquivo1.go
│   └── arquivo2.go
└── main.go
```

Neste exemplo, temos um projeto com dois pacotes (`pacote1` e `pacote2`) e um arquivo principal (`main.go`). Cada pacote tem seu próprio diretório e contém um ou mais arquivos Go relacionados.
