# Pedido da AP1

Para a AP1, cada time deve implementar **ambos** os projetos indicados abaixo, em um único arquivo.

## Projeto 1 - Simulador de dados

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

## Projeto 2 - Calculadora

Implemente uma calculadora em Python, com instruções por linha de comando (CLI). A calculadora deve possuir as seguintes funcionalidades:

* Deve ficar em um _loop_ infinito até o momento em que o usuário inserir um texto vazio (apertar ENTER);
* Deve iniciar a calculadora no valor zero;
* Dentro do loop, executar as seguintes etapas:
  * Ler um número;
  * Ler uma operação (soma, subtração, multiplicação ou divisão);
  * Ler outro número;
  * Exibir o resultado;
  * Pedir uma outra operação para continuar a conta ou "X" para limpar a calculadora;
  * Se o usuário limpar a calculadora, ela deve recomeçar do zero.

A calculadora deve exibir as informações na tela conforme o usuário for inserindo os dados. Caso o usuário insira algum valor inválido (p.ex., um texto), o programa deve alertar e realizar a pergunta novamente.

## Avaliação

Os projetos serão avaliados de acordo com os seguintes critérios:

* Qualidade de escrita do código: variáveis foram bem nomeadas, código está de acordo com os padrões discutidos em sala;
* Qualidade dos algoritmos: o código não apresenta redundâncias ou trechos não solicitados. O algoritmo está completo e atende a todos os pedidos nos requisitos do projeto;
* Apresentação do projeto: o grupo será questionado com relação à solução no dia seguinte ao da entrega do projeto;
* Testes realizados pelo professor não apresentam falhas, ou seja, todas as análises necessárias foram feitas e o código exibe na tela **exatamente** como nos exemplos de execução.

## Informações gerais:

* Prazo: 26/04/2023
* Grupos de no máximo 3 pessoas
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

* Utilize a função `str.lower()` para converter todos os caracteres para caixa baixa, e evitar comparações de strings contendo letras de _casing_ diferente. Exemplo de uso:

    ``` python
    "Água".lower()  # retorna "água"
    input("Insira um valor: ").lower()  # converte o resultado de input()
    ```

* Utilize o [modelo](./modelo_ap1.txt) de código disponível para iniciar o projeto 1.
