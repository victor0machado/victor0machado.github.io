# Operadores

Na última nota de aula discutimos os elementos fundamentais para a programação em Python, que envolve a entrada e saída de dados (respectivamente `input()` e `print()`), além dos tipos de dados primitivos disponíveis na linguagem. Falamos também sobre variáveis e sobre como alterar os tipos dos dados utilizados, chamado _typecasting_.

Nesta nota de aula vamos discutir um pouco sobre como podemos operar sobre dados em Python. Veremos três tipos de operadores: aritméticos, relacionais e lógicos. Por fim, veremos também alguns usos adicionais para operadores aritméticos e relacionais em dados não numéricos. Alguns outros operadores serão abordados ao longo do curso, como o de pertencimento (`in` e `not in`).

### Índice

1. [Operadores aritméticos](#operadores-aritméticos)
2. [Operadores relacionais](#operadores-relacionais)
3. [Operadores lógicos](#operadores-lógicos)
4. [Precedência de operadores](#precedência-de-operadores)
5. [Exercícios complementares](#exercícios-complementares)
6. [Sugestões de conteúdos](#sugestões-de-conteúdos)

## Operadores aritméticos

Os operadores artiméticos são aqueles usados para manipular valores numéricos. Temos disponíveis, além das quatro operações fundamentais, três operadores muito importantes: potenciação, divisão inteira e o operador módulo.

### Operadores fundamentais

São os operadores de soma (`+`), subtração (`-`), multiplicação (`*`) e divisão (`/`). O uso é idêntico ao que usamos na matemática:

``` python
x = 2
y = 5

print(x + y)  # 7
print(x - y)  # -3
print(x * y)  # 10
print(x / y)  # 0.4
```

Normalmente utilizamos espaços entre os operadores e os valores ou variáveis, para aumentar a legibilidade do código.

Um ponto importante: nas operações de soma, subtração e multiplicação, o tipo dos dados são mantidos, ou seja, se ambos os operandos forem do tipo `int`, o resultado também será `int`. Se um ou ambos os operandos forem `float`, o resultado também será `float`. Já na operação de divisão, o resultado é sempre do tipo `float`. Portanto, uma operação `4 / 2` retornará `2.0`. Isso se deve à forma como a operação de divisão é realizada internamente pelo interpretador.

### Potenciação e divisão inteira

O operador potência é representado pelo símbolo `**`. Já a operação divisão inteira, representada por `//` sempre retorna a parte inteira de uma divisão. É importante frisar que não é um arredondamento, e sim um truncamento, ou seja, a operação ignora a parte decimal do valor resultante. O retorno de ambas as operações segue as mesmas regras do retorno da operação soma.

``` python
print(4 ** 2)      # 16
print(2.0 ** 3)    # 8.0
print(15 // 2)     # 7
print(2.5 // 1.5)  # 1.0
print(4 // 3.0)    # 1
```

### Operador módulo

O operador módulo pode confundir inicialmente por não ser a mesma operação módulo que conhecemos na matemática, aquela em que consideramos sempre o valor positivo do operando (`|-2| = 2`). Em programação, o operador módulo refere-se ao resto da divisão inteira, e é representado pelo símbolo `%` em Python. Dessa forma, as operações divisão, divisão inteira e módulo são relacionadas conforme apresentado abaixo:

```
a / b = q com resto r

b * q + r = a

0 <= r <= b
```

Portanto, para determinar o retorno da operação módulo, divide-se um operando pelo outro, obtém-se a parte inteira e, a partir daí, é calculado o valor do resto. Este resto é o resultado da operação. O tipo retornado pela operação segue a mesma regra da operação soma.

``` python
print(5 % 2)      # 1
print(5 % 2.0)    # 1.0
print(4.5 % 2)    # 0.5
```

O operador módulo é usado diversas vezes no desenvolvimento de software. Duas aplicações relativamente comuns são apresentadas abaixo:

#### Regras de divisibilidade

A forma mais direta de se identificar que um número é divisível por outro é utilizar o operador módulo e verificar se o resultado da operação é igual a zero. Para determinar se um número é par, por exemplo, basta realizar a operação módulo deste número por dois. Caso o resultado seja zero, o número é par.

``` python
print(5 % 2)   # 1, 5 é ímpar
print(16 % 4)  # 0, 16 é divisível por 4
```

#### Transformação de listas lineares em matrizes

Veremos aplicações de listas e matrizes mais à frente no curso, mas podemos abstrair e pensar num problema em que precisamos transformar uma sequência linear de números em uma matriz bidimensional. Por exemplo, considere a seguinte transformação:

```
1 4 6 7 2 8 3 4 1

1 4 6
7 2 8
3 4 1
```

Para realizar essa transformação, devemos considerar o índice da sequência linear, a partir do 0. Ou seja, o índice 0 representa o valor 1, o índice 1 representa o valor 4, etc. A partir desse índice, devemos determinar onde um determinado elemento deve ser posicionado na matriz, considerando o índice da linha (0, 1 ou 2) e o índice da coluna (0, 1 ou 2). Podemos fazer isso através dos operadores divisão inteira e módulo.

A operação divisão inteira por 3 vai me retornar em qual linha o elemento deve ser inserido, e o operador módulo indica a coluna. Considere, por exemplo, o elemnto `8`, de índice `i = 5`.

``` python
print(i // 3)  # 1, índice da linha
print(i % 3)   # 2, índice da coluna
```

Dessa forma precisamos colocar o elemento 8 na terceira coluna (de índice 2) e na segunda linha (de índice 1). Podemos fazer isso para qualquer valor de `i`.

## Operadores relacionais

Os operadores relacionais (ou de comparação) são aqueles que comparam os valores numéricos. Esses operadores retornam um valor booleano (`True` ou `False`) e são indicados abaixo:

``` python
x = 2
y = 5

print(x > y)    # False, maior que
print(x >= y)   # False, maior ou igual a
print(x < y)    # True, menor que
print(x <= y)   # True, menor ou igual a
print(x == y)   # False, igual a
print(x != y)   # True, diferente de
```

## Operadores lógicos

Ao contrário dos anteriores, os operadores lógicos (ou booleanos) precisam de valores lógicos como operandos. Esses operadores usam regras da lógica para retornarem os seus resultados, e são, no total, três:

* `and`: retorna `True` caso ambos os operandos sejam `True`, ou `False` caso contrário;
* `or`: retorna `False` caso ambos os operandos sejam `False`, ou `True` caso contrário;
* `not`: retorna `True` caso o operando seja `False`, ou `False` caso o operando seja `True`.

``` python
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

### Operações lógicas com valores não-booleanos

Caso sejam usados valores não-booleanos em operações lógicas, os operadores `and` e `or` possuem um comportamento que pode ser contraintuitivo, apresentado abaixo:

* `and`: retorna o primeiro valor equivalente a `False` se há algum, caso contrário retorna o último valor da expressão;
* `or`: retorna o primeiro valor equivalente a `True` se há algum, caso contrário retorna o último valor da expressão.

Nesse caso, estamos considerando a mesma regra que falamos quando discutimos [typecasting](003-intro-python.md#alterando-tipos): valores diferentes de `0`, `""`, `[]` ou algo equivalente sempre são considerados `True`.

``` python
print(5 and "oi")   # "oi"
print(0 and "oi")   # 0
print([] or 16)     # 16
print(False or "")  # ""
```

Esse caso é comumente usado quando queremos fazer uma atribuição de variáveis que podem receber dois tipos de valores, mas um deles é potencialmente algo como `None`. Nesse caso, temos um dado _default_ que pode ser atribuído.

``` python
x = None
y = 16

z = x or y  # 16
```

## Precedência de operadores

Assim como na matemática tradicional, devemos ter uma ordem de execução entre diversos operadores. Em Python, temos a seguinte ordem, que pode ser alterada caso usemos parênteses (`()`):

* `()`;
* `**`;
* `*`, `/`, `//`, `%`;
* `+`, `-`;
* `==`, `!=`, `>`, `>=`, `<`, `<=`;
* `not`;
* `and`;
* `or`;

Na lista acima, quando temos mais de um operador na mesma ordem de precedência, executamos na ordem em que eles aparecem, da esquerda para a direita. Alguns exemplos são mostrados abaixo:

``` python
print(2 * 3 ** 2)               # 18
print((2 * 3) ** 2)             # 36
print(4 + (3 - 1) * 2 // 1)     # 8
print(5 % (2.5 + 1 / 2) ** 2)   # 5.0
print(x + 2 < y * (x - 1))      # True
print(x ** (4 - 2) == y - 1)    # True
```

## Exercícios complementares

1. Faça um programa que peça as três notas da disciplina (AP1, AP2 e AC) e mostre a média. A média é calculada de acordo com a fórmula `M = (AP1 + AP2) * 0.4 + AC * 0.2`.
2. Faça um programa que peça um comprimento em metros e converta para centímetros.
3. Faça um programa que leia o raio de um círculo, calcule e mostre sua área. Considere pi como aproximadamente igual a 3.14.
4. Monte um conversor de temperatura, que lê uma temperatura em graus Fahrenheit e mostre a temperatura em graus Celsius. A fórmula para conversão é `C / 5 = (F - 32) / 9`.

## Sugestões de conteúdos

* Material online:
  * [Este artigo](http://python-history.blogspot.com/2010/08/why-pythons-integer-division-floors.html) escrito pelo Guido von Rossum explicando o raciocínio por trás dos operadores de divisão inteira e módulo;
  * [Este artigo no medium](https://medium.com/i-math/intro-to-truth-tables-boolean-algebra-73b331dd9b94) com uma breve introdução a lógica booleana;
  * [Ésta pergunta no Stack Overflow](https://stackoverflow.com/questions/47007680/how-do-and-and-or-act-with-non-boolean-values) sobre operações lógicas com valores não-booleanos.

