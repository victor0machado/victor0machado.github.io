# Pedido da AP1

Para a AP1, cada time deve implementar **ambos** os projetos indicados abaixo, em um único arquivo.

## Projeto 1 - Jogo termo

Implemente uma versão rudimentar do jogo [termo](https://term.ooo/). Neste jogo, você possui seis tentativas para acertar uma palavra aleatória de 5 letras. Após inserir uma palavra, você recebe um feedback sobre cada letra, podendo ser de três tipos:

* Letra está na palavra, e no lugar correto;
* Letra está na palavra, mas no lugar incorreto;
* Letra não está na palavra.

Para podermos jogar no console, considere o caractere `+` para o primeiro feedback, o caractere `-` ou um espaço em branco para o caso da letra não estar na palavra. Para simplificar as análises, considere que nenhuma palavra possui caracteres repetidos (o que exclui "massa", "casal" e "sonho", por exemplo). Considere, também, que nenhuma palavra possui acento ou caracteres especiais.

Cada tentativa deve exibir o número da tentativa, seguido pelo máximo de tentativas possível. Por exemplo, `(1/6)`, `(2/6)`, etc.

Para este projeto, não é necessário analisar o conteúdo inserido pelo usuário. Assuma que o valor inserido é uma palavra com cinco letras distintas.

### Exemplos de execução

#### Caso 1

* Ocorre acerto durante as tentativas:

```
(1/6) Informe uma palavra: sutil
sutil
-   -
(2/6) Informe uma palavra: lapso
Acertou!!!
```

#### Caso 2

* Palavra não é acertada:

```
(1/6) Informe uma palavra: nobre
nobre
-   -
(2/6) Informe uma palavra: termo
termo
++
(3/6) Informe uma palavra: algoz
algoz
-   +
(4/6) Informe uma palavra: afeto
afeto
- --
(5/6) Informe uma palavra: plena
plena
  ---
(6/6) Informe uma palavra: pesar
pesar
 + +
Perdeu! Palavra correta: tenaz
```

## Projeto 2 - Simulador de dados

O time deve desenvolver um simulador de rolagem de dados. Primeiramente, o programa deve pedir o tamanho do dado que deseja rolar, podendo ser qualquer valor inteiro maior que zero (3, 6, 10, etc.). O programa deve fazer os seguintes tratamentos com relação à informação coletada:

* Se o usuário não passar um valor numérico maior que zero, repita o pedido até passar um valor válido;
* Se o usuário passar uma string vazia, encerre o programa.

Em seguida, o programa deve pedir quantos dados o usuário deseja rolar. Faça as mesmas validações do pedido anterior, porém considere que caso o valor passado seja uma string vazia, adotar que será rolado apenas um dado.

Por último, o programa deve gerar valores aleatórios para cada dado, e imprimi-los lado a lado na tela.

Se o tamanho do dado for válido, porém o número de dados não for, continue pedindo apenas pelo número de dados.

### Exemplos de execução

#### Caso 1

* Usuário passa uma string vazia na primeira pergunta.

```
Forneça o tamanho do dado que será rolado (ENTER para sair):
```

#### Caso 2

* Usuário passa uma string não numérica na primeira pergunta;
* Usuário passa um número maior que zero na primeira pergunta;
* Usuário passa um número maior que zero na segunda pergunta.

```
Forneça o tamanho do dado que será rolado (ENTER para sair): abc
A informação passada não é válida!
Forneça o tamanho do dado que será rolado (ENTER para sair): 10
Forneça o número de dados que serão rolados (em branco == 1): 4
Lançamento n. 1 - 10
Lançamento n. 2 - 10
Lançamento n. 3 - 7
Lançamento n. 4 - 7

4 dado(s) de 10 lados:
10 10 7 7
```

#### Caso 3

* Usuário passa zero na primeira pergunta;
* Usuário passa um número maior que zero na primeira pergunta;
* Usuário passa um número maior que zero na segunda pergunta.

```
Forneça o tamanho do dado que será rolado (ENTER para sair): 0
O número passado deve ser maior que zero!
Forneça o tamanho do dado que será rolado (ENTER para sair): 10
Forneça o número de dados que serão rolados (em branco == 1): 4
Lançamento n. 1 - 4
Lançamento n. 2 - 2
Lançamento n. 3 - 2
Lançamento n. 4 - 2

4 dado(s) de 10 lados:
4 2 2 2
```

#### Caso 4

* Usuário passa um número maior que zero na primeira pergunta;
* Usuário passa uma string não numérica na segunda pergunta;
* Usuário passa zero na segunda pergunta;
* Usuário passa um número maior que zero na segunda pergunta.

```
Forneça o tamanho do dado que será rolado (ENTER para sair): 10
Forneça o número de dados que serão rolados (em branco == 1): abc
A informação passada não é válida!
Forneça o número de dados que serão rolados (em branco == 1): 0
O número passado deve ser maior que zero!
Forneça o número de dados que serão rolados (em branco == 1): 4
Lançamento n. 1 - 9
Lançamento n. 2 - 7
Lançamento n. 3 - 5
Lançamento n. 4 - 4

4 dado(s) de 10 lados:
9 7 5 4
```

#### Caso 5

* Usuário passa um número maior que zero na primeira pergunta;
* Usuário passa uma string vazia na segunda pergunta.

```
Forneça o tamanho do dado que será rolado (ENTER para sair): 10
Forneça o número de dados que serão rolados (em branco == 1):
Lançamento n. 1 - 10

1 dado(s) de 10 lados:
10
```

## Avaliação

Os projetos serão avaliados de acordo com os seguintes critérios:

* Qualidade de escrita do código: variáveis foram bem nomeadas, código está de acordo com os padrões discutidos em sala;
* Qualidade dos algoritmos: o código não apresenta redundâncias ou trechos não solicitados. O algoritmo está completo e atende a todos os pedidos nos requisitos do projeto;
* Apresentação do projeto: o grupo será questionado com relação à solução no dia da entrega do projeto;
* Testes realizados pelo professor não apresentam falhas, ou seja, todas as análises necessárias foram feitas e o código exibe na tela **exatamente** como nos exemplos de execução.

## Informações gerais:

* Prazo: 25/04/2022
* Grupos de no mínimo 3 e no máximo 4 pessoas
* Subir na Sala de Aula Virtual o código salvo no formato .txt
* Atentar para o formato da apresentação dos resultados! Eles devem estar exatamente como nos exemplos indicados acima.

## Dicas

* Use a função `str.isnumeric()` para garantir que a string é numérica antes de convertê-la. Exemplos de usos da função:

    ``` python
    '2'.isnumeric() # Retorna True
    'abc'.isnumeric() # Retorna False
    '1.1'.isnumeric() # Retorna False
    '1a'.isnumeric() # Retorna False
    ''.isnumeric() # Retorna False
    dado = "123"
    dado.isnumeric() # Retorna True

    dado = "abc"
    dado.isnumeric() # Retorna False
    ```

* Use a função `random.randint(a, b)` para gerar um `N` inteiro, com `a <= N <= b`. Exemplo de uso:

    ``` python
    >>> import random
    >>> random.randint(1, 8)
    4
    ```

* Use a função `random.choice(a)` para escolher um elemento da lista `a`:

    ``` python
    >>> import random
    >>> random.randint(1, 8)
    4
    ```

* Lembre-se do uso da função `enumerate()` para percorrer, ao mesmo tempo, o índice e o valor em uma lista;
* Utilize a função `str.lower()` para converter todos os caracteres para caixa baixa, e evitar comparações de strings contendo letras de _casing_ diferente. Exemplo de uso:

    ``` python
    "Água".lower()  # retorna "água"
    input("Insira um valor: ").lower()  # converte o resultado de input()
    ```

* Utilize o modelo de código disponível para iniciar seu projeto.
