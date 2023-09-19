# IBM1737 - Programação Estruturada

Vou colocar nessa página links das aulas e materiais adicionais referentes à disciplina.

* [GRID](grid.md)

## Material geral

* [Slides da disciplina](/./assets/prog/slides.pdf)
* [Vídeo com tutorial para configuração do VSCode e Github](/./assets/prog/videos/github_vscode.mp4)
* [Exercícios de fundamentos](./exercicios/001-exercicios_fixacao.md)
* [Pedido da AP1](./pedido_ap1.md)

## Notas de aula

* [01 - Introdução ao Curso](./notas_aula/001-intro_curso.md)
* [02 - Algoritmos e Lógica de Programação](./notas_aula/002-algoritmos.md)
* [03 - Introdução a Python](./notas_aula/003-intro-python.md)
* [04 - Operadores](./notas_aula/004-operacoes.md)
* [05 - Funções](./notas_aula/005-funcoes.md)
* [06 - Estruturas de Seleção](./notas_aula/006-estruturas-selecao.md)
* [07 - Estruturas de Repetição](./notas_aula/007-estruturas-repeticao.md)
* [08 - Estruturas de Dados](./notas_aula/008-estruturas-dados.md)
* [09 - Strings](./notas_aula/009-strings.md)
* [10 - Erros e Exceções](./notas_aula/010-erros-excecoes.md)
* [11 - A Biblioteca Padrão do Python](./notas_aula/011-biblioteca-padrao.md)
* [12 - Módulos e Pacotes](./notas_aula/012-modulos-pacotes.md)
* [13 - Classes e Noções de Orientação a Objetos](./notas_aula/013-intro-oo.md)

## Conteúdos específicos das turmas

* [Gabaritos das ACs](https://github.com/victor0machado/prog-2023.2/tree/main/ac)
* [Turma 1 (terças e quintas manhã)](https://github.com/victor0machado/prog-2023.2/blob/main/turma_1)
* [Turma 2 (terças tarde)](https://github.com/victor0machado/prog-2023.2/blob/main/turma_2)
* [Turma 3 (quartas tarde)](https://github.com/victor0machado/prog-2023.2/blob/main/turma_3)

## Pedidos da AC

### AC1

- [Link para o notebook no Colab](https://colab.research.google.com/drive/1ni28fihtvLauYioHKkyUZyTedNjTCgfY?usp=sharing)

1. Elabore um código em Python que resolva uma equação do segundo grau `ax² + bx + c = 0`. O programa deve pedir os parâmetros `a`, `b` e `c` da equação e deve calcular as raízes pela fórmula de Bhaskara. Considere que as raízes são reais. Exemplo: `a = 1`, `b = -6`, `c = 8` dá como raízes `4` e `2`.
2. Elabore um programa que leia uma variável inteira `ano`. Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

### AC2

- [Link para o notebook no Colab](https://colab.research.google.com/drive/1LB4P43poWJSDps-wFZV49gw9IVlAbDG8?usp=sharing)

1. Monte uma função que recebe um salário por hora e o número de horas trabalhadas no mês, e retorne o salário a ser recebido.
2. Elabore uma função que receba três números e exiba na tela: (1) o produto do dobro do primeiro com metade do segundo; (2) a soma do triplo do primeiro com o terceiro; e (3) o terceiro elevado ao cubo.
3. Elabore uma função com as mesmas regras do exercício anterior, porém retornando os três resultados, ao invés de exibi-los na tela.
4. Elabore uma função que receba uma variável inteira ano. Em seguida, retorne o resultado da expressão lógica que indica se um ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

### AC3

1. Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo a tabela a seguir, baseado no salário atual. Após o aumento ser realizado, informe na tela:

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
2. Implementa uma função que receba um número e exiba o dia correspondente da semana (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
3. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma `ax^2 + bx + c`. O programa deverá receber os valores de `a`, `b` e `c` e fazer as consistências, informando ao usuário nas seguintes situações:

    * Se o usuário informar o valor de `a` igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    * Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
    * Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário;
    * Se o delta for positivo, a equação possui duas raízes reais, informe-as ao usuário.

### AC4

1. Elabore uma função `e_primo(num)` que retorna se um número `num` é primo ou não. Caso `num` não seja primo, liste todos os números pelos quais `num` é divisível.
2. Faça um programa que receba o valor de uma dívida e mostre as opções de parcelamento. O resultado final deve conter as opções de 1, 3, 6, 9 ou 12 parcelas, e o percentual de juros para cada parcela deve ser determinado conforme a primeira tabela, abaixo. O relatório com as opções de pagamento deve conter os seguintes dados: valor dos juros, valor total da dívida (incluindo juros), quantidade de parcelas e valor da parcela. A segunda tabela, abaixo, mostra um exemplo de como o resultado deve ser exibido. No momento, não é necessário formatar os valores.

    ```
    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1                       0
    3                       10
    6                       15
    9                       20
    12                      25
    ```

    ```
    Valor dos Juros Valor Total     Quantidade de Parcelas  Valor da Parcela
    0               R$ 1.000,00     1                       R$  1.000,00
    R$ 100,00       R$ 1.100,00     3                       R$    366,00
    R$ 150,00       R$ 1.150,00     6                       R$    191,67
    ```

3. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

---

[Voltar](https://victor0machado.github.io/)
