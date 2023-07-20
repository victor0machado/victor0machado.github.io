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

14. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa?

    ``` python
    input("Informe o seu nome: ")
    print("Seu nome é", nome)
    ```

    - a) O código sobe um erro de nome na segunda linha, pois a variável `nome` não foi definida.
    - b) O código pede para que o usuário informe o nome e exibe `Seu nome é None` logo em seguida.
    - c) O código pede para que o usuário informe o nome e exibe esse nome logo em seguida.
    - d) O código sobre um erro de tipo na segunda linha, pois a string e a variável `nome` são de tipos diferentes.

15. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa?

    ``` python
    print("Boa", "noite", sep="-", end="!")
    ```

    - a) O código roda e é exibido o texto `Boa noite`.
    - b) O código roda e é exibido o texto `Boa-noite!`, com a inclusão de uma quebra de linha ao final.
    - c) O código roda e é exibido o texto `Boa-noite!`, sem haver uma quebra de linha ao final.
    - d) O código não roda, o parâmetro `end` não é possível dentro da função `print()`.

16. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa?

    ``` python
    def func(x):
        if x == "a":
            return x
            print("Valor recebido:", x)

    print(func("a"))
    print(func("b"))
    ```

    - a) Ao rodar, o código sobe um erro de sintaxe, já que não é possível colocar uma instrução `print()` depois de um `return`.
    - b) O código roda, e são exibidos na tela os valores `a` e em seguida `b`.
    - c) O código roda, e são exibidos na tela os valores `a` e em seguida `None`.
    - d) O código roda, e são exibidos na tela os valores `Valor recebido: a` e em seguida `None`.

17. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa?

    ``` python
    for i in range(1, 10):
        if i % 5 == 0:
            continue
        elif i % 7 == 0:
            break
        print(i)
    ```

    - a) `1 2 3 4 6`
    - b) `1 2 3 4 6 7`
    - c) `1 2 3 4 5 6 7 8 9`
    - d) `1 2 3 4 5 6`

18. Considere o seguinte fragmento de código, escrito em Python. Supondo que o usuário respondesse ao input com a mensagem `2`, qual precisaria ser a linha seguinte para que o programa exibisse na tela a mensagem `O número exibido é 2.0`?

    ``` python
    valor = input("Informe um número: ")
    ```

    - a) `print("O número exibido é" + float(valor))`
    - b) `print("O número exibido é", int(valor))`
    - c) `print("O número exibido é", float(valor))`
    - d) `print("O número exibido é", valor)`

19. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa?

    ``` python
    print(8.5 / 2 // 2)
    ```

    - a) `2`
    - b) `2.125`
    - c) Sobe um erro, pois não é possível realizar essas duas operações em sequência.
    - d) `2.0`

20. Considere o seguinte fragmento de código, escrito em Python. O que é exibido na tela após executar o programa?

    ``` python
    x = 2
    y = 10

    if x >= 0:
        print("a")
    elif y > 0:
        print("b")
    elif x == 2 and y == 10:
        print("c")
    else:
        print("d")
    ```

    - a) `d`
    - b) `a`
    - c) `b`
    - d) `c`

21. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa e passarmos o texto `10` no input?

    ``` python
    valor = input("Informe um valor: ")
    print(not int(valor) % 2)
    ```

    - a) O código não roda, surge um erro de valor ao tentar converter o texto em inteiro.
    - b) O código roda e é exibido na tela `True`.
    - c) O código roda e é exibido na tela `true`.
    - d) O código roda e é exibido na tela `0`.

22. Considere o seguinte fragmento de código, escrito em Python. Quais valores são exibidos na tela após a execução do código?

    ``` python
    for i in range(2, 10, 2):
        print(i)
    ```

    - a) `2 4 6 8 10`
    - b) `4 6 8 10`
    - c) `2 4 6 8`
    - d) `4 6 8`

23. Considere o seguinte fragmento de código, escrito em Python. O que acontece ao executarmos o programa?

    ``` python
    def func(x=2, y):
        print(x, y)

    func(4)
    ```

    - a) `4 2`
    - b) `4`
    - c) O código sobe um erro de valor, pois não foi passado o parâmetro `y`.
    - d) O código sobe um erro de sintaxe, pois um parâmetro chave foi definido antes do parâmetro posicional.

24. Considere o seguinte fragmento de código, escrito em Python. Quais valores são exibidos na tela após a execução do programa?

    ``` python
    def func(x, y=2):
        print(x, y)

    func(4)
    ```

    - a) `4`
    - b) `4 2`
    - c) O código sobe um erro de valor, pois não foi passado o parâmetro `y`.
    - d) `4 None`

25. Considere o seguinte fragmento de código, escrito em Python. Quais valores são exibidos na tela após a execução?

    ``` python
    x = 10
    x += 2
    print(x)
    x -= 10
    print(x)
    ```

    - a) O código sobe um erro pois a operação não é válida.
    - b) `12 2`
    - c) `10 10`
    - d) `2 -10`

26. Considere o seguinte fragmento de código, escrito em Python. Qual valor é exibido na tela após a execução do programa?

    ``` python
    print(3.5 % 2)
    ```

    - a) `2`
    - b) Sobe um erro, pois não é possível realizar operação de módulo com valores não inteiros.
    - c) `1.5`
    - d) `1`

27. Considere o seguinte fragmento de código, escrito em Python. Qual valor é exibido na tela após a execução do programa?

    ``` python
    x = 2
    y = 10
    z = -2

    print(x % (3 + y) * x - z ** 2)
    ```

    - a) `18`
    - b) `26`
    - c) `0`
    - d) `36`

