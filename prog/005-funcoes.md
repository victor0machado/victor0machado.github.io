# Funções

Até agora vimos os conceitos mais fundamentais acerca de qualquer linguagem de programação. Tópicos como variáveis, operadores e tipos de dados tendem a se manter os mesmos, exceto algumas poucas exceções.

Para os próximos assuntos que veremos, apesar de já termos discutido os seus conceitos teóricos, a implementação desses conceitos varia conforme a linguagem de programação. Nesta nota de aula começaremos pelas **funções**, que são análogas ao conceito de **procedimentos**, visto na [segunda aula](002-algoritmos.md). Veremos como este conceito pode ser usado na linguagem Python, e por que devemos nos preocupar em criar funções dentro dos nossos projetos.

### Índice

1. [O que é uma função?](#o-que-é-uma-função)
2. [Sintaxe de funções](#sintaxe-de-funções)
3. [Parâmetros](#parâmetros)
4. [Saída ou retorno](#saída-ou-retorno)
5. [Documentando funções](#documentando-funções)
6. [Exercícios resolvidos](#exercícios-resolvidos)
7. [Exercícios complementares](#exercícios-complementares)
8. [Sugestão de conteúdos](#sugestões-de-conteúdos)

## O que é uma função?

Suponha que você trabalha em uma grande organização, que está desenvolvendo um sistema de gestão empresarial (ou um ERP, _enterprise resource planning_), e que você ficou responsável pela implementação de um modelo de relatório, que será utilizado em todas as áreas desse sistema.

Todo relatório precisa de um cabeçalho, certo? Poderíamos, então, gerar um código que escreva um cabeçalho para o relatório financeiro emitido pelo sistema, que pode ser algo como:

``` python
titulo = "Financeiro"

print("-" * 40)
print(titulo)
print("-" * 40)
```

Este código resolve a questão de um relatório financeiro, mas veja que, se for necessário agora elaborar um relatório de marketing, você precisa criar um novo bloco de código:

``` python
titulo = "Marketing"

print("-" * 40)
print(titulo)
print("-" * 40)
```

Caso o sistema cresça e você precise inserir novos relatórios, como "Contábil", "Almoxarifado" ou "Pessoas", você precisará inserir essas mesmas quatro linhas, por mais parecidas elas sejam. Isso normalmente vai acontecer em uma série de arquivos diferentes, que contêm, juntos, algumas centenas de milhares (ou mesmo milhões) de linhas de código. É trabalhoso, mas é possível de ser feito.

Agora considere que, 2 anos depois, houve uma mudança no formato dos relatórios, e o caractere separador do título deixou de ser `-` e passou a ser `=`, e designaram para você o trabalho de alterar o formato dos relatórios em todos os pontos do código. Você já atuou em outros três projetos depois desse, e não se lembra de absolutamente nada deste projeto (compreensivelmente).

A solução para este problema, infelizmente, é resgatar toda e qualquer menção a um relatório, e fazer a alteração de caracteres. Isso gera um risco enorme, no entanto: como você já tinha saído do projeto, você não sabe quantos relatórios são gerados pelo sistema, então as chances de você esquecer de trocar um caractere no código é enorme. Dessa forma, um relatório (ou mais, o que é mais provável) ficou com o formato antigo.

Conseguem entender a dificuldade desta implementação? Temos um bloco de código que é, claramente, replicável, porém nossa implementação não previu que pudesse haver alterações ao longo do tempo. Este é um erro muito comum em programadores iniciantes, e devemos tentar corrigir da forma mais rápida possível.

O conceito de procedimentos, que vimos [na aula de algoritmos](002-algoritmos.md), surge para evitar (ou minimizar) esse problema. Dentro de um procedimento, temos um conjunto de instruções (ou um algoritmo), que pode ser chamado a qualquer momento ao longo da execução do meu sistema.

Costumamos chamar o processo em que utilizamos procedimentos para reutilizr um determinado algoritmo em diversos momentos no programa de **encapsulamento** ou **componentização** de código. Da mesma forma que não sabemos a proporção ou mesmo a composição dos remédios que consumimos, encapsular código significa agrupar um ou mais algoritmos dentro de um único procedimento, que pode ser utilizado e reaproveitado sem necessariamente ter um conhecimento de como ele funcione.

No Python chamamos os procedimentos de **funções**. Assim como os procedimentos, toda função possui um nome, parâmetros de entrada, um conjunto de instruções de processamento, e uma ou mais saídas. Veremos todos esses conceitos aplicados nesta aula.

Como regra geral, **todo código deve ser encapsulado em funções**. Obviamente existem algumas exceções a essa regra, que serão vistas ao longo do curso, conforme necessário. No entanto, para praticamente todas as nossas aplicações, vamos pensar em sempre agrupar os nossos algoritmos dentro de funções.

## Sintaxe de funções

Voltemos ao nosso caótico exemplo de cabeçalho de relatório. Podemos considerar um procedimento que execute esse algoritmo de cabeçalho da seguinte forma:

``` txt
PROCEDIMENTO cabecalho(titulo)
------------------------------
1. Escreva "-" 40 vezes na tela e pule uma linha.
2. Escreva titulo na tela e pule uma linha.
3. Escreva "-" 40 vezes na tela e pule uma linha.
4. Encerre o procedimento e retorne nada.
```

Precisamos traduzir esse algoritmo em pseudocódigo para Python. Para isso, consideramos a seguinte sintaxe básica de funções:

``` python
def nome_funcao(param1, param2, ...):
    <instruções>
```

A primeira linha de toda função é chamada de **assinatura da função**, e contém as seguintes informações:

* A palavra reservada `def`, de _define_, que indica ao interpretador que teremos, a partir de agora, uma definição de função;
* O nome da função, que deve seguir as mesmas regras de nomenclatura que as variáveis (letras minúsculas, não começar com números, utilizar `_` para separar palavras, etc.);
* Os parâmetros de entrada da função, separados por vírgulas;
* O caractere `:`, que indica que a assinatura da função foi encerrada e que, a partir de agora, todo código indentado (ou seja, deslocado para a direita), faz parte dessa função.

Abaixo da assinatura da função, devemos incluir todas as instruções necessárias para se implementar o algoritmo desejado. Observe que, necessariamente, toda instrução contida nesta função deve estar deslocada à direita da assinatura. De acordo com o [PEP-8](https://peps.python.org/pep-0008/), utilizamos quatro espaços em branco para indicar a indentação necessária.

No momento em que inserimos um código alinhado com a assinatura da função, o interpretador do Python deixa de considerar como parte da função. O interpretador espera pelo menos uma linha de código no bloco, portanto haverá um erro de sintaxe caso uma função seja declarada e não haja nenhum código a seguir. Podemos utilizar a palavra reservada `pass` para atuar como _placeholder_ enquanto não implementamos o código da função, como no exemplo abaixo:

``` python
def cabecalho():
    pass

# podemos continuar o código normalmente, sem esperar uma exceção.
```


o uso do `pass` é relativamente comum no desenvolvimento de códigos mais extensos em que, antes de pensarmos na implementação de cada algoritmo, tentamos "quebrar" o problema em problemas menores. Isso é uma ótima prática no desenvolvimento, que estimula quem está programando a separar e encapsular bem as ideias contidas na solução.

O uso do `:` para indicar o início de um novo bloco de código é comum a diversas instruções em Python, e não apenas às funções. Veremos esse uso, por exemplo, quando estivermos trabalhando com `if` e `while`. O comportamento do interpretador e as precauções que devemos tomar serão sempre as mesmas.

## Parâmetros

Na assinatura da função, entre os parâmetros incluímos os **parâmetros de entrada**, também chamados de **argumentos da função**. Esses parâmetros são variáveis especiais que são definidas no momento em que a função é chamada. Em Python, temos dois tipos principais de parâmetros: parâmetros posicionais e parâmetros-chave, que veremos a seguir.

Não há restrição técnica no número de parâmetros que cada função pode receber. O interpretador aceita de zero até 100 (ou mais) parâmetros. No entanto, é considerado uma boa prática que se utilize no máximo dois ou três argumentos por função. Um número elevado de argumentos na função pode indicar que ela está fazendo muita coisa, ou seja, o algoritmo implementado pode ser dividido em algoritmos menores. Outra possibilidade é que alguns parâmetros são análogos ou relacionados entre si, e poderiam estar agrupados em estruturas de dados apropriadas (como listas, dicionários ou mesmo classes).

### Parâmetros posicionais

Os parâmetros posicionais são declarados em uma ordem que deve ser seguida por quem está chamando a função. Todos os parâmetros posicionais precisam ser especificados para o correto funcionamento do código.

Considere nosso exemplo do cabeçalho. Um campo extremamente necessário para a execução deste algoritmo é o título que será usado no cabeçalho. Este título é particular a cada execução daquele algoritmo, então faz sentido que ele seja abordado como um parâmetro nesse problema. Portanto, a assinatura do nosso código, junto com a implementação do algoritmo, fica:

``` python
def cabecalho(titulo):
    print("-" * 40)
    print(titulo)
    print("-" * 40)
```

Dessa forma, sempre que precisarmos chamar esta função, basta passar como parâmetro o título do relatório, como nos exemplos abaixo:

``` python
cabecalho("Finanças")
cabecalho("Marketing")
cabecalho("Contábil")
```

Caso precisemos incluir um segundo parâmetro, como por exemplo o caractere usado na linha de separação do título, basta inseri-lo após o primeiro parâmetro, utilizando `,` para separá-los:

``` python
def cabecalho(titulo, sep):
    print(sep * 40)
    print(titulo)
    print(sep * 40)
```

Neste caso, precisaríamos rever os exemplos anteriores, incluindo um novo parâmetro que indique o separador. Não incluir este parâmetro vai trazer uma exceção do tipo `TypeError`, indicando que está faltando um argumento posicional.

``` python
cabecalho("Finanças", "-")
cabecalho("Marketing", "=")
cabecalho("Contábil", ".")
```

### Parâmetros-chave (ou _default_)

No nosso exemplo, vamos supor que o separador do título não costuma mudar com muita frequência. Por padrão, temos que adotar o caractere `-` mas, ocasionalmente, este caractere pode ser alterado, dependendo das circunstâncias em que a função seja chamada.

Nesses casos, é interessante estabelecer um valor pré-definido para o parâmetro. Dessa forma, não é necessário incluí-lo na chamada da função todas as vezes, apenas nos casos em que queremos adotar um valor diferente do padrão. Chamamos esse tipo de parâmetro de **parâmetro-chave** ou **parâmetro default**, e indicamos o valor pré-definido logo depois da declaração do parâmetro, utilizando o `=` como no exemplo abaixo:

``` python
def cabecalho(titulo, sep="-"):
    print(sep * 40)
    print(titulo)
    print(sep * 40)
```

Sendo assim, não precisamos indicar `sep` no momento em que chamamos a função. Podemos utilizar a função como abaixo:

``` python
cabecalho("Finanças")               # O interpretador considera sep como "-"
cabecalho("Marketing", "=")         # O interpretador considera sep como "="
cabecalho("Contábil", sep=".")      # Podemos indicar explicitamente que sep recebe "."
```

Caso seja necessário indicar o valor de um parâmetro-chave na chamada da função, o ideal é ser explícito e colocar como no exemplo acima, na chamada em que `titulo` recebe `"Contábil"`. Isso é indicado pois, ao contrário dos parâmetros posicionais, não é obrigatório a chamada dos parâmetros na mesma ordem em que eles forem declarados. Vamos supor, por exemplo, que precisemos incluir um novo parâmetro, que é a largura do relatório:

``` python
def cabecalho(titulo, sep="-", larg=40):
    print(sep * larg)
    print(titulo)
    print(sep * larg)
```

Para chamar a função `cabecalho()`, podemos usar um, dois ou três parâmetros, conforme o número de parâmetros-chave que formos utilizar. Caso não indiquemos os parâmetros-chave usados, o interpretador vai atribui-los da esquerda para a direita, como se fossem parâmetros posicionais. No entanto, se só quisermos mudar o valor de `larg`, precisaremos necessariamente incluir o nome do parâmetro na chamada da função.

``` python
cabecalho("Finanças", larg=50)
cabecalho("Marketing", "=")
cabecalho("Contábil", sep=".")
```

Como boa prática, portanto, recomenda-se sempre explicitar o parâmetro-chave que deve ser atribuído, como no primeiro e no terceiro exemplos, e deve-se evitar o uso do segundo exemplo.

**Importante:** os parâmetros-chave devem **sempre** ser declarado após os parâmetros posicionais! Inverter esses parâmetros faz subir um erro de sintaxe!

## Saída ou retorno

Vamos pensar agora em outro exemplo. Precisamos montar uma função que realize a soma de dois números, `a` e `b`. Com o temos de conhecimento até então, o natural é declarar algo do tipo:

``` python
def soma(a, b):
    print(a + b)
```

Até aqui, parece que está tudo certo com a função. Estamos exibindo na tela o resultado da soma de dois números. No entanto, considere agora esse possível cenário de uso dessa função:

``` python
resultado = soma(2, 4) + soma(1, 3)
```

Se você rodar os dois blocos de código anteriores, encontrará uma exceção do tipo `TypeError`, dizendo que o operador `+` é incompatível com o tipo `NoneType`. Isso acontece porque, assim como nos procedimentos, toda função retorna alguma coisa, ou seja, a função precisa devolver alguma informação para quem a chamou.

Por padrão, toda função em Python retorna o dado `None` quando é chamada. Para alterar o tipo de retorno da função, deve-se usar a instrução `return`, como no caso abaixo:

``` python
def soma(a, b):
    return a + b
```

Neste último exemplo, quando a função soma for somada, ao invés de retornar `None` ela retornará o valor da operação de soma de `a` com `b`, como é o esperado para uma função desse tipo. Sendo assim, conseguimos utilizá-la normalmente em outros algoritmos que precisem realizar uma operação de soma.

O uso do `return` não implica que devemos "abolir" o uso do `print()` dos nossos códigos. O `print()` é muito útil quando queremos exibir alguma informação para o usuário, como em um relatório ou em um log de alterações realizadas pelo algoritmo. No entanto, quando queremos que a função realize algum processamento que será usado pelo próprio código, devemos retornar essas informações.

Funções podem retornar mais de um valor. Separamos os valores a serem retornados por vírgulas, e podemos atribuir diretamente para duas ou mais variáveis diferentes. Nesse caso, todos os valores a serem retornados formam uma **tupla**, uma estrutura de dados que ainda veremos no futuro. No momento, basta saber que esse tipo de retorno é possível.

``` python
def inverte(x, y):
    """Inverte dois valores."""
    return y, x

x, y = inverte(x, y)
```

## Documentando funções

Assim como vimos na [nota de aula de introdução ao Python](003-intro-python.md), precisamos documentar corretamente as funções que criamos. Para isso, utilizamos _docstrings_, como fazemos no início de um novo arquivo. Este recurso é necessário para facilitar o uso da função por outros programadores (ou até por nós mesmos) e evitar o seu mau uso.

É recomendado que se inclua o máximo de informação possível, obviamente tentando manter uma concisão e um nível de detalhamento proporcional à complexidade da função. A nossa função `soma()`, por exemplo, poderia ficar dessa forma:

``` python
def soma(a, b):
    """Soma os valores a e b."""
    return a + b
```

Já a nossa função `cabecalho()`, mais complexa, poderia ter um pouco mais de detalhe:

``` python
def cabecalho(titulo, sep="-", larg=40):
    """
    Exibe na tela um cabeçalho para relatório.

    Parâmetros:
    titulo - o título a ser exibido no relatório
    sep    - o caractere separador do título no relatório (padrão "-")
    larg   - a largura de caracteres do relatório (padrão 40)

    Retorna: None
    """
    print(sep * larg)
    print(titulo)
    print(sep * larg)
```

Veja que essa função ficou muito mais clara para quem está lendo a documentação e tentando implementar uma atualização no software. Alguns IDEs, inclusive, "leem" as _docstrings_ e exibem para quem está programando, explicando de forma rápida o que a função faz.

Recomendo que vocês já comecem, desde o início, a documentar suas funções. Quando chegarmos a projetos mais complexos, será nítida a percepção da necessidade de utilizar esse instrumento no nosso dia-a-dia.

## Exercícios resolvidos

Para a resolução dos exercícios, consulte a página de [gabaritos](./000-gabaritos_exercicios.md).

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

## Exercícios complementares

1. Monte uma função que recebe um salário por hora e o número de horas trabalhadas no mês, e retorne o salário a ser recebido.
2. Elabore uma função que receba três números e exiba na tela: (1) o produto do dobro do primeiro com metade do segundo; (2) a soma do triplo do primeiro com o terceiro; e (3) o terceiro elevado ao cubo.
3. Elabore uma função com as mesmas regras do exercício anterior, porém retornando os três resultados, ao invés de exibi-los na tela.
4. João Papo-de-Pescador, homem de bem, comprou um computador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça uma função que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. REtorne o valor da multa. Assumir que a quantidade de quilos é sempre superior a 50.
5. Faça um programa que receba dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

## Sugestões de conteúdos

* Material online:
  * [Este vídeo](https://www.youtube.com/watch?v=ezfr9d7wd_k) e [sua continuação](https://www.youtube.com/watch?v=etjJ_4Eqrk8) com mais informações sobre funções;
  * [Este tutorial](https://www.datacamp.com/community/tutorials/functions-python-tutorial?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=dsa-473406571355&utm_loc_interest_ms=&utm_loc_physical_ms=9100825&gclid=CjwKCAjwi6WSBhA-EiwA6Niokzq9bNPhCoWO4gieeatzvGc9lGNL7vTtGmWrGlW_7lpNI55NR1qgahoCT1IQAvD_BwE) sobre funções.
