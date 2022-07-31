# Gabaritos dos exercícios resolvidos

Retornar para [lista de exercícios](./exercicios.md)

### Índice

* [Funções](#nota-de-aula-05-funções)
* [Estruturas de seleção](#nota-de-aula-06-estruturas-de-seleção)
* [Estruturas de repetição](#nota-de-aula-07-estruturas-de-repetição)
* [Estruturas de dados](#nota-de-aula-08-estruturas-de-dados)
* [Strings](#nota-de-aula-09-strings)

## Funções

1. Faça uma função `media()`, que recebe os parâmetros posicionais `ap1`, `ap2` e `ac`, e retorne a média de avaliações, utilizando a fórmula `M = (AP1 + AP2) * 0.4 + AC * 0.2`.

    **SOLUÇÃO:**

    ``` python
    def media(ap1, ap2, ac):
        """Retorna uma média de avaliações."""
        return 0.4 * (ap1 + ap2) + 0.2 * ac
    ```

2. Faça uma função `m_para_cm()` que receba um comprimento em metros e converta para centímetros.

    **SOLUÇÃO:**

    ``` python
    def m_para_cm(comp_m):
        """Converte um comprimento em metros para centímetros."""
        return 100 * comp_m
    ```

3. Faça uma função que receba o raio de um círculo, calcule e retorne sua área. Considere pi como aproximadamente igual a 3.14.

    **SOLUÇÃO:**

    ``` python
    def area_circulo(raio):
        """Calcula a área de um círculo, dado o seu raio."""
        return 3.14 * raio * raio
    ```

4. Monte um conversor de temperatura, que recebe uma temperatura em graus Fahrenheit e devolva a temperatura em graus Celsius. A fórmula para conversão é `C / 5 = (F - 32) / 9`.

    **SOLUÇÃO:**

    ``` python
    def celsius_para_fahrenheit(temp_celsius):
        """Retorna uma temperatura em graus Fahrenheit."""
        return 9 * temp_celsius / 5 + 32
    ```

5. Desenvolva uma função que gera um relatório na tela do usuário. Essa função calcula o contracheque de uma pessoa. O salário é calculado como as horas trabalhadas no mês vezes o valor por hora. O salário líquido precisa ter descontado o IRPF (11%), INSS (8%, que pode variar entre pessoas) e sindicato (5%). O relatório precisa ter o formato indicado abaixo:

    ``` txt
    Salário por hora trabalhada: 10.5
    Número de horas trabalhadas no mês: 20
    ----------------------------------------
    Salário bruto: 210.0
    (-) Imposto de Renda: 23.1
    (-) INSS: 16.8
    (-) Sindicato: 10.5
    (=) Salário Líquido: 159.6
    ```

    **SOLUÇÃO:** Importante aqui atentar para o fato de que o percentual referente ao INSS varia de pessoa para pessoa, portanto é um caso claro de que o parâmetro deve ser considerado como chave.

    ``` python
    def contracheque(horas, valor_hora, tx_inss=0.08):
        """
        Monta um relatório contendo um contracheque.
        O salário é calculado como as horas trabalhadas no mês vezes o valor por hora.
        O salário líquido precisa ter descontado os seguintes valores:
        - IRPF: 11%
        - INSS: 8% (mas esse valor pode ser alterado)
        - Sindicato: 5%
        """
        salario_bruto = horas * valor_hora
        irpf = salario_bruto * 0.11
        inss = salario_bruto * tx_inss
        sind = salario_bruto * 0.05
        salario_liq = salario_bruto - irpf - inss - sind

        print("Salário por hora trabalhada:", valor_hora)
        print("Número de horas trabalhadas no mês:", horas)
        print("-" * 40)
        print("Salário bruto:", salario_bruto)
        print("(-) Imposto de Renda:", irpf)
        print("(-) INSS:", inss)
        print("(-) Sindicato:", sind)
        print("(=) Salário Líquido:", salario_liq)
    ```

## Estruturas de seleção

1. Elabore uma função `e_par`, que recebe um número e retorna `True` ou `False` conforme o número seja par ou não.

    **SOLUÇÃO:** Como sempre, em programação, temos mais de uma possível solução. Para este caso, em particular, o uso das instruções `if/else` não é necessário, uma vez que só queremos retornar o resultado da operação lógica `num % 2 == 0`.

    ``` python
    def e_par(num):
        """Retorna True se num for par, e False caso contrário."""
        if num % 2 == 0:
            return True
        else:
            return False
    ```

    ``` python
    def e_par_alt(num):
        """Retorna True se num for par, e False caso contrário."""
        return num % 2 == 0
    ```

2. Implemente um programa que receba dois números e retorne o maior deles.

    **SOLUÇÃO:** Novamente, vamos apresentar duas soluções possíveis. A primeira é a mais "tradicional":

    ``` python
    def maior(num1, num2):
        """
        Faça um programa que receba dois números e
        retorne o maior deles.
        """
        if num1 > num2:
            return num1

        return num2
    ```

    A solução abaixo é considerada mais _pythonica_, termo usado quando queremos destacar alguma característica específica à linguagem Python. Neste caso, estamos usando a representação de [ternários em Python](https://towardsdatascience.com/ternary-operators-in-python-49c685183c50), que torna a solução mais limpa.

    ``` python
    def maior_melhor(num1, num2):
        """
        Faça um programa que receba dois números e
        retorne o maior deles.
        """
        return num1 if num1 > num2 else num2
    ```

3. Crie uma função que receba um valor e retorne se ele é positivo ou negativo.

    **SOLUÇÃO:** Assim como no exercício anterior, também há a possibilidade de realizar a solução com ternários, que será deixada em aberto para o aluno.

    ``` python
    def e_positivo(num):
        """
        Faça um programa que receba um valor e
        retorne se o valor é positivo ou negativo.
        """
        if num > 0:
            return "positivo"

        return "negativo"
    ```

4. Faça um programa que verifique se uma letra é vogal ou consoante.

    **SOLUÇÃO:** Veremos ao longo do curso algumas estruturas que permitem soluções muito melhores ao problema. Por enquanto, vamos nos ater aos conceitos discutidos em sala. Veja que esse exercício também pode ser resolvido com ternários, ou até mesmo sem a estrutura `if/else`, como fizemos no primeiro exercício.

    ``` python
    def e_vogal(letra):
        """
        Faça um programa que verifique se uma letra digitada é vogal ou consoante.
        """
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            return True

        return False
    ```

5. Faça um programa que receba três notas, calcule sua média aritmética simples e apresente na tela uma das seguintes informações:

    * A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    * A mensagem "Reprovado", se a média for menor do que sete;
    * A mensagem "Aprovado com Distinção", se a média for igual a dez;
    * A mensagem "Nota inválida!" toda vez que for inserido um valor inválido.

    **SOLUÇÃO:** Temos aqui dois problemas a resolver: calcular a média de três notas e definir uma mensagem para uma dada média. Quando temos dois (ou mais) problemas para serem resolvidos, é boa prática dividir a nossa solução em funções independentes, que tenham uma única responsabilidade. Portanto, vamos resolver esses dois problemas:

    ``` python
    def calcula_media(nota1, nota2, nota3):
        """Retorna a média aritmética simples de três notas."""
        return (nota1 + nota2 + nota3) / 3
    ```

    ``` python
    def resultado(media):
        """Retorna o resultado de aproveitamento de uma média."""
        if media < 0 or media > 10:
            return "Nota inválida!"
        if media == 10:
            return "Aprovado com Distinção"
        if media >= 7:
            return "Aprovado"

        return "Reprovado"
    ```

    Por fim, para resolver o exercício proposto, precisamos de uma função que junte os resultados das funções anteriores. Essa função receberá as três notas passadas, calculará a média e exibirá na tela o retorno da função `resultado()`.

    ``` python
    def main(nota1, nota2, nota3):
        """
        Faça um programa para a leitura das três notas de um aluno.
        O programa deve calcular a média alcançada por aluno e apresentar:
        - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        - A mensagem "Reprovado", se a média for menor do que sete;
        - A mensagem "Aprovado com Distinção", se a média for igual a dez;
        - A mensagem "Nota inválida!" toda vez que for inserido um valor inválido.
        """
        media = calcula_media(nota1, nota2, nota3)
        print(resultado(media))
    ```

## Estruturas de repetição

1. Elaborar uma função `conta_pares(min, max)` para exibir todos os valores entre `min` e `max`, com um incremento de 2, separando-os com um hífen. Ex.: `2 – 4 – 6 – 8 – 10 – 12 – 14`.

    **SOLUÇÃO:** Abaixo duas soluções, uma usando `while` e uma usando `for`.

    ``` python
    def conta_pares(min, max):
        """Exibe números entre min e max, de 2 em 2."""
        while min < max:
            print(min, end=" - ")
            min += 2

        print(min)
    ```

    ``` python
    def conta_pares(min, max):
        """Exibe números entre min e max, de 2 em 2."""
        for num in range(min, max + 1, 2):
            if num + 2 > max:
              print(num)
            else:
              print(num, end=" - ")
    ```

2. Faça um programa que receba um nome de usuário e a sua senha, exiba uma mensagem de erro e retorne `False` caso os dois valores sejam iguais e retorne `True` caso sejam valores diferentes.

    **SOLUÇÃO:** Neste caso, estamos separando em duas funções, uma que pede os valores e processa a análise e outra que, de fato, analisa as informações. Como boa prática, sempre que for necessário utilizar leitura de dados, considere implementar em uma função separada da regra de análise, para um maior reaproveitamento de código futuro.

    ``` python
    def e_senha_valida(nome, senha):
        """Analisa se a senha é válida."""
        if nome == senha:
            print("Senha inválida!")
            return False

        return True

    def main():
        """Pede o nome de usuário e uma senha até que esta seja válida."""
        nome = input("Informe o seu nome: ")

        while True:
            senha = input("Informe a senha: ")
            if e_senha_valida(nome, senha):
              break
    ```

3. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    ```
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50
    ```

    **SOLUÇÃO:**

    ``` python
    def tabuada(num):
        """Gera a tabuada de num."""
        print("Tabuada de ", num, ":", sep="")
        for mult in range(1, 11):
            print(num, "X", mult, "=", num * mult)
    ```

4. Faça um programa que calcule o fatorial de um número inteiro positivo fornecido pelo usuário. Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120.

    **SOLUÇÃO:**

    ``` python
    def fatorial(num):
        """Retorna o fatorial de num."""
        fat = 1
        for mult in range(1, num + 1):
            fat *= mult

        return fat
    ```

5. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

    **SOLUÇÃO:**

    ``` python
    def populacao(pop_a, pop_b):
        """
        Retorna o número de anos para que a população do país A ultrapasse a de B.
        """
        num_anos = 0
        while pop_a < pop_b:
            pop_a *= 1.03
            pop_b *= 1.015
            num_anos += 1

        return num_anos
    ```

## Estruturas de dados

1. Elabore uma função `le_numeros()`, que fica lendo números inseridos pelo usuário até que seja pressionado a tecla ENTER, e adiciona esses números em uma lista, que é retornada.

    **SOLUÇÃO:**

    ``` python
    def le_numeros():
        """
        Monta uma função que fica lendo números do usuário, até que seja
        pressionado ENTER, e adiciona os números na lista numeros.
        """
        numeros = []
        while True:
            valor = input("Informe um número: ")
            if valor == "":
                return numeros

            numeros.append(float(valor))
    ```

2. Elabore uma função `remove_elem_inplace()`, que recebe como atributos um determinado elemento `elem` e uma lista `lista_a_remover`, e remove todas as entradas de `elem` em `lista_a_remover`.

    **SOLUÇÃO:**

    ``` python
    def remove_elem_inplace(elem, lista_a_remover):
        """
        Remove todas as referências de elem em lista_a_remover.
        """
        while elem in lista_a_remover:
            lista_a_remover.remove(elem)
    ```

3. Monte uma função `remove_elem()`, que recebe como atributos um determinado elemento `elem` e uma lista `lista_a_remover`, e retorna uma nova lista igual a `lista_a_remover`, a menos dos elementos iguais a `elem`.

    **SOLUÇÃO:**

    ``` python
    def remove_elem(elem, lista_a_remover):
        """
        Remove todas as referências de elem em lista_a_remover,
        e retorna para uma nova lista.
        """
        lista_limpa = []

        for item in lista_a_remover:
            if item != elem:
                lista_limpa.append(item)

        return lista_limpa
    ```

4. Implemente a função `procura_nota()`, que recebe um determinado aluno `nome_procurado`, uma lista de alunos `nomes` e uma lista de notas `numeros`, e retorna uma tupla contendo o nome do aluno e sua nota. A função retorna `-1.0` e uma mensagem que o aluno não foi encontrado caso `nome_procurado` não esteja em `nomes`.

    **SOLUÇÃO:**

    ``` python
    def procura_nota(nome_procurado, nomes, numeros):
        """
        Retorna um par (nome, nota) para um dado nome em nomes.
        """
        for indice, nome in enumerate(nomes):
            if nome == nome_procurado:
                return (nome, numeros[indice])

        print(f"{nome_procurado} não encontrado!")
        return ("Não encontrado!", -1.0)
    ```

5. Usando a função `chr(i)`, que busca o caractere que possui código `i` na tabela ASCII, e sabendo que as letras minúsculas do alfabeto possuem códigos entre 97 e 122 (inclusive), monte uma função `alfabeto()` que retorna uma lista com todas as letras do alfabeto. Utilize compreensão de listas para resolver esse exercício.

    **SOLUÇÃO:**

    ``` python
    def alfabeto():
        """Retorna um alfabeto minúsculo."""
        return [chr(i) for i in range(97, 123)]
    ```

6. Usando o módulo `random`, a função `random.shuffle(lista)` e a função `alfabeto()` criada no exercício anterior, que embaralha os valores de `lista`, implemente uma função `gera_chave()`, que retorna uma chave criptográfica gerada aleatoriamente. Uma chave criptográfica, nesse caso, é um dicionário que possui como chaves todas as letras do alfabeto, e como valores letras definidas aleatoriamente.

    **SOLUÇÃO:**

    ``` python
    def gera_chave():
        """Retorna uma chave criptográfica gerada aleatoriamente."""
        alfa = alfabeto() # De "a" a "z", em ordem
        alfa_random = alfabeto()
        random.shuffle(alfa_random) # alfabeto embaralhado

        chave = {}
        for indice, letra in enumerate(alfa):
            chave[letra] = alfa_random[indice]

        return chave
    ```

7. Implemente uma função `cripto()`, que recebe uma mensagem em string e uma chave criptográfica (como a criada no exercício anterior), e retorna a mensagem cifrada.

    **SOLUÇÃO:**

    ``` python
    def cripto(mensagem, chave):
        """Retorna uma mensagem criptografada."""
        msg_cripto = ""

        for letra in mensagem:
            msg_cripto += chave[letra]

        return msg_cripto
    ```

8. Implemente uma função `decripto()`, que recebe uma mensagem em string e uma chave criptográfica (como a criada no exercício 6), e retorna a mensagem descriptografada.

    **SOLUÇÃO:**

    ``` python
    def decripto(mensagem, chave):
        """Retorna uma mensagem decriptografada."""
        chave_decripto = {}
        for letra, letra_cripto in chave.items():
            chave_decripto[letra_cripto] = letra

        return cripto(mensagem, chave_decripto)
    ```

9. Implemente uma função `main()`, que gera uma chave criptográfica e lê mensagens inseridas pelo usuário e uma opção (se deseja encriptar ou decriptar uma mensagem), e exibe na tela a mensagem resultante.

    **SOLUÇÃO:**

    ``` python
    def main():
        """Ponto de entrada do programa."""
        chave = gera_chave()
        opcoes = {
            "1": cripto,
            "2": decripto
        }

        while True:
            msg = input("Informe uma mensagem: ")
            if msg == "":
                break
            oper = input("Informe uma opção: ")
            if oper not in opcoes:
                break

            print(opcoes[oper](msg, chave))
    ```

## Strings

1. Faça um programa para imprimir o texto abaixo, para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

    ```
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
    ```

    **SOLUÇÃO:**

    ``` python
    def imprime_sequencia_numeros(num):
        """Imprime uma sequência de números, até num."""
        for i in range(1, num + 1):
            print("   ".join([str(i)] * i))
    ```

2. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 → 721.

    **SOLUÇÃO:**

    ``` python
    def inverte_num(num):
        """Inverte os caracteres de num."""
        return str(num)[::-1]
    ```

3. Construa uma função que desenhe um retângulo usando os caracteres ‘+’, ‘−’ e ‘|‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, a função deve retornar uma mensagem de erro. Exemplos abaixo, para 2 linhas e 4 colunas, e para 4 linhas e 10 colunas.

    ```
    +--+
    +--+
    ```

    ```
    +--------+
    |        |
    |        |
    +--------+
    ```

    **SOLUÇÃO:**

    ``` python
    def retangulo(linhas=1, colunas=1):
        """Desenha um retângulo com os parâmetros passados."""
        if linhas <= 0 or colunas <= 0 or linhas > 20 or colunas > 20:
            return "Erro!\n"

        ret = ""
        for linha in range(linhas):
            if linha == 0 or linha == linhas - 1:
                ret += "+\n" if colunas == 1 else "+" + "-" * (colunas - 2) + "+\n"
            else:
                ret += "|\n" if colunas == 1 else "|" + " " * (colunas - 2) + "|\n"

        return ret
    ```

4. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

    **SOLUÇÃO:**

    ``` python
    def e_palindromo(palavra):
        print(palavra)
        return palavra == palavra[::-1]
    ```
