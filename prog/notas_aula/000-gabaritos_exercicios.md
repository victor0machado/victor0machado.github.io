# Gabaritos dos exercícios resolvidos

### Índice

* [Nota de aula 02](#nota-de-aula-02-algoritmos-e-lógica-de-programação)
* [Nota de aula 05](#nota-de-aula-05-funções)
* [Nota de aula 06](#nota-de-aula-06-estruturas-de-seleção)
* [Nota de aula 07](#nota-de-aula-07-estruturas-de-repetição)
* [Nota de aula 08](#nota-de-aula-08-estruturas-de-dados)
* [Nota de aula 09](#nota-de-aula-09-strings)

## Nota de aula 02: Algoritmos e Lógica de Programação

[Link para a nota de aula](./002-algoritmos.md)

1. Faça um procedimento `maior` que receba dois números e retorne o maior deles.

    **SOLUÇÃO:** Veja que não usamos aqui a instrução "senão", uma vez que, se o `x` for maior que `y`, o procedimento já é encerrado e nunca executará a instrução 2.

    ```
    PROCEDIMENTO maior(x, y)
    -----------------------------
    # Entrada: parâmetros x e y são números.
    # Saída: o maior dentre x e y.
    -----------------------------
    1. Se x > y, encerre o procedimento e retorne x.
    2. Encerre o procedimento e retorne y.
    ```

2. Faça um procedimento `fatorial` que receba um número (assumindo inteiro positivo) e devolva o fatorial dele.

    **SOLUÇÃO:** A lógica aqui é que o fatorial de um número é igual ao produto de todos os inteiros, de 1 até o número. Existem algoritmos mais elegantes que essa solução, incluindo recursividade, mas para o propósito desta aula, este algoritmo é preciso e eficiente o suficiente.

    ```
    PROCEDIMENTO fatorial(x)
    -----------------------------
    # Entrada: parâmetro x é um número inteiro positivo.
    # Saída: o fatorial de x.
    -----------------------------
    1. Atribua 1 para a variável fat.
    2. Para i = 1 até x, faça:
      2.1. Atribua i * fat para a variável fat.
    3. Encerre o procedimento e retorne fat.
    ```

3. Faça um procedimento `maximo` que receba um arranjo de números e o número de elementos deste arranjo e retorne o maior valor contido no arranjo.

    **SOLUÇÃO:** Podemos aqui fazer algo parecido com o algoritmo `busca_linear` que temos na nota de aula. No entanto, ao contrário do algoritmo de busca, este sempre retorna um elemento do arranjo e não pode ter menos que `n` iterações (descontando a iteração do primeiro elemento, que está sendo feita na instrução 1).

    ```
    PROCEDIMENTO maximo(A, n)
    -----------------------------
    # Entrada:
    #   - A: um arranjo de números.
    #   - n: o valor do maior índice de A, maior que zero.
    # Saída: o elemento de maior valor contido em A.
    -----------------------------
    1. Atribua A[0] para a variável max.
    2. Para i = 1 até n, faça:
      2.1. Se A[i] > max, atribua A[i] para max.
    3. Encerre o procedimento e retorne max.
    ```

4. Faça um procedimento `contagem_regressiva` que receba um número (assumindo inteiro positivo) e exiba na tela uma contagem regressiva deste número até zero, inclusive.

    **SOLUÇÃO:** Podemos usar aqui tanto a instrução "enquanto" quanto a instrução "para cada". Preferi usar a enquanto para não precisar criar novas variáveis dentro do procedimento.

    ```
    PROCEDIMENTO contagem_regressiva(x)
    -----------------------------
    # Entrada: parâmetro x é um número inteiro positivo.
    # Saída: Nenhuma.
    -----------------------------
    1. Enquanto x >= 0, faça:
      1.1. Exiba x na tela.
      1.2. Atribua o valor x - 1 a x.
    3. Encerre o procedimento.
    ```

5. Uma loja de tintas possui galões de 18 litros que custam R$80.00 a unidade, e latas de 3.6 litros que custam R$25.00 a unidade. É conhecido que essa marca de tintas consome aproximadamente um litro para cada 6 metros quadrados de parede. Considere que um cliente da loja apresenta uma `área` a ser pintada, e que, por segurança, adotamos 10% de margem de segurança, ou seja, compramos sempre, pelo menos, 10% a mais de tinta do que o suficiente para cobrir `área`. Desenvolva um algoritmo para um procedimento `otimiza_tinta` que receba `area` e determine a melhor combinação de galões e latas a serem compradas, de forma que o preço seja sempre o menor.

    **SOLUÇÃO:** Rapidamente podemos identificar que um galão (R$4.44/litro) é mais econômico que uma lata (R$6,94/litro). Além disso, vemos que se estivermos falando de um valor superior a 10.8 litros (3 latas) e inferior a 18 litros, também é mais vantajoso comprar um galão. Portanto, precisamos comprar quantos galões inteiros forem necessários, e obter o que restar. Desse resto, compramos em latas até um total de 10.8 litros, ou adicionamos mais um galão à nossa conta. Colocando no formato de um algoritmo, temos o seguinte:

    ```
    PROCEDIMENTO otimiza_tinta(area)
    -----------------------------
    # Entrada: parâmetro area é um número positivo.
    # Saída: um par [g, l], indicando o número de galões e
    #   latas necessários para compra, respectivamente.
    -----------------------------
    1. Atribua 1.1 * area / 6 para a variável tinta.
    2. Atribua a parte inteira da operação tinta / 18 para a variável galoes.
    3. Atribua tinta - galoes * 18 para a variável tinta.
    4. Se tinta < 10.8, faça:
      4.1. Atribua tinta / 3.6, arredondando para cima, para a variável latas.
    5. Senão, faça:
      5.1. Atribua galoes + 1 para a variável galoes.
      5.2. Atribua 0 para a variável latas.
    6. Encerre o procedimento e retorne o par [galoes, latas].
    ```

6. Desenvolva um procedimento `inverte_arranjo` que inverta os elementos de um arranjo `A`, de índice máximo `n`. Por exemplo, o retorno do procedimento com um arranjo `[1, 2, 3]` seria `[3, 2, 1]`.

    **SOLUÇÃO:** Para que o algoritmo não inverta o arranjo duas vezes, é necessário que a estrutura de repetição só vá até o meio do arranjo. Observe que, se o arranjo possui um número ímpar de elementos (ou seja, se `n` é par), não precisamos executar o algoritmo de troca para o elemento do meio. Para executar a troca, criamos uma variável `temp`, que armazena um dos valores para que a troca seja possível.

    ```
    PROCEDIMENTO inverte_arranjo(A, n)
    -----------------------------
    # Entrada:
    #   - A: um arranjo de números.
    #   - n: o valor do maior índice de A, maior que zero.
    # Saída: o arranjo A, com os elementos invertidos.
    -----------------------------
    1. Atribua para x a parte inteira de n / 2.
    2. Se n é par, atribua x - 1 para a variável x.
    3. Para cada i = 0, 1, ..., x faça:
      3.1. Atribua A[i] para uma variável temp.
      3.2. Atribua A[n - i] para A[i].
      3.3. Atribua temp para A[n - i].
    4. Encerre o procedimento e retorne A.
    ```

7. Elabore um procedimento que implemente o algoritmo de **busca binária**, aplicado para localizar valores em arranjos ordenados. O procedimento deve devolver o índice do arranjo em que foi encontrado o valor, ou -1 caso o valor não tenha sido encontrado. O conceito do algoritmo é o seguinte:

    * Para um determinado arranjo, vá até o meio deste e leia o valor do elemento.
    * Se o valor procurado for igual ao valor do elemento, encerre a busca.
    * Se o valor procurado for maior que o valor do elemento, continue procurando na metade maior do arranjo.
    * Se o valor procurado for menor que o valor do elemento, continue procurando na metade menor do arranjo.
    * Se todo o arranjo tiver sido percorrido e não for encontrado o valor, retorne um erro.

    Considere por exemplo o arranjo `[1, 4, 5, 16, 20, 25, 33]` e queremos procurar um valor `4`. Temos a seguinte execução:

    * Olhamos para o meio do arranjo, ou `16`.
    * `4` é menor que `16`,  então continuamos procurando na primeira parte do arranjo, `[1, 4, 5]`.
    * Agora olhamos para a metade da primeira parte do arranjo, que seria `4`.
    * `4` é igual a `4`, então retornamos esse valor e encerramos a busca.

    **SOLUÇÃO:**

    ```
    PROCEDIMENTO busca_binaria(A, inicio, fim, x)
    -----------------------------
    # Entrada:
    #   - A: um arranjo de números.
    #   - inicio: índice em que o algoritmo deve buscar no arranjo.
    #   - fim: índice até onde o algoritmo deve buscar no arranjo.
    #   - x: o valor a ser procurado.
    # Saída: O índice em que o valor foi localizado, ou -1 caso
    #   o valor não tenha sido encontrado.
    -----------------------------
    1. Atribua para y a parte inteira de (inicio + fim) / 2.
    2. Se A[y] = x, encerre o procedimento e retorne y.
    3. Se inicio = fim, encerre o procedimento e retorne -1.
    4. Se A[y] < x, então faça:
      4.1. Encerre o procedimento e retorne busca_binaria(A, y + 1, fim, x).
    5. Encerre o procedimento e retorne busca_binaria(A, inicio, y - 1, x).
    ```

## Nota de aula 05: Funções

[Link para a nota de aula](./005-funcoes.md)

Os quatro primeiros exercícios já foram feitos em listas de exercícios anteriores, portanto serão apresentadas apenas uma possível solução para cada problema, sem maiores discussões. Fica aqui o destaque para o uso correto dos parâmetros e para o retorno de cada função, bem como a documentação adequada das funções.

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

## Nota de aula 06: Estruturas de Seleção

[Link para a nota de aula](./006-estruturas-selecao.md)

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

## Nota de aula 07: Estruturas de Repetição

[Link para a nota de aula](./007-estruturas-repeticao.md)

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

2. Faça um programa que peça um nome de usuário e a sua senha, exiba uma mensagem de erro e caso os dois valores sejam iguais. O programa deve continuar pedindo uma nova senha até que o valor seja válido.

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

## Nota de aula 08: Estruturas de Dados

[Link para a nota de aula](./008-estruturas-dados.md)

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

## Nota de aula 09: Strings

[Link para a nota de aula](./009-strings.md)

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
