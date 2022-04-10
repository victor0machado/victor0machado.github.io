# Introdução a Python

Com os conceitos básicos de algoritmos e lógica de programação, conseguimos agora discutir sobre a sintaxe e as particularidades da linguagem Python. Veremos nesta aula alguns conceitos básicos de Python, e para começarmos a nos acostumar às consultas na documentação oficial, vou apresentar alguns links com informações importantes.

### Índice

1. [Sobre um arquivo Python](#sobre-um-arquivo-python)
2. [Documentando o código](#documentando-o-código)
3. [Exibindo dados na tela](#exibindo-dados-na-tela)
4. [Tipos de dados em Python](#tipos-de-dados-em-python)
5. [Lendo dados do usuário](#lendo-dados-do-usuário)
6. [Atribuindo valores para variáveis](#atribuindo-valores-para-variáveis)
7. [Alterando tipos](#alterando-tipos)
8. [Exercícios complementares](#exercícios-complementares)
9. [Sugestões de conteúdos](#sugestões-de-conteúdos)

## Sobre um arquivo Python

Um arquivo Python (também chamado de um **módulo** Python) pode ser escrito como um texto normal. Podemos inclusive usar o tradicional bloco de notas para escrever código, apesar de não ser uma experiência interessante. Usualmente, códigos escritos em Python possuem algumas extensões típicas para que eles possam ser reconhecidos. As mais comuns são **.py**, **.pyc** e **.pyw**. Para este curso, trabalharemos apenas com a extensão **.py**.

Usualmente, trabalhamos com algum editor de códigos, que possui ferramentas específicas para auxiliar a nossa vida. Os [slides da disciplina](/assets/prog/slides.pdf) possuem algumas sugestões de IDEs, como o IDLE, PyCharm e o VSCode. Este último é o que eu uso profissionalmente, e recomendo, apesar de exigir um pouco mais de estudo por parte do usuário, e paciência para começar a ganhar produtividade.

Para a primeira parte do curso, no entanto, vamos usar o [Replit](http://www.replit.com). Este é um editor disponibilizado na nuvem, de forma que seja simples começar a programar. Para criar um novo projeto, basta fazer o login e criar um novo _repl_, lembrando sempre se selecionar a opção **Python**.

## Documentando o código

O primeiro passo que temos em todo projeto de software é aprender a documentá-lo bem. Desde cedo, é importante aprender que não escrevemos código para nós mesmos. Em uma empresa, o seu código entrará em produção e só será alterado daqui a anos, possivelmente por outra pessoa. Mesmo quando estamos trabalhando em projetos pessoais, é importante documentar nosso trabalho, de forma que fique fácil recuperar informações após alguns meses (ou mesmo anos).

Em Python, usamos um recurso chamado **docstring**. Podemos utilizar docstrings nos arquivos e em cada função, classe ou método que construirmos (vamos falar sobre isso em aulas futuras). Uma docstring nada mais é do que um resumo do que aquele módulo em particular faz. Para construir uma docstring, envolvemos o texto em **três aspas duplas**, como no exemplo abaixo:

``` python
"""
Este é um exemplo de docstring.
Você pode usar quantas linhas achar necessário!
"""
```

Quando o interpretador do Python é executado, ele simplesmente ignora qualquer informação contida entre essas três aspas duplas, quando ela estiver sem nenhuma instrução específica. O guia oficial de estilo do Python, [PEP-8](https://peps.python.org/pep-0008/), no entanto, recomenda que esse uso seja restrito às primeiras linhas do módulo e às primeiras linhas de funções, classes e métodos.

Para documentar o código ao longo do arquivo, o melhor é trabalhar com comentários mais simples, que sejam sucintos e ocupem, no máximo, uma linha. Para isso, utilizamos o símbolo `#`, como no exemplo abaixo:

``` python
# Este é um comentário de uma linha.
# Para comentar outra linha, é necessário incluir o # novamente.
```

Assim como nas três aspas duplas, o interpretador ignora o conteúdo após o `#`. É importante destacar que, apesar de comentários e documentação serem extremamente importantes, temos que ter bom senso na hora de comentar. Se você precisar incluir 5 linhas de comentários para explicar uma determinada operação, isso pode ser um sinal que o seu código pode ser melhorado.


## Exibindo dados na tela

Toda linguagem de programação precisa de uma forma simples para entrada e saída de dados. Para a saída de dados, utilizamos a função [`print()`](https://docs.python.org/pt-br/3/library/functions.html#print). Uma função nada mais é que um procedimento "encapsulado" em uma representação mais simples. O Python oferece uma série de funções pré-definidas para podermos utilizar, mas também é possível criar funções próprias, como faremos nas próximas aulas.

Retornando à função `print()`, ela recebe, como parâmetros de entrada, as informações que devem ser exibidas na tela. Considere, por exemplo, a função abaixo:

``` python
print("Olá, mundo!")
```

Podemos colocar quantos parâmetros quisermos na função `print()`. Ela possui um parâmetro especial, chamado `sep`, que define qual o caractere separador dos parâmetros inseridos. O valor padrão para `sep` é um espaço em branco. No exemplo abaixo, por exemplo, seria exibido na tela o valor `Olá, mundo!`:

``` python
print("Olá,", "mundo!")
```

Para mudarmos o caractere separador, basta incluir o parâmetro `sep` adicional. No exemplo abaixo, seria exibido na tela o valor `Olá,-mundo!`:

``` python
print("Olá,", "mundo!", sep="-")
```

## Tipos de dados em Python

Na seção anterior utilizamos os textos entre aspas duplas. Um texto compõe um dos quatro tipos de dados principais em Python, chamados **tipos primitivos**, que são explicados abaixo. É importante ressaltar que, apesar de termos usado o `print()` com dados de texto, é possível utilizar qualquer tipo de dados.

### Booleanos

O valore booleano, chamado de `bool`, é o menor tipo de dado que podemos ter. Um dado `bool` só pode ter um entre dois valores: verdadeiro ou falso. Esses valores são representados no código como `True` e `False`, respectivamente. É importante prestar atenção no fato de que esses valores começam com um caractere maiúsculo! O valor `True` é completamente diferente do símbolo `true`.

### Inteiros

Dados inteiros são representados como `int`. Podemos utilizar qualquer valor numérico inteiro nesse caso, como `2`, `5`, `0` ou `-10`.

### Decimais

Números decimais são chamados de `float` em Python e em muitas outras linguagens. Um número decimal é representado utilizando um ponto como separador, e não uma vírgula, como estamos acostumados. Então temos exemplo `2.0`, `5.16`, `0.0` ou `-10.3456`. Aqui é importante ressaltar que, apesar de significarem o mesmo valor matemático, as representações `2` e `2.0` são diferentes! Uma é `int` e outra é `float`.

### Texto

Dados tipo texto são chamados de **strings** ou `str` em Python. Basicamente, podemos representar qualquer informação no formato de string. Para isso, devemos envolver o texto em aspas duplas ou simples, como `"Olá, mundo"` e `'Olá, mundo'`. Importante ressaltar que não podemos misturar as aspas, ou seja, não é possível começar com aspas duplas e terminar com aspas simples, ou vice-versa. Então, um texto do tipo `"Olá, mundo'` retornará um erro.

Alguns caracteres especiais exigem uma representação especial quando escrevemos strings. Abaixo há alguns exemplos, mas ao longo do curso veremos outros:

* `\"`: inclui uma aspa dupla;
* `\\`: inclui uma contrabarra;
* `\n`: inclui uma quebra de linha (pula uma linha);
* `\t`: inclui uma tabulação (o famoso tab).

Portanto, se quisermos colocar aspas entre `mundo`, precisamos fazer algo assim (claro que também poderíamos usar aspas simples ao redor da string):

``` python
print("Olá, \"mundo\"!")
```

Assim como no caso das representações `2` e `2.0` serem diferentes, as representações `"2"` e `"2.0"` também são diferentes das suas contrapartes numéricas. Para que essas representações de texto e numéricas conversem entre si, é necessário alterar seus tipos. Vamos falar sobre isso ainda nesta nota de aula.

### Dados nulos

A função `print()` não retorna um valor para o código. Quando uma função não retorna nenhuma informação, o Python intepreta que esse retorno é um valor nulo. Apesar de não ser um tipo primitivo, é importante destacar o valor nulo logo no início da sua jornada com o Python. Representamos esse valor como sendo `None`.

### Listas

Apesar de não ser um tipo de dado primitivo, também é importante dizer que em Python temos o conceito de arranjos incorporados nas **listas**, ou `list`. Ao contrário da definição formal de arranjo, no entanto, uma lista pode ter uma mistura de qualquer tipos de dados, inclusive outras listas e estruturas de dados que ainda não vimos. Por exemplo, a lista `[1, 2, "abc", [4, 5], False]` é perfeitamente possível, apesar de ser desencorajada por conta da potencial dificuldade de ter que lidar com vários tipos de dados diferentes.

Representamos listas por colchetes, com seus elementos separados por vírgulas. Os elementos estão associados a índices começando pelo zero, como nos arranjos. Identificamos um elemento em particular da lista incluindo o índice entre colchetes, como `A[4]` para indicar o quinto elemento de `A`.

Listas possuem uma lista de funções e recursos gigantesca, e não é o caso de explorá-la neste momento. Por enquanto, basta saber que podemos agrupar os dados em listas.

## Lendo dados do usuário

Entendemos como exibimos dados na tela, e quais tipos de dados podemos usar. Vamos ver agora como podemos ler dados.

Apesar de pouco usado no dia-a-dia, a função [`input()`](https://docs.python.org/pt-br/3/library/functions.html#input) é a forma mais simples de recebermos algum tipo de dado externo à implementação do código. Para usar a função, basta inserir o _prompt_, ou a chamada para a leitura do dado, entre os parênteses, como no exemplo abaixo:

``` python
input("Informe um número: ")
```

No momento em que o interpretador identificar um `input()`, ele interrompe a execução do código e dá o acesso para que o usuário insira uma informação no console. No momento que o usuário insere o valor e aperta enter, o Python retoma a execução, retornando em `print()` o valor inserido pelo usuário. Importante ressaltar que a função `input()` sempre retorna um valor de tipo `str`, mesmo que o dado inserido pelo usuário seja numérico!

## Atribuindo valores para variáveis

Para podermos usar o valor retornado pela função `input()`, e para armazenar os tipos de dados que temos falado, precisamos utilizar o recurso de **variáveis**. Variáveis nada mais são que símbolos que indicam para o interpretador Python um determinado endereço na memória. Uma das grandes vantagens do Python para quem está aprendendo é que o próprio interpretador se encarrega de escolher qual é este endereço, e quanto de memória deve ser reservado para aquele dado em particular.

Para atribuirmos um determinado valor para uma variável, utilizamos o símbolo `=`. No exemplo abaixo, lemos como sendo **x recebe o valor de 2**:

``` python
x = 2
```

Não precisamos atribuir apenas dados de tipos primitivos às variáveis. Podemos também incluir o retorno de funções, como o da própria função `input()`:

``` python
nome = input("Informe o seu nome: ")
```

O Python tem uma particularidade frente a outras linguagens populares, como C e Java, em que a alocação das variáveis é **dinâmica**, ou seja, não é preciso especifica o tipo de dado que a variável vai receber, o próprio interpretador se encarrega de entender o que está sendo passado para a variável. O caso abaixo, por exemplo, é totalmente válido:

``` python
x = 2
x = "olá, mundo"
```

No entanto, ficar trocando o tipo da variável não é muito recomendado, devendo ser restrito a casos muito específicos (e bem documentados). Inclusive, existe um guia para deixar os tipos das variáveis mais claros para os programadores, utilizando um conceito chamado de [_type hints_](https://peps.python.org/pep-0484/).

Um outro ponto importante com relação a variáveis é como nomeá-las. O [PEP-8](https://peps.python.org/pep-0008/) contém uma série de recomendações, e temos outras restrições da linguagem. Abaixo seguem as recomendações que considero mais importantes:

* Não deve começar com valores numéricos (p.ex., `12var`). Após o primeiro caractere, no entanto, é possível usar números (p.ex., `n1`);
* Não use símbolos especiais, como `?`, `#` ou `!`, ou letras acentuadas, como `á`, `ç` ou `õ`;
* Utilize sempre letras minúsculas, e separe palavras com um `_`, como `valor_procurado`;
* Não utilize palavras reservadas da linguagem, como `int`, `def`, `bool` ou `list`;
* Crie variáveis com nomes claros, em que o seu conteúdo seja facilmente compreendido por quem estiver lendo o código.

Como regra geral, o ideal é só utilizar letras e o `_` para variáveis. Números devem ser usados em casos muito particulares, e evitados sempre que possível.

## Alterando tipos

Vimos anteriormente que os dados `2` e `"2"` são diferentes. O primeiro é `int`, enquanto que o segundo é `str`. Vimos também que a função `input()` sempre retorna uma string, independente do valor inserido pelo usuário. Nesses e em outros casos, pode ser interessante fazer uma conversão de tipo dos dados, que chamamos comumente de _typecasting_. Para isso, basta colocar o dado a ser convertido dentro da função de tipo que para o qual você deseja converter: `int()`, `float()`, `str()` ou `bool()`, como nos exemplos abaixo:

``` python
int(6.8)      # 6
float("7.9")  # 7.9
str(True)     # "True"
bool(0)       # False
```

Duas observações sobre typecasting em Python:

* Não tente converter dados não numéricos em números! Chamar `float("olá")` vai retornar uma exceção;
* O Python considera que qualquer valor diferente de `0`, `0.0`, `""`, `[]` (ou qualquer outra representação de dados vazios ou nulos) seja um valor verdadeiro. Então `bool("olá")` é verdadeiro, e `bool([])` é falso.

A conversão pode ocorrer direto na chamada da função `input()`, ou de qualquer outra função, como no exemplo abaixo:

``` python
numero = float(input("Informe um valor: "))
```

## Exercícios complementares

1. Faça um programa que escreva a mensagem "Olá, mundo!" na tela.
2. Faça um programa que peça um número e então mostre a mensagem `O número informado foi [número]`.
3. Faça um programa que leia o seu nome e exiba na tela `Prazer, [nome], eu sou o Python!`.

## Sugestões de conteúdos

* Material online:
  * [Este vídeo](https://www.youtube.com/watch?v=31llNGKWDdo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=5) do Curso em Vídeo sobre os primeiros comandos em Python;
  * [Esta página](https://www.webopedia.com/definitions/floating-point-number/#:~:text=The%20term%20floating%20point%20is,the%20decimal%20point%20can%20float.) que explica porque valores decimais são chamados de `float`;
  * [Este artigo](https://towardsdatascience.com/introduction-to-python-c43e17aaa78b) com uma introdução rápida ao Python.

