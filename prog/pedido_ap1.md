# Pedido da AP1 - Gerador de ficha de D&D

## Pedido

Implemente um gerador simplificado de personagens de D&D. A ideia é rolar atributos, definir modificadores baseados em raça, e salvar a ficha do personagem em um arquivo de texto. o programa deve seguir os passos listados abaixo:

1. O programa usa uma interface baseada em texto, que deve pedir as seguintes informações:

    - O nome do personagem;
    - Sua raça (humano, elfo, anão ou halfling).

2. Em seguida, ele deve fazer uma rolagem de "dados" para sortear os seis atributos de um personagem: força (STR), destreza (DEX), constituição (CON), inteligência (INT), sabedoria (WIS) e carisma (CHA). Para cada um dos atributos, o programa deve rolar quatro dados de seis faces, somando os três maiores números.

3. O programa deve apresentar os valores dos seis atributos para o usuário, que deve associar cada número a um atributo específico. Por exemplo, suponha que o programa chegou nos seguintes números:

    ```
    8 12 10 15 16 13
    ```

    O usuário deve associar cada um desses números a um atributo específico, com base nas suas preferências. Ele pode escolher, por exemplo:

    ```
    STR 15
    DEX 13
    CON 16
    INT 12
    WIS 10
    CHA 8
    ```

4. Após isso, o programa deve apresentar os valores finais dos atributos, somando os modificadores com base na classe ou raça. Humanos recebem +1 em todos os atributos, elfos +2 em DEX e +1 em INT, anões +2 em STR e +2 em CON, e halflings +2 em DEX e +1 em CHA. O programa deve então perguntar se o usuário está satisfeito com os resultados. Caso não esteja, o programa deve voltar para o passo 3.

5. Por fim, o programa deve exibir um resumo da ficha do personagem, e perguntar se o usuário deseja salvar esse conteúdo. Caso deseje, o programa deve criar um arquivo de texto com nome igual a `<personagem>.txt`, e voltar para a tela de início de criação do personagem.

### DICAS

- Use sys.exit() para sair do programa a partir de qualquer ponto do código;
- Use a função `random.randint(a, b)` para gerar um `N` inteiro, com `a <= N <= b`. Exemplo de uso:

    ``` python
    >>> import random
    >>> random.randint(1, 8)
    4
    ```

- Utilize a função `str.lower()` ou `str.upper()` para converter todos os caracteres para caixa baixa ou alta, respectivamente, e evitar comparações de strings contendo letras de _casing_ diferente. Exemplo de uso:

    ``` python
    "Água".lower()  # retorna "água"
    input("Insira um valor: ").upper()  # converte o resultado de input() para caixa alta
    ```

## Exemplos de exibição

### Caso de sucesso:

```
------------------------------------------------------------
Gerador de personagens D&D
Digite "sair" para sair do programa


Primeiro, informe seu nome: Legolas
Informe sua raça: Elfo

Resultados dos dados:
16 12 14 7 5 17
Escolha um valor para STR: 16
12 14 7 5 17
Escolha um valor para DEX: 12
14 7 5 17
Escolha um valor para CON: 14
7 5 17
Escolha um valor para INT: 7
5 17
Escolha um valor para WIS: 5
17
Escolha um valor para CHA: 17

Resultados atribuídos com modificadores de raça:
STR 16
DEX 14
CON 14
INT 8
WIS 5
CHA 17
Estes valores estão satisfatórios (S/N)? s

========================================
Ficha de Legolas / elfo:
STR 16
DEX 14
CON 14
INT 8
WIS 5
CHA 17
========================================

Deseja salvar a ficha (S/N)? S
Ficha salva em Legolas.txt
```

### Usuário erra raça

```
Primeiro, informe seu nome: Gimli
Informe sua raça: anao
Raça inválida! As opções são humano, elfo, anão, halfling
Informe sua raça: anão
```

### Usuário erra escolha de atributos

```
Resultados dos dados:
14 15 17 14 14 6
Escolha um valor para STR: 15
14 17 14 14 6
Escolha um valor para DEX: 17
14 14 14 6
Escolha um valor para CON: 9
Valor passado é inválido! Tente novamente.
Escolha um valor para CON: 15
Valor passado é inválido! Tente novamente.
Escolha um valor para CON: 14
14 14 6
Escolha um valor para INT: 14
14 6
Escolha um valor para WIS: 14
6
Escolha um valor para CHA: 6
```

### Usuário deseja não salvar atributos

```
Resultados atribuídos com modificadores de raça:
STR 17
DEX 17
CON 16
INT 14
WIS 14
CHA 6
Estes valores estão satisfatórios (S/N)? n

Resultados dos dados:
14 15 17 14 14 6
Escolha um valor para STR: 14
15 17 14 14 6
Escolha um valor para DEX: 15
17 14 14 6
Escolha um valor para CON:
...
```

### Usuário deseja não salvar arquivo

```
========================================
Ficha de Gimli / anão:
STR 16
DEX 15
CON 19
INT 14
WIS 14
CHA 6
========================================

Deseja salvar a ficha (S/N)? n
```

### Usuário sai do programa

```
------------------------------------------------------------
Gerador de personagens D&D
Digite "sair" para sair do programa


Primeiro, informe seu nome: sair
```

## Avaliação

O projeto será avaliado de acordo com os seguintes critérios:

* Qualidade de escrita do código: variáveis foram bem nomeadas, código está de acordo com os padrões discutidos em sala (_casing_, indentação, espaçamento, sem variáveis globais, etc.);
* Qualidade dos algoritmos: o código não apresenta redundâncias ou trechos não solicitados. O algoritmo está completo e atende a todos os pedidos nos requisitos do projeto;
* Apresentação do projeto: o grupo será questionado com relação à solução no dia da entrega do projeto;
* Testes realizados pelo professor não apresentam falhas.

## Informações gerais:

* Prazo: 09/10/2022
* Grupos de no mínimo 3 e no máximo 4 pessoas
* Subir na Sala de Aula Virtual o código salvo no formato .txt
* Incluir o nome de todos os participantes como docstring no início do código
