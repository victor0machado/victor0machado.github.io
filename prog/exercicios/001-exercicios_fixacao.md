# Exercícios de fixação

Neste material são apresentados alguns exercícios conceituais, voltados à fixação dos conhecimentos da linguagem Python e dos fundamentos de programação. O gabarito para os exercícios se [encontra aqui](000-gabaritos_exercicios.md).

1. Escolha a opção adequada ao tentar rodar o código a seguir:

    ``` python
    if 5 > 2
        print("True!")
    ```

    - a) O código roda, exibindo "True!" na tela.
    - b) O código possui um erro de tipo, já que `True` deveria ser um booleano e não uma string.
    - c) O código possui um erro de sintaxe, já que após a instrução `if` deve ser incluído `:`.
    - d) O código possui um erro de valor, já que não é possível colocar valores no teste lógico da instrução `if`.

2. Considere o seguinte fragmento de código, escrito em Python. Após a execução de todos os comandos, qual seria o resultado apresentado pelo comando `print(a)`?

    ``` python
    a = 3
    b = 4 + a * 2 - 2
    a = b % 5
    ```

    - a) 0.
    - b) 1.
    - c) 2.
    - d) 3.

3. Considere o seguinte fragmento de código, escrito em Python. Após a execução de todos os comandos, qual seria o resultado apresentado pelo comando `print(b)`?

    ``` python
    def foo(a):
        return a + a + a

    b = 1
    foo(b)
    foo(b)
    foo(b)
    ```

    - a) 0.
    - b) 1.
    - c) 3.
    - d) 9.

4. Considere o seguinte fragmento de código, escrito em Python. Qual o valor impresso ao executarmos o programa?

    ``` python
    def dobra(y):
        x = y + y
        return x

    x = 5
    dobra(x)
    dobra(x)
    print(x)
    ```

    - a) 5.
    - b) 10.
    - c) 15.
    - d) 20.

5. Considere o seguinte fragmento de código, escrito em Python. Qual o valor impresso ao executarmos o programa?

    ``` python
    def dobra(y):
        global x
        x = y + y
        return x

    x = 5
    dobra(x)
    dobra(x)
    print(x)
    ```

    - a) 5.
    - b) 10.
    - c) 15.
    - d) 20.

6. Qual dos tipos abaixo NÃO é considerado um tipo primitivo em Python?

    - a) int.
    - b) double.
    - c) bool.
    - d) str.

7. Qual das características abaixo é indicada para referenciar a linguagem Python?

    - a) Ela é uma linguagem multiparadigma.
    - b) Ela possui tipagem estática, ou seja, não é possível alterar os tipos de variáveis.
    - c) Python é uma linguagem compilada.
    - d) Python não pode ser executada em ambientes Mac.

8. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa?

    ``` python
    i = 3
    j = "Nome"

    print(i + j)
    ```

    - a) O código roda e é exibido o texto `3Nome`.
    - b) O código roda e é exibido o texto `3 Nome`.
    - c) Há um erro de sintaxe, pois não é possível concatenar inteiros e strings.
    - d) Há um erro de tipo, pois não é possível concatenar inteiros e strings.

9. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa?

    ``` python
    i = 3
    j = "Nome"

    print(i * j)
    ```

    - a) O código roda e é exibido o texto `3Nome`.
    - b) O código roda e é exibido o texto `NomeNomeNome`.
    - c) Há um erro de sintaxe, pois não é possível concatenar inteiros e strings.
    - d) Há um erro de tipo, pois não é possível concatenar inteiros e strings.

10. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa?

    ``` python
    x = 10
    if x > 7:
        print("Valor maior que 7")
    else x < 2:
        print("Valor menor que 2")
    ```

    - a) O código roda e é exibido o texto `Valor maior que 7`.
    - b) O código roda e é exibido o texto `Valor menor que 2`.
    - c) O código não roda porque a instrução `else` não pode ser associada a um teste lógico.
    - d) O código roda e não exibe nada.

11. Considere o seguinte fragmento de código, escrito em Python. O que é impresso na tela ao executarmos o programa?

    ``` python
    x = 5
    while x < 10:
        print(x)
        x += 2
    ```

    - a) O código roda e são exibidos os valores `5 7 9`.
    - b) O código roda e são exibidos os valores `7 9 11`.
    - c) O código roda e são exibidos os valores `5 7`.
    - d) O código roda e não exibe nada.

12. Considere o seguinte fragmento de código, escrito em Python. O que é impresso na tela ao executarmos o programa?

    ``` python
    for i in range(1, 4, -1):
        print(i)
    ```

    - a) O código roda e são exibidos os valores `1 2 3`.
    - b) O código roda e são exibidos os valores `1 2 3 4`.
    - c) O código roda e são exibidos os valores `4 3 2`.
    - d) O código roda e não exibe nada.

13. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa?

    ``` python
    x = 10
    y = False
    z = "3"

    print(x or y or z)
    ```

    - a) O código não roda, pois não é possível realizar operações booleanas com valores não booleanos.
    - b) O código roda e é exibido o valor `True`.
    - c) O código roda e é exibido o valor `10`.
    - d) O código roda e é exibido o valor `"3"`.
