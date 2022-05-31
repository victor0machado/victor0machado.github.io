# Estruturas de Dados

Com o conhecimento básico dos conteúdos de Python já vistos, nesta nota de aula vamos focar no desenvolvimento de algumas formas que a linguagem nos dá para armazenar e declarar coleções de dados.

De forma alguma esta nota de aula será completa com relação a esses tópicos - o número de funções e métodos que podem ser usados é gigantesco. No geral, sempre que apresentarmos uma nova estrutura de dados, vamos indicar links para a [documentação oficial do Python](https://docs.python.org/pt-br/3/).

### Índice

1. [Listas](#listas)
2. [Tuplas](#tuplas)
3. [Conjuntos](#conjuntos)
4. [Dicionários](#dicionários)
5. [Exercícios resolvidos](#exercícios-resolvidos)
6. [Exercícios complementares](#exercícios-complementares)

## Listas

*Listas* são a forma mais simples de se registrar coleções de dados em Python. Podemos agrupar em uma lista os mais variados tipos de dados, como strings, números, outras listas e até objetos mais complexos, como funções e classes. A representação de listas é feita com os dados entre colchetes (`[]`), e separados entre vírgulas, como no exemplo abaixo:

``` python
alunos = ["João", "Alessandra", "Felipe", "Bianca"]
```

Como boas práticas para o uso de listas em Python, é recomendado o seguinte:

* Apesar do Python permitir que uma única lista contenha diversos tipos diferentes de dados, é recomendado que se use um mesmo tipo de dado dentro de uma lista. Por exemplo, uma lista de strings representando os alunos de uma turma, uma lista de funções indicando possíveis operações a serem realizadas, ou uma lista de números que represente os pontos ganhos de vários times de futebol;
* Para nomear listas (e quaisquer outras coleções de dados), dê preferência para substantivos no plural, como `alunos`, `notas` ou `operacoes`. Utilize as mesmas regras apresentadas para variáveis e funções (uso de _snake_case_, letras minúsculas, etc.).

Para acessar um determinado elemento da lista, basta utilizar o nome da variável, seguido pelo índice do elemento entre colchetes, considerando que o primeiro elemento possui indice `0` (utilize valores negativos de índice para buscar de trás para frente):

``` python
alunos = ["João", "Alessandra", "Felipe", "Bianca"]

print(alunos[2])  # "Felipe"
print(alunos[-1])  # "Bianca"
```

Deve-se tomar cuidado com o uso de índices que não existem na lista. Fazer isso trará uma exceção na execução:

``` python
alunos = ["João", "Alessandra", "Felipe", "Bianca"]

# print(alunos[5])  -> vai subir uma exceção do tipo IndexError
```

Como mencionado anteriormente, podemos ter qualquer tipo de dado como elementos de listas, incluindo outras listas. Por exemplo, para implementar uma matriz bidimensional com 3 linhas e 2 colunas, basta implementar o seguinte:

``` python
matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]
```

O acesso aos valores de uma lista de listas (ou matriz) pode ser através dos colchetes, como normalmente fazemos com listas unidimensionais. Nesse caso, o primeiro número entre colchetes representa a linha, e o segundo indica a coluna da matriz.

``` python
print(matriz[0][1]) # 2
print(matriz[2][0]) # 5
```

As matrizes não precisam se restringir a apenas duas dimensões. Podemos ter quantas dimensões forem necessárias, sabendo que isso aumenta (muito) a complexidade e o entendimento da nossa estrutura. Normalmente, para matrizes com mais de duas dimensões, normalmente temos alternativas melhores (como dicionários).

### Slicing

Uma técnica interessante para selecionar sublistas dentro de uma determinada lista é o _slicing_, ou fatiamento. Para selecionar sublistas, basta utilizar os dois-pontos, `:`, dentro dos colchetes, e indicar o ínicio, o fim e o passo da sublista, com as mesmas regras que usamos na função [`range()`](007-estruturas-repeticao.md#a-função-range):

``` python
alunos = [
    "abc", "def", "ghi", "jkl",
    "mno", "pqr", "stu", "vwx"
]

# sintaxe
# alunos[start:stop:step] -> o step é opcional
print(alunos[1:4])  # ["def", "ghi", "jkl"]
print(alunos[0:5:2]) # ["abc", "ghi", "mno"]

# omitir o primeiro número faz com que devolva desde o início da lista
print(alunos[:3])  # ["abc", "def", "ghi"]

# omitir o segundo número faz com que vá até o final da lista
print(alunos[6:])  # ["stu", "vwx"]

# use um step negativo para inverter a ordem da string
print(alunos[::-1])  # ["vwx", "stu", ..., "def", "abc"]
```

### Operações com listas

Um dos recursos mais poderosos em listas é a possibilidade de utilizá-las em operações, possibilitando inclui-las em estruturas de seleção e/ou de repetição. A documentação sobre essas operações pode ser encontrada na [documentação oficial](https://docs.python.org/pt-br/3/library/stdtypes.html#common-sequence-operations), e abaixo são indicados alguns exemplos:

``` python
# verifica se um determinado valor é igual a um dos elementos de uma lista
if "victor" in alunos:
    print("aluno localizado!")

# percorre todos os elementos de uma lista
for nota in notas:
    print(nota)

# percorre os índices e os valores dos elementos de uma lista, simultaneamente
for indice, aluno in enumerate(alunos):
    print(indice + 1, aluno, sep="-")

# junta duas listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista = lista1 + lista2  # [1, 2, 3, 4, 5, 6]

# repete uma dada lista um número determinado de vezes
lista = 3 * lista1  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### Funções e métodos de listas

O número de funções e métodos disponíveis para manipular listas é enorme. Certamente não faz sentido abordar todas as possibilidades aqui, já que muitas são usadas em casos bem pontuais, ou com aplicações mais avançadas. No entanto, abaixo há uma série de funções e métodos úteis para manipular listas, juntamente com os links para a sua documentação:

* [`len()`](https://docs.python.org/pt-br/3/library/functions.html#len)
* [`list.append()`](https://docs.python.org/pt-br/3/library/stdtypes.html#mutable-sequence-types)
* [`list.insert()`](https://docs.python.org/pt-br/3/library/stdtypes.html#mutable-sequence-types)
* [`list.extend()`](https://docs.python.org/pt-br/3/library/stdtypes.html#mutable-sequence-types)
* [`list.pop()`](https://docs.python.org/pt-br/3/library/stdtypes.html#mutable-sequence-types)
* [`list.remove()`](https://docs.python.org/pt-br/3/library/stdtypes.html#mutable-sequence-types)
* [`list.index()`](https://docs.python.org/pt-br/3/library/stdtypes.html#common-sequence-operations)
* [`list.count()`](https://docs.python.org/pt-br/3/library/stdtypes.html#common-sequence-operations)
* [`min()`](https://docs.python.org/pt-br/3/library/functions.html#min)
* [`max()`](https://docs.python.org/pt-br/3/library/functions.html#max)
* [`sum()`](https://docs.python.org/pt-br/3/library/functions.html#sum)
* [`list.sort()`](https://docs.python.org/pt-br/3/library/stdtypes.html#list.sort)
* [`sorted()`](https://docs.python.org/pt-br/3/library/functions.html#sorted)

### Passagem por referência

Uma particularidade das listas e de outras estruturas de dados compostas é como as utilizamos como parâmetros em funções. Considere a seguinte função e uma possível chamada:

``` python
def insere_valor(valor, lista):
    lista.append(valor)

exemplo = [1, 2, 3, 4]
insere_valor(5, exemplo)
print(exemplo)  # [1, 2, 3, 4, 5]
```

Veja que a função `insere_valor` não possui um retorno, portanto ela devolveria `None`. No entanto, quando passamos uma lista (ou qualquer estrutura de dados composta) como um argumento de função, tanto este quanto a variável usada na chamada da função serão apontados para um mesmo endereço na memória pelo interpretador do Python. Ou seja, a alteração do argumento provoca uma alteração também na variável usada na chamada da função.

Veja que esse comportamento é diferente quando temos dados primitivos, como `int` ou `str`. Nesses casos, a variável usada na chamada da função não sofre alteração. Essa é uma distinção crítica a se fazer entre estruturas de dados compostas e dados primitivos. Um cenário análogo ocorre quando fazemos atribuição de listas para variáveis, como no exemplo abaixo:

``` python
a = []
b = a

a.append(1)
b.append(2)

print(a)  # [1, 2]
print(b)  # [1, 2]

a.pop()

print(b)  # [1]
```

Veja que, quando alteramos `a`, a variável `b` também é afetada, e vice-versa, pois temos uma atribuição de igualdade na segunda linha do exemplo. Para evitarmos esse efeito, podemos utilizar o método `.copy()`, como no exemplo abaixo:

``` python
a = []
b = a.copy()

a.append(1)

print(b)  # []
```

### Pilhas e filas

No desenvolvimento de software, temos duas aplicações particulares para listas, as **pilhas** e as **filas**. São estruturas mais simples, que possuem um custo computacional consideravelmente menor que o de listas usuais. Não é o objetivo aqui trazer em detalhes como essas duas estruturas funcionam, mas sim trazer uma visão geral para conhecimento da turma. Certamente essas duas estruturas serão abordadas com mais detalhes na disciplina de Estruturas de Dados.

Em Python, não temos um ganho real de eficiência no uso de pilhas ou filas, quando comparado com listas. No entanto, no ponto de vista de design das soluções, adotar pilhas e filas pode simplificar muito o entendimento de como os problemas estão sendo resolvidos.

#### Pilhas

Pilhas, ou _stacks_, são estruturas de dados do tipo **LIFO**, ou _last in, fist out_. Nesse tipo de estrutura, o último elemento a ser inserido é sempre o primeiro a ser removido. Dessa forma, uma pilha permite acesso a apenas o último elemento inserido. Para processar o último item inserido, deve-se primeiro remover o último.

Uma aplicação direta do uso de pilhas é a funcionalidade de desfazer ou refazer uma ação em um editor de texto. Sempre que usamos o ctrl+z para desfazer uma ação, a ação selecionada é a última realizada.

Em Python, uma implementação bem simples de funções básicas de pilhas (inserir e remover elementos) pode ser descrita abaixo:

``` python
def insere_pilha(valor, pilha):
    """Insere valor em uma pilha."""
    pilha.append(valor)

def remove_pilha(pilha):
    """Remove o último valor da pilha."""
    return pilha.pop()
```

Veja que essa é realmente uma solução simplificada. Idealmente, quando estamos trabalhando com estruturas de dados mais sofisticadas em Python, costumamos utilizar conceitos como Orientação a Objetos, que ainda não discutimos neste curso.

#### Filas

Filas, ou _queues_, são estruturas de dados do tipo **FIFO**, ou _first in, first out_. Como em uma fila de banco, o primeiro elemento a ser adicionado à fila é sempre o primeiro elemento a ser removido. Filas são usadas, por exemplo, no controle de documentos para impressão, ou na criação de _buffers_ de informações entre diferentes dispositivos.

Em Python, uma implementação bem simples de funções básicas de pilhas (inserir e remover elementos) pode ser descrita abaixo:

``` python
def insere_fila(valor, fila):
    """Insere valor em uma fila."""
    fila.append(valor)

def remove_fila(fila):
    """Remove o primeiro valor da fila."""
    if fila:
        return fila.pop(0)
```

### Compreensão de listas (_list comprehension_)

Uma forma bem elegante de se criar listas em Python (dizemos que é uma solução _pythonica_) é usando o conceito de [compreensões de listas](https://docs.python.org/pt-br/3/tutorial/datastructures.html#list-comprehensions), ou _list comprehension_. Essa é uma notação concisa para construção de listas e outros dados iteráveis (como tuplas, conjuntos e dicionários, que veremos logo adiante). Nesse tipo de notação, inserimos a regra de formação da lista dentro dos colchetes, utilizando estruturas de repetição e de seleção caso necessário.

Considere, por exemplo, uma lista de números pares entre 0 e 1000:

``` python
# solução usual
pares = []

for num in range(501):
    pares.append(2 * num)

# solução pythonica
pares = [2 * num for num in range(501)]
```

Ambas as soluções apresentadas acima resultam em uma lista contendo todos os pares entre 0 e 1000. No entanto, a segunda é apresentada de forma direta e legível, em apenas uma linha. Podemos incluir também estruturas de seleção, caso necessário. Considere que, além do número ser par, ele precisa ser múltiplo de 6:

``` python
numeros = [2 * num for num in range(501) if not num % 3]
```

A única preocupação que temos com compreensões de lista é em não tornar sua leitura um desafio para os programadores. O caso abaixo, por exemplo, chega em um limite para o entendimento do que está sendo feito:

``` python
matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

lista = [num for elem in matriz for num in elem]
```

A compreensão de lista acima vai "achatar" uma lista de listas. Começamos lendo pelo primeiro `for` e logo depois concatenamos com o segundo `for`. Uma adaptação mais clara seria a seguinte:

``` python
lista = []

for elem in matriz:
    for num in elem:
        lista.append(num)
```

Um ponto importante no desenvolvimento de software é que o código precisa ser legível para qualquer um, e não apenas para aqueles que possuem um profundo conhecimento da linguagem. "Simples é melhor que complexo", como diz o [zen do Python](https://peps.python.org/pep-0020/)!

## Tuplas

[Tuplas](https://docs.python.org/pt-br/3/tutorial/datastructures.html#tuples-and-sequences) são casos particulares de listas, em que não podemos alterar seus elementos ou o seu tamanho _a posteriori_. Sendo assim, tuplas são consideradas **imutáveis**. Representamos tuplas com parênteses (`()`):

``` python
tupla = (1, 2, 3)

print(tupla[1]) # 2
print(tupla[:2]) # (1, 2)
# tupla.append(4) -> vai subir uma exceção!
```

O uso mais comum de tuplas é quando queremos que uma função retorne informações associadas entre si, que não devem ser modificadas por quem chamou a função. Podemos ver no exemplo abaixo, onde temos uma função que localiza a informações de nome e nota de um aluno:

``` python
matriculas = [1, 2, 3, 4, 5, 6]
nomes = ["a", "b", "c", "d", "e", "f"]
notas = [5.5, 7.8, 4.3, 9.9, 6.7, 8.8]

def localiza_info_aluno(matricula_procurada):
    """Retorna as informações de um aluno."""
    for indice, matricula in enumerate(matriculas):
        if matricula == matricula_procurada:
            return (matricula, nomes[indice], notas[indice])

print(localiza_info_aluno(3)) # (3, "c", 4.3)
```

Nesse caso, não queremos que qualquer instrução que tenha chamado `localiza_info_aluno()` modifique o resultado do retorno. Sendo assim, adotamos uma tupla no lugar.

Com exceção de funções e métodos que alterem o conteúdo ou o tamanho das tuplas, podemos usar qualquer funcionalidade prevista para listas, incluindo compreensões.

## Conjuntos

[Conjuntos](https://docs.python.org/pt-br/3/tutorial/datastructures.html#sets) são outro caso particular de listas. Eles são coleções desordenadas de elementos, e não possuem elementos repetidos. Para representar conjuntos, utilizamos chaves ou a função `set()`:

``` python
frutas = {"laranja", "pera", "mamão", "abacaxi", "mamão", "laranja"}
print(frutas) # {"laranja", "pera", "mamão", "abacaxi"}

letras = set("palavra")
print(letras) # {"p", "a", "l", "v", "r"}
```

Conjuntos, assim como tuplas, são imutáveis. Se for necessário criar um conjunto vazio, deve-se utilizar `set()`, e não `{}`. Esse último cria um dicionário vazio, que veremos logo a seguir.

## Dicionários

A última estrutura que veremos por enquanto neste curso é o [dicionário](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries). Enquanto os elementos de uma lista são indexados através de números inteiros, os dicionários são indexados através de **chaves**, que podem ser qualquer tipo de dado imutável, como strings, inteiros ou mesmo tuplas (o mais comum é usarmos strings, no entanto).

Dicionários, assim como conjuntos, também são delimitados por chaves, `{}`. A representação das chaves e dos valores é feita através de dois pontos (`:`), como no exemplo abaixo:

``` python
# dic = {chave: valor}
aluno = {
    "nome": "123 de oliveira 4",
    "matrícula": 12345,
    "data de nascimento": "11/11/2000",
    "notas": {
        "ap1": 6.7,
        "ap2": 7.7,
        "ac": 4.5
    }
}
```

Para visualizar um valor dentro do dicionário, utilizam-se os colchetes como em listas (cuidado para passar apenas chaves existentes!):

``` python
print(aluno["nome"])
print(aluno["notas"]["ap2"])
```

Assim como em listas, podemos usar o operador `in` para verificar pertencimento de dados dentro de dicionários, bem como para iterar pelos seus elementos. Usamos também os métodos `.keys()`, `.values()` e `.items()` para visualizar as chaves de um dicionário, seus valores ou ambos.

``` python
pauta = {
    # chave: valor
    "a": 4.0,
    "b": 5.5,
    "c": 9.2,
    "d": 8.7,
    "e": 6.6
}

print(pauta)
print(pauta.keys())
print(pauta.values())

if "h" in pauta:
    print(pauta["h"])

# iterar pelas chaves -> o uso do .keys() é dispensável
for aluno in pauta:
    print(aluno)

# iterar pelos valores
for nota in pauta.values():
    print(nota)

# iterar pelo dicionário inteiro
for aluno, nota in pauta.items():
    print(aluno, nota)
```

## Exercícios resolvidos

Para a resolução dos exercícios, consulte a página de [gabaritos](./000-gabaritos_exercicios.md).

1. Elabore uma função `le_numeros()`, que fica lendo números inseridos pelo usuário até que seja pressionado a tecla ENTER, e adiciona esses números em uma lista, que é retornada.
2. Elabore uma função `remove_elem_inplace()`, que recebe como atributos um determinado elemento `elem` e uma lista `lista_a_remover`, e remove todas as entradas de `elem` em `lista_a_remover`.
3. Monte uma função `remove_elem()`, que recebe como atributos um determinado elemento `elem` e uma lista `lista_a_remover`, e retorna uma nova lista igual a `lista_a_remover`, a menos dos elementos iguais a `elem`.
4. Implemente a função `procura_nota()`, que recebe um determinado aluno `nome_procurado`, uma lista de alunos `nomes` e uma lista de notas `numeros`, e retorna uma tupla contendo o nome do aluno e sua nota. A função retorna `-1.0` e uma mensagem que o aluno não foi encontrado caso `nome_procurado` não esteja em `nomes`.

Os próximos exercícios fazem parte de um mesmo problema:

5. Usando a função `chr(i)`, que busca o caractere que possui código `i` na tabela ASCII, e sabendo que as letras minúsculas do alfabeto possuem códigos entre 97 e 122 (inclusive), monte uma função `alfabeto()` que retorna uma lista com todas as letras do alfabeto. Utilize compreensão de listas para resolver esse exercício.
6. Usando o módulo `random`, a função `random.shuffle(lista)` e a função `alfabeto()` criada no exercício anterior, que embaralha os valores de `lista`, implemente uma função `gera_chave()`, que retorna uma chave criptográfica gerada aleatoriamente. Uma chave criptográfica, nesse caso, é um dicionário que possui como chaves todas as letras do alfabeto, e como valores letras definidas aleatoriamente.
7. Implemente uma função `cripto()`, que recebe uma mensagem em string e uma chave criptográfica (como a criada no exercício anterior), e retorna a mensagem cifrada.
8. Implemente uma função `decripto()`, que recebe uma mensagem em string e uma chave criptográfica (como a criada no exercício 6), e retorna a mensagem descriptografada.
9. Implemente uma função `main()`, que gera uma chave criptográfica e lê mensagens inseridas pelo usuário e uma opção (se deseja encriptar ou decriptar uma mensagem), e exibe na tela a mensagem resultante.

## Exercícios complementares

1. Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
2. Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
3. Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor par e os números ímpares no vetor impar. Imprima os três vetores.
4. Faça um programa que leia um vetor com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
5. Faça um programa que leia as idades e alturas de N alunos do ensino fundamental (N é um número fornecido pelo usuário) e determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
6. Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

    ```
    8  3  4
    1  5  9
    6  7  2
    ```

7. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

    * Mostre a quantidade de valores que foram lidos;
    * Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    * Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    * Calcule e mostre a soma dos valores;
    * Calcule e mostre a média dos valores;
    * Calcule e mostre a quantidade de valores acima da média calculada;
    * Calcule e mostre a quantidade de valores abaixo de sete;
    * Encerre o programa com uma mensagem.  

8. Construa uma função que receba uma data no formato `DD/MM/AAAA` e devolva uma string no formato `D de mesPorExtenso de AAAA`. Opcionalmente, valide a data e retorne `None` caso a data seja inválida. Utilize um dicionário para armazenar a equivalência do número do mês para o nome por extenso.

## Leitura complementar

* Material online:
    * [Este artigo](https://betterprogramming.pub/20-things-to-know-to-master-lists-in-python-e3417f4c28cf) com 20 dicas para dominar listas em Python.
