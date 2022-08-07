# Introdução a Java

Nesta nota de aula vamos compilar os primeiros programas com Java. Vamos também trazer os conceitos básicos da linguagem, como as sintaxes para exibição de informações, tipos de dados, declaração de variáveis, estruturas de seleção e estruturas de repetição.

### Índice

1. [Compilando o primeiro programa](#compilando-o-primeiro-programa)
2. [Variáveis e tipos de dados](#variáveis-e-tipos-de-dados)
3. [Operadores](#operadores)
4. [Estruturas de decisão](#estruturas-de-decisão)
5. [Estruturas de repetição](#estruturas-de-repetição)

## Compilando o primeiro programa

Vamos para o nosso primeiro código! O programa que imprime uma linha simples. Para mostrar uma linha, podemos fazer:

``` java
System.out.println("Minha primeira aplicação Java!");
```

Mas esse código não será aceito pelo compilador java. O Java é uma linguagem bastante burocrática, e precisa de mais do que isso para iniciar uma execução. Veremos os detalhes e os porquês durante os próximos capítulos. O mínimo que precisaríamos escrever é algo como:

``` java
class MeuPrograma {
    public static void main(String[] args) {
        System.out.println("Minha primeira aplicação Java!");
    }
}
```

Após digitar o código acima, grave-o como MeuPrograma.java em algum diretório. Para compilar, você deve pedir para que o compilador de Java da Oracle, chamado _javac_, gere o bytecode correspondente ao seu código Java.

Depois de compilar, o bytecode foi gerado. Quando o sistema operacional listar os arquivos contidos no diretório atual, você poderá ver que um arquivo .class foi gerado, com o mesmo nome da sua classe Java.

### O que pode dar errado?

Muitos erros podem ocorrer no momento que você rodar seu primeiro código. Vamos ver alguns deles:

* É comum o esquecimento do `;` ao final de cada linha, principalmente entre programadores iniciantes e/ou que trabalhem com linguagens que não adotem esse caractere;
* Java é uma linguagem _case sensitive_, ou seja, reconhece a diferença entre caracteres maiúsculos e minúsculos. Portanto, `class` é diferente de `Class`;
* Da mesma forma, declaração de classes e variáveis devem seguir o mesmo `case` usado na declaração;
* Por convenção, utiliza-se o estilo _camelCase_ para a nomeação de classes, métodos e variáveis em Java. Para a declaração de classes, sempre comece com uma letra maiúscula. Para métodos e variáveis, sempre comece com uma letra minúscula;
* O nome do arquivo `.java` deve sempre refletir o nome da classe presente dentro do arquivo.

### Comentando código

É possível inserir linhas ou blocos de comentário no código, utilizando as expressões `//` ou `/**/`, respectivamente:

``` java
// esta é uma linha de comentário.

/*
este é um bloco de comentário.
ele tem várias linhas!
*/
```

## Variáveis e tipos de dados

Java é uma linguagem com **tipagem estática**, ou seja, para você declarar uma variável, é necessário especificar a qual tipo ela pertence. Isso é necessário para que a JVM consiga fazer a alocação correta de memória para aquele tipo específico de dado.

Os tipos de dados primitivos em Java são **boolean**, **byte**, **char**, **short**, **int**, **long**, **float** e **double**. Uma variável do tipo primitivo pode armazenar exatamente um valor de seu tipo declarado por vez, quando outro valor for atribuído a essa variável, seu valor inicial será substituído.

A tabela abaixo indica os tipos de dados primitivos que podemos utilizar em Java:

| **Nome** | **Tipo** | **Tamanho**                                                                                                                | **Valor inicial** |
|----------|----------|----------------------------------------------------------------------------------------------------------------------------|-------------------|
|  boolean | booleano | 1 bit<br/>0 ou 1                                                                                                           | false             |
|   byte   |  inteiro | 1 byte<br/>-128 a 127                                                                                                      | 0                 |
|   short  |  inteiro | 2 bytes<br/>-32.768 a 32.767                                                                                               | 0                 |
|    int   |  inteiro | 4 bytes<br/>-2.147483.648 a 2.147.483.647                                                                                  | 0                 |
|   long   |  inteiro | 8 bytes<br/>-9.22E18 a 9.22E18                                                                                             | 0                 |
|   float  |  decimal | 4 bytes<br/>faixa de 1.401298464324817e-45f até 3.402823476638528860e+38f<br/>precisão de 6 ou 7 dígitos significativos    | 0                 |
|  double  |  decimal | 8 bytes<br/>faixa de 4.94065645841246544e-324 até 1.79769313486231570e+308<br/>precisão de 14 ou 15 dígitos significativos | 0                 |
|   char   |   texto  | 2 bytes<br/>usa o código UNICODE                                                                                           | '0'               |

A escolha do tipo de dado para uma variável depende do que deve ser armazenado nessa variável. Isso exige um conhecimento prévio de como ela será usada e de que forma será manipulada. Se o tamanho do sistema não for significativo, pode-se optar por variáveis de tipo `int` e `double`. Se for um sistema mais complexo e que utilize um número grande de variáveis para o processamento, deve-se ser um pouco mais rigoroso nas definições.

Adicionalmente aos tipos primitivos, é comum trabalharmos com dados do tipo `String`, que são uma sequência de caracteres. Em Java, uma string é sempre um objeto da classe `String`, portanto deve ser declarada como tal.

A sintaxe para declaração de variáveis é a seguinte:

``` java
<tipo_dado> <nome_var> [= <valor_inicial>];
```

Algumas observações:

* Os tipos `long` e `float` precisam que seja incluído um "marcador" (respectivamente `l` e `f`) após a instanciação do valor;
* Utilizamos o padrão **camelCase** para nomeação de variáveis em Java, com a primeira letra da variável minúscula e a primeira letra de cada palavra posterior em caixa alta;
* Os valores lógicos de verdadeiro e falso são escritos em caixa baixa, `true` e `false` respectivamente.

O bloco abaixo indica uns exemplos de declarações de variáveis em Java:

``` java
public class Variaveis {
    public static void main(String[] args) {
        // Variáveis - Tipos Primitivos
        // Dados inteiros:
        byte idade = 15;
        short ano = 2021;
        int negativo = -15000;
        long muitoGrande = 78522214801l;

        // Dados em ponto flutuante:
        double piLongo = 3.14159265358979;
        float pi = 3.14f;

        // Dados booleanos:
        boolean verdadeiro = true;
        boolean falso = false;

        // Caracteres:
        char letra = 'a'; // Usa o código UNICODE e ocupa 2 bytes
        String nome = "André";
    }
}
```

É possível converter tipos de dados em outros tipos, numa operação chamada de _type casting_. Para isso, deve-se incluir o tipo para o qual se deseja converter o dado entre parênteses, antes do valor desejado, como no exemplo abaixo:

``` java
int m = 2;
double n = 5.6;

System.out.println(m); // 2
System.out.println(n); // 5.6

int o = (int) n;
double p = (double) m;

System.out.println(o); // 5
System.out.println(p); // 2.0
```

## Operadores

### Operadores aritméticos

Em Java temos cinco operadores aritméticos básicos:

| + | soma                               |
| - | subtração                          |
| * | multiplicação                      |
| / | divisão                            |
| % | operador módulo (resto da divisão) |

Esses operadores podem ser usados entre duas variáveis ou dados, ou antes da atribuição, como apresentado abaixo:

``` java
int numero1 = 5;
int numero2;

numero2 = numero1 + 4;
numero1 -= 10; // numero1 = numero1 - 10;
```

É importante reforçar que a operação de divisão entre valores inteiros (`int` ou `long`, por exemplo) sempre produz um valor inteiro, descartando-se a parte fracionária. `9 / 6`, por exemplo, retorna `1`, enquanto que `9 / 6.0` ou `9.0 / 6` retorna `1.5`.

Além deles, o Java possui operadores de incremento e decremento, que são bastante utilizados. Eles são representados por `++` e `--`, e podem ser declarados antes ou depois da variável e incrementam ou decrementar em 1 o valor da variável;

``` java
int numero = 5;
numero++; // numero passa a ser 6
numero--; // numero passa a ser 5 novamente
```

Quando o operador é declarado antes da variável, o incremento ou decremento é realizado antes do valor da variável ser lido para o processamento. Quando é declarado depois, ocorre o contrário. Como ilustração, considere os comportamentos indicados nos comentários abaixo:

``` java
public class Incremento {
    public static void main(String[] args) {
        int idade = 15;

        idade = idade + 1; // 16
        idade += 1; // 17

        // Pós incremento
        idade++; // idade 18

        int novaIdade = idade++;

        System.out.println(idade); // 19
        System.out.println(novaIdade); // 18

        // Pré incremento
        int novaNovaIdade = ++idade;

        System.out.println(idade); // 20
        System.out.println(novaNovaIdade); // 20

        idade--;
        --idade;
    }
}
```

Como foi possível ver, no momento da declaração de `novaIdade`, primeiramente ocorre a atribuição do valor, ou seja, `novaIdade` recebe o valor `18`. Logo em seguida, há o incremento na variável `idade`, e ela passa a ter o valor `19`. Já na declaração de `novaNovaIdade`, primeiramente há o incremento de `idade`, ou seja, `idade` primeiro passa a ter o valor `20`, para depois `novaNovaIdade` receber o seu valor, ou seja, `20`.

Como exercício, tente prever os valores de `idade` nas últimas duas linhas. Inclua linhas para imprimir na tela o valor da variável em cada etapa.

### Operadores relacionais

Os operadores relacionais ou de comparação são seis, no total: `==` (igual a), `!=` (diferente de), `>` (maior que), `>=` (maior ou igual a), `<` (menor que) e `<=` (menor ou igual a). Ao contrário dos operadores aritméticos, que geram novos valores numéricos, os operadores relacionais retornam sempre um valor booleano, `false` ou `true`, conforme as operações são consideradas falsas ou verdadeiras, respectivamente.

### Operadores lógicos

Os operadores lógicos recebem valores booleanos como operandos, e assim como os operadores relacionais, eles retornam valores booleanos. São apenas três: **E**, representado por `&&`; **OU**, representado por `||`; e **NÃO**, representado por `!`.

### Precedência de operadores

Os operadores aritméticos possuem uma precedência assim como na matemática, ou seja, os operadores `*`, `/` e `%` são executados antes de `+` e `-`. Os demais tipos de operadores possuem o mesmo nível de precedência, e são executados da esquerda para a direita. Assim como em outras linguagens, é possível forçar a precedência em uma operação, utilizando-se `()`.

## Estruturas de decisão

O Java possui duas aplicações das estruturas de decisão, o `if-else` e `switch`.

### `if-else`

Em Java, todo início de bloco deve ser inserido entre chaves, `{}`. Além disso, os testes lógicos das estruturas de seleção devem ser incluídos entre parênteses, `()`. A sintaxe para o `if-else` é a seguinte:

``` java
if (condicao) {
    codigo;
} else if (condicao) {
    codigo;
} else {
    codigo;
}
```

As instruções `else if` e `else` são opcionais. Onde foi indicada uma `condicao`, inclua o teste lógico que deseja que seja executado para se entrar no bloco. É possível ter quantas instruções `else if` desejar, porém deve-se levar em consideração que o número de caminhos aumenta quadraticamente quanto maior o número de casos possíveis. Portanto, caso o seu `if` tenha muitas situações `else if`, considere a possibilidade de refatorar o seu código. É possível ter apenas uma instrução `if` e uma instrução `else` por comando.

O bloco pode conter quantas instruções for desejado, inclusive outras estruturas de decisão ou de repetição. É uma boa prática indentar os blocos mais internos. Isso facilita muito a legibilidade do código, e simplifica a manutenção.

``` java
int idade = 15;

if (idade < 18) {
    System.out.println("Não pode entrar");
} else {
    System.out.println("Pode entrar");
}

boolean amigoDoDono = true;

if (idade < 18 && amigoDoDono == false) {
    System.out.println("Não pode entrar");
} else {
    System.out.println("Pode entrar");
}
```

Caso o bloco possua apenas uma instrução, sintaticamente é possível suprimir as chaves do bloco. O primeiro exemplo acima poderia ficar, por exemplo:

``` java
int idade = 15;

if (idade < 18)
    System.out.println("Não pode entrar");
else
    System.out.println("Pode entrar");
```

Apesar de ficar visualmente mais agradável, não é uma boa prática suprimir as chaves. Em Java, as chaves indicam a existência de um novo bloco para qualquer outra situação, e suprimi-las pode deixar o código propenso a falhas no futuro, pois um desenvolvedor (podendo inclusive ser o programador original) pode esquecer de inserir as chaves e incluir outras instruções no bloco, causando um erro no programa.

### `switch`

Já a instrução `switch` é utilizada quando se deseja verificar o comportamento de uma única variável. Consideram-se vários casos, um para cada valor possível. A sintaxe utilizada é indicada abaixo:

``` java
switch (variavel) {
    case valor1:
        codigo;
        break;
    case valor2:
        codigo;
        break;
    // [...]
    default:
        codigo;
}
```

A instrução `break` é obrigatória ao final de cada `case`. A instrução `default` é opcional e pode ser omitida. Caso não haja nenhuma equivalência aos valores indicados em cada `case`, o programa entra no bloco do `default`. Caso não haja um bloco `default`, o programa ignora o `switch` e segue adiante no código.

Veja que só são incluídas chaves após a instrução `switch`. Não são usadas chaves nos `case`, e nem no `default`.

``` java
int numero = 10;

switch (numero) {
    case 1:
        System.out.println("Um");
        break;
    case 2:
        System.out.println("Dois");
        break;
    default:
        System.out.println("Muito alto");
}
```

No exemplo acima, `numero` não é igual a nenhum dos `case` apresentados, `1` ou `2`. Sendo assim, o código entra no bloco `default` e exibe na tela a mensagem `Muito alto`.

## Estruturas de repetição

O Java possui duas estruturas de repetição possíveis, `for` e `while`.

### `while`

Sintaxe padrão:

``` java
while (condicao) {
    codigo;
}
```

De forma similar ao `if`, o programa entra no bloco do `while` caso `condicao` seja verdadeira. Ao final da execução do bloco, o programa volta a testar `condicao` e, caso ela continue verdadeira, executa novamente o bloco. Essa estrutura se repete até que `condicao` passe a ser falsa.

``` java
int idade = 15;
while (idade < 18) {
    idade++;
    System.out.println(idade);
}
```

No exemplo acima, o programa exibe os números `15`, `16` e `17` na tela, interrompendo o `while` quando `idade` chega ao valor de `18`.

### `for`

Sintaxe padrão:

``` java
for (inicializacao; condicao; incremento) {
    codigo;
}
```

Dentro dos parênteses há três campos:

* `inicializacao` indica qual será a variável de controle da estrutura de repetição. Deve-se declarar uma variável de contagem no próprio campo, como por exemplo `int i = 0`;
* `condicao` indica o teste lógico que deve ser verdadeiro para que se continue executando o bloco da estrutura. Quando `condicao` for falsa, a estrutura é interrompida;
* `incremento` indica qual deve ser o incremento (ou decremento) da variável de controle. É comum se utilizar o operador `++` nessas condições.

Um exemplo de uso de `for` que tem exatamente o mesmo comportamendo do exemplo do `while` apresentado anteriormente está indicado abaixo:

``` java
idade = 15;
for (int i = 15; i < 18; i++) {
    idade++;
    System.out.println(idade);
}
```

É importante destacar que, no exemplo, a variável `i` possui um escopo fechado, dentro do bloco `for`. Não é possível utilizá-la após o encerramento do bloco.

O `for` possui uma segunda sintaxe possível, mas para isso precisamos ver algumas estruturas de dados mais complexas, portanto ela será apresentada posteriormente no curso.

### Instruções `break` e `continue`

Ambas as estruturas de repetição, `for` e `while`, possuem duas instruções especiais. A instrução `break` é usada quando se deseja interromper a execução da estrutura de repetição por completo. O programa para de rodar a estrutura e passa para a instrução seguinte. Já a instrução `continue` encerra apenas a iteração que está sendo executada no momento, e o programa retorna para o teste da `condicao`.

No exemplo abaixo, o programa exibe na tela os valores `5` a `18`, um em cada linha. Quando `i` recebe o valor `19`, o programa entra no bloco `if`, exibe a mensagem indicada na tela e em seguida exibe a mensagem `Fim do programa`, indicando que saiu do bloco `for` após a instrução `break`.

``` java
int x = 5;
int y = 30;

for (int i = x; i < y; i++) {
    if (i % 19 == 0) {
        System.out.println("Achei um número divisível por 19");
        break;
    }
    System.out.println(i);
}

System.out.println("Fim do programa");
```

Já no exemplo a seguir, o programa vai exibindo na tela a partir do valor `0`, sempre incrementando a variável `i` em 1, até chegar no valor `50`. Quando `i` é incrementado para `51`, o programa passa a entrar no bloco `if`, que tem uma instrução `continue`. Sendo assim, até o valor `59`, o programa não entra na linha que manda exibir `i` na tela. O próximo valor a ser exibido é, portanto, `60`.

``` java
for (int i = 0; i < 100; i++) {
    if (i > 50 && i < 60) {
        continue;
    }
    System.out.println(i);
}
```

## Exercícios complementares

1. Crie um programa para imprimir uma mensagem, como "olá, mundo!".
2. Altere o programa anterior para imprimir duas linhas de texto usando duas linhas de código `System.out`.
3. Sabendo que os caracteres `\n` representam uma quebra de linhas, imprima duas linhas de texto usando uma única linha de código `System.out`.
4. Na empresa onde trabalhamos, há tabelas com o quanto foi gasto em cada mês. Para fechar o balanço do primeiro trimestre, precisamos somar o gasto total. Sabendo que, em janeiro, foram gastos R$15.000, em fevereiro, R$23.000 e em março, R$17.000, faça um programa que calcule e imprima o gasto total no trimeste.
5. Adicione código (sem alterar as linhas que já existem) na classe anterior para imprimir a média mensal de gasto.
6. Faça um programa que peça as três notas da disciplina (AP1, AP2 e AC) e mostre a média. A média é calculada de acordo com a fórmula `M = (AP1 + AP2) * 0.4 + AC * 0.2`.
7. Imprima todos os números de 150 a 300.
8. Imprima a soma de 1 até 1000.
9. Imprima todos os múltiplos de 3, entre 1 e 100.
10. Imprima os fatoriais de 1 a 10.
11. Imprima os primeiros números da série de Fibonacci até passar de 100. Considere que o primeiro número da série é 1 e o segundo é 1.
12. Para todos os números entre 2 e 100, exiba na tela apenas os primos.
13. Escreva um programa que, dada uma variável `x` com algum valor inteiro, recalcule `x` de tal forma que seja igual a `x / 2` se `x` for par, e `3 * x + 1` se `x` for ímpar. O programa deve parar quando `x` tiver o valor final de 1. Por exemplo, para `x = 13`, a saída será `40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1`. *Dica:* utilize a função `System.out.print` para imprimir um dado sem quebrar linha.
