# Lista de Exercícios

Para os gabaritos dos exercícios resolvidos, consulte a página de [gabaritos](./exercicios_gabaritos.md).

### Índice

* [Introdução a Python](#introdução-a-python)
* [Operadores](#operadores)
* [Funções](#funções)
* [Estruturas de seleção](#estruturas-de-seleção)
* [Estruturas de repetição](#estruturas-de-repetição)
* [Estruturas de dados](#estruturas-de-dados)
* [Strings](#strings)
* [A Biblioteca padrão do Python](#a-biblioteca-padrão-do-python)

## Introdução a Python

### Exercícios propostos

1. Faça um programa que escreva a mensagem "Olá, mundo!" na tela.
2. Faça um programa que peça um número e então mostre a mensagem `O número informado foi [número]`.
3. Faça um programa que leia o seu nome e exiba na tela `Prazer, [nome], eu sou o Python!`.

## Operadores

### Exercícios propostos

1. Faça um programa que peça as três notas da disciplina (AP1, AP2 e AC) e mostre a média. A média é calculada de acordo com a fórmula `M = (AP1 + AP2) * 0.4 + AC * 0.2`.
2. Faça um programa que peça um comprimento em metros e converta para centímetros.
3. Faça um programa que leia o raio de um círculo, calcule e mostre sua área. Considere pi como aproximadamente igual a 3.14.
4. Monte um conversor de temperatura, que lê uma temperatura em graus Fahrenheit e mostre a temperatura em graus Celsius. A fórmula para conversão é `C / 5 = (F - 32) / 9`.

## Funções

### Exercícios resolvidos

1. Faça uma função `media()`, que recebe os parâmetros posicionais `ap1`, `ap2` e `ac`, e retorne a média de avaliações, utilizando a fórmula `M = (AP1 + AP2) * 0.4 + AC * 0.2`.
2. Faça uma função `m_para_cm()` que receba um comprimento em metros e converta para centímetros.
3. Faça uma função que receba o raio de um círculo, calcule e retorne sua área. Considere pi como aproximadamente igual a 3.14.
4. Monte um conversor de temperatura, que recebe uma temperatura em graus Fahrenheit e devolva a temperatura em graus Celsius. A fórmula para conversão é `C / 5 = (F - 32) / 9`.
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

### Exercícios propostos

1. Monte uma função que recebe um salário por hora e o número de horas trabalhadas no mês, e retorne o salário a ser recebido.
2. Elabore uma função que receba três números e exiba na tela: (1) o produto do dobro do primeiro com metade do segundo; (2) a soma do triplo do primeiro com o terceiro; e (3) o terceiro elevado ao cubo.
3. Elabore uma função com as mesmas regras do exercício anterior, porém retornando os três resultados, ao invés de exibi-los na tela.
4. João Papo-de-Pescador, homem de bem, comprou um computador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça uma função que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Retorne o valor da multa. Assumir que a quantidade de quilos é sempre superior a 50.
5. Faça um programa que receba dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

## Estruturas de seleção

### Exercícios resolvidos

1. Elabore uma função `e_par`, que recebe um número e retorna `True` ou `False` conforme o número seja par ou não.
2. Implemente um programa que receba dois números e retorne o maior deles.
3. Crie uma função que receba um valor e retorne se ele é positivo ou negativo.
4. Faça um programa que verifique se uma letra é vogal ou consoante.
5. Faça um programa que receba três notas, calcule sua média aritmética simples e apresente na tela uma das seguintes informações:

    * A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    * A mensagem "Reprovado", se a média for menor do que sete;
    * A mensagem "Aprovado com Distinção", se a média for igual a dez;
    * A mensagem "Nota inválida!" toda vez que for inserido um valor inválido.

### Exercícios propostos

1. Faça um programa que leia três números e mostre o maior deles.
2. Faça um programa que leia três números e mostre o maior e o menor deles.
3. Faça uma função `saudacao()`, que recebe o parâmetro `turno` como entrada, podendo ser “M” para matutino, “V” para vespertino ou “N” para noturno. Exiba na tela a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
4. Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo a tabela a seguir, baseado no salário atual. Após o aumento ser realizado, informe na tela:

    * O salário antes do reajuste;
    * O percentual de aumento aplicado;
    * O valor do aumento;
    * O novo salário, após o aumento.

    ```
    Salários até R$ 280,00 (incluindo)      Aumento de 20%
    Salários entre R$ 280,00 e R$ 700,00    Aumento de 15%
    Salários entre R$ 700,00 e R$ 1500,00   Aumento de 10%
    Salários de R$ 1500,00 em diante        Aumento de 5%
    ```

5. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são dados na lista abaixo. O Salário Líquido corresponde ao Salário Bruto menos os descontos (imposto e sindicato). O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês, e deve imprimir todos os cálculos realizados. O desconto do IR é calculado conforme a tabela em seguida.

    * Imposto de Renda, que depende do salário bruto (conforme tabela abaixo);
    * 3% do salário bruto para o Sindicato;
    * O FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).

    ```
    Salário bruto até R$900 (inclusive)     isento;
    Salário bruto até R$1500 (inclusive)    desconto de 5%;
    Salário bruto até R$2500 (inclusive)    desconto de 10%;
    Salário bruto acima de R$2500           desconto de 20%.
    ```

6. Uma loja de tintas possui galões de 18 litros que custam R$80.00 a unidade, e latas de 3.6 litros que custam R$25.00 a unidade. É conhecido que essa marca de tintas consome aproximadamente um litro para cada 6 metros quadrados de parede. Considere que um cliente da loja apresenta uma `área` a ser pintada, e que, por segurança, adotamos 10% de margem de segurança, ou seja, compramos sempre, pelo menos, 10% a mais de tinta do que o suficiente para cobrir `área`. Implemente uma função `otimiza_tinta` que receba `area` e determine a melhor combinação de galões e latas a serem compradas, de forma que o preço seja sempre o menor.
7. Implementa uma função que receba um número e exiba o dia correspondente da semana (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
8. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:

    * Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    * Triângulo Equilátero: três lados iguais;
    * Triângulo Isósceles: quaisquer dois lados iguais;
    * Triângulo Escaleno: três lados diferentes.

9. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma `ax^2 + bx + c`. O programa deverá receber os valores de `a`, `b` e `c` e fazer as consistências, informando ao usuário nas seguintes situações:

    * Se o usuário informar o valor de `a` igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    * Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
    * Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário;
    * Se o delta for positivo, a equação possui duas raízes reais, informe-as ao usuário.

10. Elabore uma função `e_bissexto()` que receba um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

## Estruturas de repetição

### Exercícios resolvidos

1. Elaborar uma função `conta_pares(min, max)` para exibir todos os valores entre `min` e `max`, com um incremento de 2, separando-os com um hífen. Ex.: `2 – 4 – 6 – 8 – 10 – 12 – 14`.
2. Faça um programa que peça um nome de usuário e a sua senha, exiba uma mensagem de erro e retorne `False` caso os dois valores sejam iguais e retorne `True` caso sejam valores diferentes. O programa deve continuar pedindo uma nova senha até que o valor seja válido.
3. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    ```
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50
    ```

4. Faça um programa que calcule o fatorial de um número inteiro positivo fornecido pelo usuário. Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120.
5. Supondo que a população de um país A seja da ordem de `pop_a` habitantes com uma taxa anual de crescimento de 3% e que a população de B seja `pop_b` habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

### Exercícios propostos

1. Faça um programa que receba 5 números e informe o maior número.
2. Implemente uma função `fibo(num)` que recebe `num` e calcule o "num-ésimo" elemento da série de Fibonacci. Considere que a série é formada pela sequência 1, 1, 2, 3, ...
3. Elabore uma função `e_primo(num)` que retorna se um número `num` é primo ou não. Caso `num` não seja primo, liste todos os números pelos quais `num` é divisível.
4. Crie uma função `lista_primos(min, max)`, que exibe na tela todos os primos entre `min` e `max`.
5. Elabore um programa que lê votos de uma zona eleitoral, com candidatos "A", "B" e "C". O mesário insere os votos, um a um, e quando não há mais votos, ele pressiona "ENTER". O programa deve, por fim, calcular o número de votos para cada candidato, além dos votos nulos (aquelas entradas diferentes de qualquer candidato), e exibir o número de votos e o percentual de votos para cada opção.
6. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo, e logo em seguida é apresentado um exemplo da saída do programa. No momento, não é necessário formatar os valores.

    ```
    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1                       0
    3                       10
    6                       15
    9                       20
    12                      25
    ```

    ```
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     R$ 100,00       3                       R$    366,00
    R$ 1.150,00     R$ 150,00       6                       R$    191,67
    ```

7. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

## Estruturas de Dados

### Exercícios resolvidos

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

### Exercícios propostos

1. Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
2. Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
3. Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor par e os números ímpares no vetor impar. Imprima os três vetores.
4. Faça um programa que leia um vetor com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
5. Faça um programa que leia as idades e alturas de N alunos do ensino fundamental (N é um número fornecido pelo usuário) e determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
6. Elabore uma função que identifica se uma matriz n x n informada é um quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número diferente em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

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

## Strings

### Exercícios resolvidos

1. Faça um programa para imprimir o texto abaixo, para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

    ```
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
    ```

2. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 → 721.
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

4. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

### Exercícios propostos

1. Faça um programa para imprimir o texto abaixo, para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

    ```
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
    ```

2. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
3. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

    ```
    Compara duas strings
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.
    ```

4. Elabore uma função que imprime um cabeçalho. A função recebe dois argumentos: a largura do cabeçalho em número de caracteres e o título. O título deve ser disposto centralizado no cabeçalho, e caso o número de espaços a serem preenchidos na linha do título seja ímpar, o programa deve colocar esse espaço adicional à esquerda do título. Veja exemplo abaixo:

    ```
    ============================================================
                    RELATÓRIO DE PAGAMENTO
    ============================================================
    ```

5. Elabore uma função que recebe uma lista de nomes e uma lista de e-mails e imprime as informações na tela considerando uma largura máxima de 60 caracteres. Os nomes devem ficar alinhados à esquerda, e os e-mails, alinhados à direita. Cada par nome/email deve preencher uma linha do relatório final.
6. Faça um programa que formate um relatório. O programa recebe como parâmetros o nome do usuário, a sua matrícula, o seu salário bruto e o valor a ser descontado. O programa deve calcular o salário líquido e exibir o relatório exatamente no seguinte formato:

    ```
    Informe a matrícula: 12345678
    Informe o nome do usuário: Victor Machado da Silva
    Informe o salário bruto: 1000
    Informe o total de descontos: 30
    ============================================================
                    RELATÓRIO DE PAGAMENTO
    ============================================================
    Usuário                              Victor Machado da Silva
    Matrícula                                           12345678
    Salário bruto:                                     R$ 1000.0
    (-) Descontos:                                       R$ 30.0
    ------------------------------------------------------------
    (=) Salário líquido:                                R$ 970.0
    ```

7. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

## A Biblioteca padrão do Python

### Exercícios propostos

1. Utilizando o pacote `random`, faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores (1-6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.
2. Utilizando o pacote `random`, construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra `python`, pode retornar `npthyo`, `ophtyn` ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
3. Utilizando o pacote `json`, faça um programa que leia dados de alunos (nome, matrícula e e-mail) e salve esses dados em um arquivo `.json`, com o seguinte formato:

    ``` json
    {
        “1234”: {
            “nome”: “André Guimarães”,
            “e-mail”: “andre.guim@gmail.com”
        },
        “5678”: {
            “nome”: “Vanessa Barboza”,
            “e-mail”: “vbarboza@yahoo.com”
        },
        “9012”: {
            “nome”: “Renato Amorim”,
            “e-mail”: “ream@hotmail.com”
        },
    }
    ```

4. Utilizando o pacote `datetime`, construa uma função que receba uma data no formato `DD/MM/AAAA` e devolva uma string no formato `D de mesPorExtenso de AAAA`. Opcionalmente, valide a data e retorne `None` caso a data seja inválida.
5. Utilizando o pacote `turtle`, elabore um desenho de uma estrela de N pontas, com N sendo um número fornecido pelo usuário. A figura abaixo ilustra um exemplo para 9 pontas.

    ![Turtle](/prog/img/011.001.jpg)

6. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo. Dica: utilize o pacote random para escolher a palavra e embaralhar a palavra escolhida.
7. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente (utilize o pacote random). O jogador poderá errar 6 vezes antes de ser enforcado.

    ```
    Digite uma letra: A
    -> Você errou pela 1ª vez. Tente de novo!

    Digite uma letra: O
    A palavra é: _ _ _ _ O

    Digite uma letra: E
    A palavra é: _ E _ _ O

    Digite uma letra: S
    -> Você errou pela 2ª vez. Tente de novo!
    ```

8. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este ponto novamente.
