# Resolução de exercícios de algoritmos

## Tomadas

Link: https://br.spoj.com/problems/TOMADA13/

A lógica por trás desse algoritmo é que, para maximizar o número de tomadas disponíveis para os usuários, é necessário que todas as réguas estejam conectadas entre si. Portanto, considerando que uma régua está conectada na parede, as outras três precisam estar conectadas em outras réguas. Já que estamos lidando com réguas, podemos assumir com segurança que cada uma possui pelo menos duas tomadas, sendo uma usada pela régua seguinte e uma ficando livre para uso de alguém.

Dessa forma, para obtermos nossa resposta, basta somar o número total de tomadas disponíveis e diminuir três.

```
PROGRAMA TOMADA
    Lê T1, T2, T3, T4
    totalTomadas := T1 + T2 + T3 + T4
    Escreve totalTomadas - 3
```

## Meteoros

Link: https://br.spoj.com/problems/METEORO/

Esse é um problema de geometria. Para que o meteorito tenha caído na fazenda, basta que as suas coordenadas estejam localizadas dentro do retângulo delimitador da fazenda. Supondo, por exemplo que o meteorito está nas coordenadas `(x, y)`, e o retângulo seja delimitado pelos cantos `(x1, y1)` (superior esquerdo) e `(x2, y2)` (inferior direito), podemos assumir que o meteorito caiu na fazenda se as duas condições abaixo forem satisfeitas:

- `x1 <= x <= x2`;
- `y2 <= y <= y1`.

O desafio adicional do programa é ler, continuamente, áreas de fazendas e meteoritos, até que seja inserido o campo `0 0 0 0`. Para isso, é necessário incluir um segundo laço logo no início do programa. Um outro ponto importante é que o texto de saída só deve ser inserido após o final da execução do programa, então ele deve ser armazenado em uma variável.

```
PROGRAMA METEOROS
    contFazenda := 0
    mensagem := ""

    Enquanto VERDADEIRO, faça:
        Lê x1, y1, x2, y2
        Se x1 = x2 = y1 = y2 = 0 então:
            Pare

        contFazenda += 1
        mensagem += "Teste " + contFazenda + "\n"

        Lê numMeteoritos
        meteoritosNaFazenda := 0

        Para cada meteorito entre 1 e numMeteoritos, faça:
            Lê x, y
            Se x1 <= x <= x2 e y2 <= y <= y1 então:
                meteoritosNaFazenda++

        mensagem += meteoritosNaFazenda + "\n"

    Escreve mensagem
```

## Desafio do Maior Número

Link: https://br.spoj.com/problems/JDESAF12/

O principal ponto nesse problema é a análise do maior número durante a execução. Ou seja, a qualquer momento pode ser inserido um valor `0` e o programa será encerrado. Pensando num primeiro momento, o problema poderia ser resolvido criando-se um array, que vai recebendo os números um a um, e no momento em que é lido um `0` o programa calcula o maior número. Porém, isso gera um consumo de memória que não é adequado.

Pode-se pensar em uma solução que utilize uma única variável para armazenar um inteiro, e que ela fique sendo alterada durante a execução do programa. Como o problema listou que todos os números válidos são maiores que zero, essa variável pode ser inicializada como zero.

```
PROGRAMA MAIOR_NUMERO
    maior := 0

    Enquanto VERDADEIRO, faça:
        Lê numero
        Se numero = 0 então:
            Pare
        Se numero > maior então:
            maior = numero

    Escreve maior
```

## Cartas

Link: https://br.spoj.com/problems/CARTAS14/

Esse problema pode ser inspirado pela solução do problema anterior. Podemos ter uma variável que indica a classificação da sequência. Se após a leitura dos dois primeiros números for identificada uma tendência de alta, muda-se a variável de classificação para "C". Se houver uma tendência de queda, muda-se para "D". Nas leituras seguintes, identifica-se se houve uma mudança na classificação. Caso tenha havido, muda-se a variável de classificação para "N" e encerra o programa. Se a leitura chegou ao fim e não houve mudança, retorna-se o valor da variável.

Pode-se otimizar ainda mais essa solução, para que ela tenha o uso de apenas três variáveis, duas numéricas e uma de texto. Ao longo da execução do programa, as variáveis numéricas vão sendo substituídas.

```
PROGRAMA CARTAS
    n1, n2 := 0
    classificacao := ""

    Enquanto houver números, faça:
        Lê n2
        Se n1 = 0 então:
            n1 = n2
            continue

        Se n2 > n1:
            Se classificacao = "" então:
                classificacao = "C"
            Senão se classificacao = "D":
                classificacao = "N"
                Pare

        Se n2 < n1:
            Se classificacao = "" então:
                classificacao = "D"
            Senão se classificacao = "C":
                classificacao = "N"
                Pare

        n1 = n2

    Escreve classificacao
```

## Encontre o telefone

Link: https://br.spoj.com/problems/ENCOTEL/

Este é um caso de substituição. Em algumas linguagens, como Go, há uma estrutura adequada para isso (`switch`). Basta analisar cada elemento do texto inserido e fazer a conversão necessária, conforme a tabela apresentada no problema. Conforme o problema, todos as letras inseridas são maiúsculas.

```
PROGRAMA ENCONTRE_TELEFONE
    Enquanto houver expressões, faça:
        Lê expressao
        telefone = ""

        Para cada caractere em expressão, faça:
            Analise caractere:
                Caso "1", "0" ou "-":
                    telefone += caractere
                Caso "A", "B" ou "C":
                    telefone += "2"
                Caso "D", "E" ou "F":
                    telefone += "3"
                Caso "G", "H" ou "I":
                    telefone += "4"
                Caso "J", "K" ou "L":
                    telefone += "5"
                Caso "M", "N" ou "O":
                    telefone += "6"
                Caso "P", "Q", "R" ou "S":
                    telefone += "7"
                Caso "T", "U" ou "V":
                    telefone += "8"
                Caso "W", "X", "Y" ou "Z":
                    telefone += "9"

        Escreve telefone
```

## F91

Link: https://br.spoj.com/problems/F91/

Nesse caso, o objetivo é apenas implementar a função proposta por McCarthy.

```
PROGRAMA PRINCIPAL
    Lê numeros

    Para cada numero em numeros, faça:
        Escreva "f91(" + numero + ") = " + F91(numero)

PROGRAMA F91(n)
    Se n <= 100 então:
        Retorna F91(F91(n + 11))
    Senão:
        Retorna n - 10
```

## Rumo aos 9s

Link: https://br.spoj.com/problems/RUMO9S/

Neste problema, temos que analisar a regra de qual é o grau-9 da soma dos dígitos de um número. Se a soma dos dígitos foi igual a 9, o número tem grau-9 igual a 1. Se a soma desse resultado for igual a 9, o seu grau-9 é 2, e assim sucessivamente. A condição de parada aqui deve ser se a soma dos dígitos for menor ou igual a 9. Caso seja igual a 9, o número é um multiplo.

Para apresentar o resultado da forma que está sendo solicitado, vamos precisar passar, através da recursão, o número original e o grau-9 naquele instante, ou seja, quantas vezes o programa precisou se aprofundar na recursão. Caso desejado, o número original pode ser mantido fora da recursão, caso a função principal faça o trabalho de exibir o resultado final.

Um ponto importante aqui é que os números iniciais podem ter até 1000 dígitos. Isso implica que não podemos calcular o número como um inteiro. Portanto, em termos de implementação, o cálculo do primeiro número deve ser feito convertendo o número para uma string, percorrendo os seus caracteres e somando dígito a dígito. Do segundo número em diante, é possível fazer a soma de cada dígito como inteiro, mas podemos manter a lógica da recursão.

O último ponto de observação é com relação ao grau-9. Caso a string passada seja "9", seu grau-9 é 1. Porém, caso a string seja "18", seu grau-9 também é 1. Por isso, incluímos na primeira condição de parada uma estrutura de decisão para resolver essa questão.

```
PROGRAMA PRINCIPAL
    Lê numeros

    Para cada numero em numeros, faça:
        RUMO_AOS_9(numero, numero, 0)

PROGRAMA RUMO_AOS_9(original, n, grau)
    Se n = '9' então:
        Se grau = 0 então faça grau = 1
        Escrever original + " is a multiple of 9 and has 9-degree " + grau
    Senão se n tiver apenas um caractere então:
        Escrever original " is not a multiple of 9"
    Senão:
        soma := 0

        Para cada digito em n, faça:
            Converter digito para inteiro
            soma += digito

        Converter soma para string
        RUMO_AOS_9(soma, grau + 1)
```

## Paridade

Link: https://br.spoj.com/problems/PARIDADE/

Essa é uma solução que pode se inspirar na resolução do problema anterior. A diferença principal é que agora o maior número possível é 2.147.483.647, então ele cabe em um inteiro de 32 bits. Segundo a lógica para converter um número base-10 para base-2:

- Divide-se o número por 2
- Pega-se o resto da divisão e coloca em uma string "resultado"
- O quociente é passado para a mesma função, que reinicia o processo até que o quociente seja igual a 0

Importante que os restos da divisão devem ser lidos "ao contrário", ou seja, o resto da última operação é dígito mais à esquerda do número final. Além disso, também mantemos como parâmetro da função um campo para controlar a paridade do número.

```
PROGRAMA CALCULA_PARIDADE(numero, numeroBin, paridade)
    quociente := parte inteira de numero / 2
    resto := resto da divisão de numero por 2

    Se resto = 1 então:
        paridade++

    numeroBin = resto + numeroBin

    Se quociente = 0 então:
        Escrever "The parity of " + numeroBin + " is " + paridade + " (mod 2)."
    Senão:
        CALCULA_PARIDADE(quociente, numeroBin, paridade)
```
