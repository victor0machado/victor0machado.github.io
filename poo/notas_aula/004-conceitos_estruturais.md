# Conceitos estruturais

Embora a OO tenha vantagens em relação aos paradigmas que a precederam, existe uma desvantagem inicial: ser um modo mais complexo e difícil de se pensar. Isso pode ser atribuído à grande quantidade de conceitos que devem ser assimilados para podermos trabalhar orientado a objetos. Nesta nota de aula, vamos trazer o primeiro grupo de conceitos específicos do POO, chamados de estruturais.

### Índice

1. [A classe](#a-classe)
2. [O atributo](#o-atributo)
3. [O método](#o-método)
4. [O objeto](#o-objeto)
5. [Os tipos de atributo e método](#os-tipos-de-atributo-e-método)
6. [A mensagem](#a-mensagem)
7. [Exercícios complementares](#exercícios-complementares)

## A classe

O paradigma que está sendo estudado é o Paradigma Orientado a Objeto (POO). Embora se tenha o termo "objeto" presente nessa denominação, tudo começa com a definição de uma classe.

Antes mesmo de ser possível manipular objetos, é preciso definir uma classe, pois esta é a unidade inicial e mínima de código na OO. É a partir de classes que futuramente será possível criar objetos.

> _"Classe é uma estrutura que abstrai um conjunto de objetos com características similares. Uma classe define o comportamento de seus objetos através de métodos e os estados possíveis destes objetos através de atributos. Em outros termos, uma classe descreve os serviços providos por seus objetos e quais informações eles podem armazenar."_

O objetivo de uma classe é definir, servir de base, para o que futuramente será o objeto. É através dela que criamos o "molde" aos quais os objetos deverão seguir. Este "molde" definirá quais informações serão trabalhadas e como elas serão manipuladas.

A classe é a forma mais básica de se definir apenas uma vez como devem ser todos os objetos criados a partir dela, em vez de dfinir cada objeto separadamente e até repetidamente. A partir disto, logo percebemos que o conceito de classe é fundamental para a aplicação da abstração. Assim, uma classe também pode ser definida como uma abstração de uma entidade, seja ela física (bola, pessoa, carro, etc.) ou conceitual (viagem, venda, estoque, etc.) do mundo real.

É através de criação de classes que se conseguirá codificar todas as necessidades de um sistema. Mas como será possível identificar as necessidades, entidades, de um software? Um bom ponto de partida é pensar em substantivos. Estes são responsáveis por nomear tudo o que conhecemos, então é a partir deles que se possibilitará identificar quais as entidades um software terá de modelar.

Por exemplo, imagine que precisamos desenvolver um site de vendas online. Assim, aparecerão entidades como `Venda`, `Cliente`, `Fornecedor`, `Produto`, entre outras. Vemos que todos estes substantivos fazem parte do contexto de um site de vendas como esse. Logo, é possível especificar (codificar) classes, para assim manipular tais entidades.

Mas como devemos chamar, nomear as classes? Seu nome deve representar bem sua finalidade dentro do contexto ao qual ela foi necessária. Por exemplo, em um sistema de controle hospitalar, podemos ter uma classe chamada `Pessoa` para representar quem está hospitalizado ou apenas sendo consultado. Já em um sistema de pondo de vendas (PDV), temos mais uma vez o conceito de `Pessoa`, que neste caso é quem está comprando os produtos.

A partir disto, é possível termos classes nestes sistemas com estas definições. Entretanto, nota-se que o termo _pessoa_ pode gerar uma ambiguidade, embora esteja correto. No hospital, também existem os médicos, enfermeiros; e no supermercado, gerentes e vendedores. Todos são pessoas.

Assim, muito melhor seria definir a classe `Paciente` no hospital e, no PDV, `Cliente`, além de `Médico`, `Vendedor`, respectivamente. Todos estes são pessoas, mas dentro de cada contexto eles representam papéis diferentes, então, para melhorar o entendimento e a representatividade, seria melhor mudar seus nomes.

Embora possa parecer preciosismo, classes com nomes pobremente definidos podem dificultar o entendimento do código e até levar a erros de utilização. Pense bem antes de nomear uma classe.

A sintaxe básica para criação de classes é com a instrução `class`. Para nomes de classes, convenciona-se iniciar por letras maiúsculas, para diferenciá-las de variáveis, atributos e métodos. Utilizam-se chaves após a declaração da classe, para indicar o início de bloco. Por fim, utilizaremos nesse momento a palavra-chave `public` antes da classe. Ela trata da visibilidade da classe frente ao projeto. Mais à frente no curso veremos que não se deve utilizar esta palavra-chave em todos os casos, mas por enquanto lidaremos apenas com classes públicas.

Em Java, normalmente utilizamos um arquivo .java para cada classe. Tanto o arquivo quanto a classe possuem o mesmo nome. Consideremos, por exemplo, um sistema bancário. Conseguimos indicar, de imediato, duas classes, `Cliente` e `Conta`. Uma classe `Cliente`, portanto, seria armazenada em um arquivo `Cliente.java`, e seria declarada da seguinte forma:

``` java
public class Cliente {

}
```

Já a classe `Conta` seria armazenada em um arquivo `Conta.java`, na mesma pasta de `Cliente.java`, e seria declarada como:

``` java
public class Conta {

}
```

## O atributo

Após o processo inicial de identificar as entidades (classes) que devem ser manipuladas, começa a surgir a necessidade de detalhá-las. A primeira coisa que vem à mente é: quais informações devem ser manipuladas através desta classe? A partir disto, começa-se a tarefa de caracterizá-las. Essas características é que vão definir quais informações as classes poderão armazenar e manipular. Na OO, estas características e informações são denominadas de **atributo**.

> _Atributo é o elemento de uma classe responsável por definir sua estrutura de dados. O conjunto destes será responsável por representar suas características e fará parte dos objetos criados a partir da classe._

Essa definição deixa bem claro que os atributos devem ser definidos dentro da classe. Devido a isso, são responsáveis por definir sua estrutura de dados. É a partir do uso de atributos que será possível caracterizar (detalhar) as classes, sendo possível representar fielmente uma entidade do mundo real.

Assim como nas classes, os atributos podem ser representados a partir de substantivos. Além destes, podemos também usar adjetivos. Pensar em ambos pode facilitar o processo de identificação dos atributos.

Por exemplo, imagine que a entidade `Paciente` foi identificada para o sistema hospitalar. Alguns de seus atributos podem ser nome, CPF, sexo. Todos estes são substantivos, mas alguns de seus valores poderiam ser adjetivos. Quanto mais for realizado o processo de caracterização, mais detalhada será a classe e, com isso, ela terá mais atributos. Porém, é preciso ter parcimônia no processo de identificação dos atributos.

Embora um atributo possa pertencer à classe, nem sempre fará sentido ele ser definido. Isso ocorre devido ao **contexto** no qual a classe vai ser usada. Por exemplo, foi visto anteriormente que `Paciente` não deixa de ser uma `Pessoa`, e geralmente elas possuem um hobby. Porém, em um contexto hospitalar, este atributo não agregaria muito valor. Já em `Cliente` - que também é uma pessoa - seria mais interessante, pois a partir de seu hobby poderiam ser apresentados produtos que lhe interessassem mais. Percebe-se, com isso, que o contexto de uso da classe vai impactar diretamente no processo de definição de seus atributos.

Ainda no processo de identificação e criação dos atributos, é válido ressaltar que nem sempre uma informação, mesmo sendo importante (uma característica inerente à entidade), deve ser transformada em um atributo. Um exemplo clássico disso é a idade. Embora essa seja uma característica válida e importante para uma pessoa, seja ela um `Paciente` ou `Cliente`, devido ao trabalho de mantê-la atualizada (todo ano fazemos aniversário), não valeria a pena criá-la.

Neste caso, seria melhor usar o que é conhecido como _atributo calculado_ ou _atributo derivado_. A idade não se torna um atributo em si, mas tem seu valor obtido a partir de um método (ainda será explicado o que vem a ser um método mais à frente). Assim, a idade de um paciente poderia ser calculada a partir da data atual menos a data de nascimento, essa sim um atributo da classe `Paciente` ou `Cliente`.

Não diferentemente de linguagens estruturadas, um atributo possui um tipo. Como sua finalidade é armazenar um valor que será usado para caracterizar a classe, ele precisará identificar qual o tipo do valor armazenado em si. Linguagens orientadas a objetos proveem os mesmos tipos de dados básicos - com pequenas variações - que suas antecessoras.

A nomeação de atributos deve seguir a mesma preocupação das classes: deve ser o mais representativo possível. Nomes como `qtd`, `vlr` devem ser evitados. Esses nomes eram válidos na época em que as linguagens de programação e os computadores que as executavam eram limitados, portanto deveríamos sempre abreviar os nomes das variáveis. Entretanto, atualmente não temos essa limitação, e os editores modernos possuem recursos para reaproveitar nomes de atributos e variáveis sem precisar digitar tudo novamente. Portanto, não deixe a preguiça lhe dominar e escreva `quantidade` e `valor`.

Utilize nomes claros. Evite, por exemplo, o atributo `data`. Uma data pode significar várias coisas: nascimento, morte, envio de um produto, cancelamento de venda. Escreva exatamente o que se deseja armazenar nesse atributo: `dataNascimento`, `dataObito`, etc.

Todos os atributos da classe devem ser declarados logo no topo. A sintaxe é a mesma da declaração de variáveis, incluindo-se o tipo do dado antes de seu nome. Não é necessário utilizar apenas tipos primitivos ou strings para atributos. É possível definir atributos como sendo instâncias de outras classes (ou objetos, como veremos adiante).

Seguindo nosso exemplo de sistema bancário, para a classe `Cliente` poderíamos ter informações como `nome`, `sobrenome`, `cpf` e `endereco`, todas do tipo `String`. Já a classe `Conta` poderia ser composta de `numero` (tipo `int`), `titular` (tipo `Cliente`), `agencia` (tipo `String`) e `saldo` (tipo `double`).

``` java
public class Cliente {
    String nome;
    String sobrenome;
    String cpf;
    String endereco;
}
```

``` java
public class Conta {
    int numero;
    Cliente titular;
    String agencia;
    double saldo;
}
```

## O método

Tendo identificado a classe com seus atributos, as seguintes perguntas podem surgir: mas o que fazer com eles? Como utilizar a classe e manipular os atributos? É nessa hora que o método entra em cena. Este é responsável por identificar e executar as operações que a classe fornecerá. Essas operações, via de regra, têm como finalidade manipular os atributos.

_Método é uma porção de código (sub-rotina) que é disponibilizada pela classe. Esta é executada quando é feita uma requisição a ela. Um método serve para identificar quais serviços, ações, que a classe oferece. Eles são responsáveis por definir e realizar um determinado comportamento._

Para facilitar o processo de identificação dos métodos de uma classe, podemos pensar em verbos. Isso ocorre devido à sua própria definição: _ações_. Ou seja, quando se pensa nas ações que uma classe venha a ofereces, estas identificam seus métodos.

No processo de definição de um método, a sua assinatura deve ser identificada. Esta nada mais é do que o nome do método e sua lista de parâmetros. Mas como nomear os métodos? Novamente, uma expressividade ao nome do método deve ser fornecida, assim como foi feito com o atributo.

Por exemplo, no contexto do hospital, imagine termos uma classe `Procedimento`, logo, um péssimo nome de método seria `calcular`. Calcular o quê? O valor total do procedimento, o quanto cada médico deve receber por ele, o lucro do plano? Neste caso, seria mais interessante `calcularTotal`, `calcularGanhosMedico`, `calcularLucro`.

Veja que, ao lermos esses nomes, logo de cara já sabemos o que cada método se propõe a fazer. Já a lista de parâmetros são informações auxiliares que podem ser passadas aos métodos para que estes executem suas ações. Cada método terá sua lista específica, caso haja necessidade. Esta é bem livre e, em determinados momentos, podemos não ter parâmetros, como em outros podemos ter uma classe passada como parâmetro, ou também tipos primitivos e classes ao mesmo tempo.

Há também a possibilidade de passarmos somente tipos primitivos, entretanto, isto remete à programação procedural e deve ser desencorajado. Via de regra, se você passa muitos parâmetros separados, talvez eles pudessem representar algum conceito em conjunto. Neste caso, valeria a pena avaliarmos se não seria melhor criar uma classe para aglutiná-los.

Por fim, embora não faça parte de sua assinatura, os métodos devem possuir um retorno. Se uma ação é disparada, é de se esperar uma reação. O retorno de um método pode ser qualquer um dos tipos primitivos vistos na seção sobre atributos.

Além destes, o método pode também retornar qualquer um dos conceitos (classes) que foram definidos para satisfazer as necessidades do sistema em desenvolvimento, ou também qualquer outra classe - não criada pelo programador - que pertença à linguagem de programação escolhida.

Continuando nosso exemplo, a classe `Cliente` precisaria ter um método que indicasse as informações contidas na classe, que poderíamos chamar de `exibirInfoCliente`. Já a classe `Conta` poderia ter mais algumas operações, como `sacar`, `depositar`, `transferir`, `consultarSaldo`, `exibirInfoConta`.

Como sintaxe de métodos, utilizamos a estrutura `[<tipoVisibilidade>] <tipoRetorno> <nomeMetodo>([<param1>, <param2>, ...])`. O campo `tipoVisibilidade`, por enquanto, não será usado (com exceção dos métodos construtores, que veremos a seguir). Assim como funções na programação estruturada, métodos devem retornar outros dados. Caso o método não retorne nada, o campo `<tipoRetorno>` deve ser `void`.

Por fim, utilizamos os atributos e métodos da classe através da palavra-chave `this` antecedendo o nome da entidade. Isso serve para diferenciar o que é atributo e método da classe do que é uma entidade que não faz parte necessariamente da classe.

``` java
public class Cliente {
    String nome;
    String sobrenome;
    String cpf;
    String endereco;

    String exibirInfoCliente() {
        return this.cpf + " - " + this.nome + " " + this.sobrenome;
    }
}
```

``` java
public class Conta {
    int numero;
    Cliente titular;
    String agencia;
    double saldo;

    void sacar(double quantidade) {
        this.saldo -= quantidade;
    }

    void depositar(double quantidade) {
        this.saldo += quantidade;
    }

    void transferir(double quantidade, Conta destino) {
        this.sacar(quantidade);
        destino.depositar(quantidade);
    }

    double consultarSaldo() {
        return this.saldo;
    }

    String exibirInfoConta() {
        String mensagem;

        mensagem = "Conta n. " + this.numero + "\n";
        mensagem += "Agencia n. " + this.agencia + "\n";
        mensagem += "Titular: " + this.titular.exibirInfoCliente() + "\n";

        // Usamos o método String.format() para formatar valores numéricos
        mensagem += "Saldo atual: R$" + String.format("%.2f", this.saldo);

        return mensagem;
    }
}
```

### Dois métodos especiais

Em uma classe, independente de qual conceito ela queira representar, podemos ter quantos métodos forem necessários. Cada um será responsável por uma determinada operação que a classe deseja oferecer. Muitas vezes, os métodos trabalham em conjunto para realizar seus comportamentos. Além disso, independente da quantidade e da finalidade dos métodos de uma classe, existem dois especiais que toda classe possui: o construtor e o destrutor.

O construtor é responsável por criar objetos - na seção _O objeto_, será visto como é este processo de criação - a partir da classe em questão. Ou seja, sempre que for necessário criar objetos de uma determinada classe, seu construtor deverá ser utilizado. É através do seu uso que será possível instanciar objetos e, a partir disto, manipular de forma efetiva seus atributos e métodos.

Além disto, uma outra função do construtor é prover alguns valores iniciais que o objeto precisa ter inicialmente. O nome do método construtor é idêntico ao da classe. Diferentemente de outros métodos, no entanto, o construtor é "sem retorno", ou seja, não devolve nenhum dado para a instrução que a chamou. No caso de Java, para construtores é necessário omitir inclusive o tipo `void` na assinatura do método.

Muitas linguagens, incluindo Java e C#, possuem construtores implícitos. Ou seja, mesmo se os programadores não definirem um construtor para a classe, ele estará disponível. Por padrão, o construtor implícito tem como assinatura o mesmo nome da classe e sem parâmetros.

Já o destrutor tem a função inversa: destruir o objeto criado a partir da classe. Ou seja, sempre que não precisarmos mais de objetos que foram criados a partir de uma determinada classe, devemos usar seu destrutor. É através do seu uso que poderemos eliminar os objetos criados.

Ao contrário do construtor, o destrutor em Java possui uma sintaxe bem diferente: chama-se `finalize` e usa-se o `void`. Além disso, o destrutor não possui parâmetros.

A ideia por detrás desse processo de eliminação dos objetos é liberar possíveis recursos que ele teve de se apoderar para realizar suas atividades, além de também simplesmente eliminá-lo. Por exemplo, imagine um objeto criado a partir de uma classe que represente uma impressora. Provavelmente, precisaremos reservar para ele uma porta serial ou USB. Assim, será possível realizar a comunicação entre a impressora e o computador. Com isso, as aplicações poderão realizar impressões.

Entretanto, se essa porta não for liberada em momento algum, ela ficará alocada indefinidamente a este objeto, mesmo quando não estiverem sendo realizadas mais impressões. Então, seria uma boa prática liberar essa porta quando o objeto não for mais necessário, ou seja, quando ele puder ser destruído. Neste caso, nada mais apropriado do que liberar esse recurso no destrutor. Para finalizar, a mesma ideia de implícito dos construtores aplica-se aos destrutores.

Portanto, caso haja necessidade, devemos definir os destrutores para nossas classes e nossos futuros objetos. No entanto, não devemos usá-los diretamente. Isto não é proibido, mas também não é uma boa prática. Na verdade, mesmo se os usarmos diretamente, ainda não teremos a certeza de que, no exato momento de seu uso, o objeto será eliminado.

Isso ocorre devido a uma funcionalidade que as linguagens orientadas a objetos proveem: o Garbage Collector. Este é responsável por automaticamente identificar objetos que não mais estão sendo usados e eliminá-los. É neste processo de eliminação que o Garbage Collector usa os destrutores. Este procedimento de gerenciamento de objetos surgiu em Smalltalk 80 e é usado em linguagens que surgiram depois, por exemplo, Java e C#.

O Garbage Collector possui algoritmos de identificação de objetos ociosos que, com certeza, farão um ótimo trabalho para nós, eliminando os objetos não mais usados. Esta facilidade mais uma vez reforça o sentido da OO: facilitar o processo de desenvolvimento. Em linguagens como C, temos de nos preocupar em liberar a memória com comandos do tipo `free`.

Continuando o exemplo das classes `Cliente` e `Conta`, podemos trabalhar com os seguintes métodos construtores. Novamente, vamos usar o modificador de visibilidade `public` antes do construtor. Ao longo do curso veremos outros tipos de visibilidade.

``` java
public class Cliente {
    String nome;
    String sobrenome;
    String cpf;
    String endereco;

    public Cliente(String nome, String sobrenome, String cpf, String endereco) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.cpf = cpf;
        this.endereco = endereco;
    }

    String exibirInfoCliente() {
        return this.cpf + " - " + this.nome + " " + this.sobrenome;
    }
}
```

``` java
public class Conta {
    int numero;
    Cliente titular;
    String agencia;
    double saldo;

    public Conta(int numero, Cliente titular, String agencia) {
        this.saldo = 0;
        this.numero = numero;
        this.agencia = agencia;
        this.titular = titular;
    }

    // métodos
}
```

### A sobrecarga de método

Muitas vezes, é preciso que um mesmo método possua entradas (parâmetros) diferentes. Isso ocorre porque ele pode precisar realizar operações diferentes em determinado contexto. Este processo é chamado de *sobrecarga de método*.

Para realizá-la, devemos manter o nome do método intacto, mas alterar sua lista de parâmetros. Podem ser acrescentados ou retirados parâmetros para assim se prover um novo comportamento. Por exemplo, se uma determinada aplicação tivesse uma classe para representar um quadrilátero, ela deveria se chamar `Quadrilátero` e possuir o método `calcularArea`, seguindo as boas práticas já citadas. Mas sabemos que um quadrado, retângulo, losango e trapézio também são quadriláteros.

Mais interessante do que possuir um método para cada figura (`calcularAreaQuadrado`, `calcularAreaLosango`, etc.) é definir o mesmo método `calcularArea` com uma lista de parâmetros que se adeque a cada um desses quadriláteros. A seguir, veja um exemplo da abordagem:

``` java
class Quadrilatero {
    // área do quadrado
    double calcularArea(double lado) {
        return lado * lado;
    }

    // área do retângulo
    double calcularArea(double baseMaior, double baseMenor) {
        return baseMaior * baseMenor;
    }

    // área do trapézio
    double calcularArea(double baseMaior, double baseMenor, double altura) {
        return ((baseMaior * baseMenor) * altura) / 2;
    }

    // área do losango
    double calcularArea(float diagonalMaior, float diagonalMenor) {
        return diagonalMaior * diagonalMenor;
    }
}
```

No exemplo acima, a quantidade de parâmetros (nos 3 primeiros métodos) e os tipos (no último método) foram alterados. Isso demonstra que, caso haja necessidade, os tipos também podem ser mudados. Se fosse preciso que o cálculo das áreas só fosse feito a partir de medidas inteiras, nada impediria que os tipos `double` ou `float` fossem trocados por `int` ou `long`. Neste caso, seriam outras sobrecargas para o método `calcularArea`.

Ou seja, sempre que a lista de parâmetros muda - seja acrescentando ou eliminando parâmetros, mudando seus tipos e até mesmo sua sequência -, estaremos criando sobrecargas de um método. Mas lembre-se de que o nome dele deve permanecer intacto.

A vantagem de usar a sobrecarga não se limita à "facilidade" de se manter o mesmo nome do método. Na verdade, existe uma questão conceitual, que é manter a abstração. Como exploramos por aqui, a OO surgiu para representar de forma mais realista e fidedigna as necessidades que devem ser transportadas para dentro do software.

Assim, no caso de nosso exemplo do quadrilátero, a abstração é calcular sua área, independente de sua real forma. Deste modo, a sobrecarga possibilitou que tal cálculo pudesse receber os devidos parâmetros de acordo com a sua necessidade - no caso, a forma do quadrilátero - e, mesmo assim, manteve-se a abstração-alvo, que é calcular a área.

Para a classe `Cliente`, vamos criar uma sobrecarga do construtor, para iniciar um cliente "vazio":

``` java
public class Cliente {
    String nome;
    String sobrenome;
    String cpf;
    String endereco;

    public Cliente() {
        this.nome = "N/A";
        this.sobrenome = "N/A";
        this.cpf = "N/A";
        this.endereco = "N/A";
    }

    public Cliente(String nome, String sobrenome, String cpf, String endereco) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.cpf = cpf;
        this.endereco = endereco;
    }

    String exibirInfoCliente() {
        return this.cpf + " - " + this.nome + " " + this.sobrenome;
    }
}
```

## O objeto

Embora o nome do paradigma que está sendo estudado seja a Orientação a Objeto, já tínhamos visto que tudo começa com a definição de uma classe. Então, o que é um objeto? É a instanciação de uma classe.

Como já explicado, a classe é a abstração base a partir da qual os objetos serão criados. Quando se usa a OO para criar um software, primeiro pensamos nos objetos que ele vai manipular/representar. Tendo estes sido identificados, devemos então definir as classes que serviram de abstração base para que os objetos venham a ser criados (instanciados).

> _Um objeto é a representação de um conceito/entidade do mundo real, que pode ser física (bola, carro, árvore, etc.) ou conceitual (viagem, estoque, compra, etc.) e possui um significado bem definido para um determinado software. Para esse conceito/entidade, deve ser definida inicialmente uma classe a partir da qual posteriormente serão instanciados objetos distintos._

Contextualizando melhor, imagine que temos um software de Fluxo de Caixa, logo, um conceito que teria de manipular seria uma _conta_. Então, deveríamos criar uma classe chamada `Conta` e, a partir dela, seriam criados objetos que representariam uma _Conta de Água_, _Conta de Energia_, _Conta de Telefone_, entre outros. Cada um teria seus respectivos atributos e métodos, como: total a ser pago, empresa que fornece tal serviço, verificar pagamento, calcular multa, etc.

A partir disto, percebemos que, no processo de identificação dos conceitos/entidades que são necessários para o software se tornar operante, primeiro devemos identificar os objetos em um alto nível de pensamento. Somente após este processo é que as classes com seus atributos e métodos são definidas para abstrair esses objetos e, finalmente, criar cada objeto distinto a partir da classe definida.

Instanciamos um novo objeto de uma classe utilizando a instrução `new`. Por exemplo, vamos realizar uma sobrecarga no construtor de `Conta` para criar uma conta vazia:

``` java
public class Conta {
    int numero;
    Cliente titular;
    String agencia;
    double saldo;

    public Conta() {
        this.saldo = 0;
        this.numero = 0;
        this.agencia = "Sem agência";
        // Instanciando um cliente novo
        this.titular = new Cliente();
    }

    public Conta(int numero, Cliente titular, String agencia) {
        this.saldo = 0;
        this.numero = numero;
        this.agencia = agencia;
        this.titular = titular;
    }

    // métodos
}
```

### A identidade (igualdade) de um objeto

Por definição, todo objeto é único. Se tivermos uma classe e forem criados dois objetos a partir dela, cada um será diferente do outro, mesmo que seus estados sejam iguais por coincidência. Porém, cada sistema terá necessidades específicas para definir o que torna um objeto igual a outro. Devido a isso, a identidade ou a igualdade de objetos deve ser definida por quem criou a classe, pois só este tem o conhecimento do contexto em questão para poder determinar o que torna dois objetos iguais.

Poder determinar se dois objetos são iguais é de grande utilidade em sistemas, pois se uma das premissas deles é automatizar um processo do mundo real, nada melhor do que poder prover facilidades que agilizem a execução das atividades. Por exemplo, imagine um estoque de uma loja de eletrodomésticos. Se um funcionário precisar encontrar um determinado produto em um processo manual ele dirigiria ao estoque e visualmente procuraria estante por estante, prateleira por prateleira.

Entretanto, se existir um software, ele pode digitar o nome ou tipo de eletrodoméstico que deseja encontrar. Assim, uma varredura automática será feita e eliminará uma grande quantidade de itens que não são iguais aos que ele deseja achar. Especificando mais, se ele deseja encontrar um aparelho de blu-ray, não teria lógica ter de ir a estantes de sons, TVs, etc.

Mas como ele saberia especificamente a estante e a prateleira onde se encontram os aparelhos de blu-ray? A identidade ou a igualdade pode ajudar nisso. Neste caso, ele usaria um objeto que representasse seus parâmetros de pesquisa para assim agilizar o processo. Mas o que tornaria seu objeto de pesquisa igual ao objeto que deseja encontrar?

Mais uma vez, quem definiu a classe é que tem como determinar isso. No exemplo do blu-ray, poderíamos colocar o tipo de aparelho e o modelo. Assim, a igualdade seria determinada pelos atributos que armazenassem esses valores.

Para poder efetivamente verificar se um objeto é igual ao outro, devemos utilizar um método, pois, como já vimos, são estes os responsáveis por definirem os comportamentos, ações das classes/objetos e, neste caso, o comportamento que torna dois objetos iguais. Ainda no exemplo do blu-ray, o método verificaria se o tipo de aparelho e o modelo são iguais a alguns do estoque. Em caso positivo, seria informada a localização deles dentro do estoque, e assim o vendedor iria diretamente ao local para pegar o produto do cliente.

Em Java, existe um método específico para determinar se dois objetos são iguais: o `equals`. Como a função deste é determinar se dois objetos são iguais, nada mais óbvio que ele retornar um booleano. É importante ressaltar que não devemos usar o operador `==` para comparação entre objetos, já que este verifica se os dois membros da operação estão apontando para o mesmo lugar na memória do computador.

No momento não veremos como implementamos um método `equals`, pois ele exige alguns conceitos que herança que não vimos. No momento, basta compreender que a operação de igualdade (`==`) **não é válida** para comparar tipos de dados não-primitivos (inclusive dados do tipo `String`).

## Os tipos de atributo e método

Só após os conceitos de classe e objeto serem explicados é que é possível apresentar os dois tipos de atributos e métodos. Ambos podem ser de instância ou estático.

Os atributos de instância, embora definidos na classe, pertencem ao objeto. Ou seja, só poderão ser acessados/usados a partir de instâncias de uma classe (no caso, um objeto). Com isso, cada um pode ter valores distintos para seus atributos e assim conseguir armazenar os valores que necessitam.

Por exemplo, se em uma classe chamada `Pessoa` existir um atributo de instância chamado `nome`, poderemos criar dois objetos e cada um ter um valor em particular para esse atributo. No caso, poderíamos ter um objeto com o valor "Isadora" para seu atributo `nome`, e um outro objeto com o valor "Lorena" para seu atributo `nome`.

Caso uma coincidência ocorresse, esses dois objetos distintos até poderiam ter o mesmo valor para o `nome`, mas mesmo assim cada valor pertenceria isoladamente a cada objeto. Por padrão, todo atributo é de instância e, para defini-los desta forma, basta criar os atributos normalmente.

O atributo estático pertence à classe, e não ao objeto. Atributos deste tipo devem ser acessados/usados diretamente a partir da classe. Podem até ser acessados/usados via o objeto, mas isso não é uma boa prática e deve ser desencorajado.

Devido ao comportamento de pertencer à classe e não ao objeto, ele se comporta de forma oposta ao de instância: valores armazenados neles são iguais em todos os objetos criados a partir da classe, pois eles pertencem a ela antes mesmo de existir um objeto. Devido a isso, objetos distintos terão o mesmo valor para esse determinado atributo.

Por exemplo, uma classe `Carro` poderia ter um atributo chamado `numeroRodas`. Independente de qualquer objeto criado, esse valor sempre será 4. Podemos ter diferentes objetos a partir de carro, cada um tem valores específicos de `modelo` e `cor`, por exemplo, mas todos possuem quatro rodas. Então, o atributo `numeroRodas` poderia ser estático.

Iniciando as explicações sobre o método, o de instância (assim como o atributo) é definido na classe, mas é acessado/usado via o objeto. Ou seja, sua execução só poderá ser requisitada por meio de um objeto.

Por natureza, o método não armazena valores e sim executa uma ação. Então, mesmo pertencendo a objetos distintos, o comportamento será o mesmo. A única questão é que ele só pode ser requisitado através de um objeto. Por padrão, todo método é de instância.

Já o método estático pertence à classe, e não ao objeto, ou seja, deve ser acessado diretamente através da classe. Mais uma vez, ele executa uma ação e ela será a mesma independente do objeto, já que, antes mesmo de pertencer ao objeto, o método já pertencia à classe.

Para se criar atributos ou métodos estáticos, utiliza-se a palavra-chave `static` entre o modificador de visibilidade e o tipo do atributo ou do retorno do método. Considere, por exemplo, uma classe `Quadrado`:

``` java
public class Quadrado {
    static int numeroLados = 4;
}
```

O uso de atributos e métodos estáticos, como mencionado, é feito a partir da classe, e não a partir das instâncias dos objetos. Portanto, uma chamada do atributo `numeroLados` poderia ser:

``` java
class Main {
    public static void main(String[] args) {
        System.out.println(Quadrado.numeroLados);
    }
}
```

## A mensagem

> _Mensagem é o processo de ativação de um método de um objeto. Isto ocorre quando uma requisição (chamada) a esse método é realizada, assim disparando a execução de seu comportamento descrito por sua classe. Pode também ser direcionada diretamente à classe, caso a requisição seja a um método estático._

A definição anterior deixa bem claro que, quando requisitamos que um comportamento (código) de um método seja executado, estamos passando uma mensagem a esse método. Mensagens podem ser trocadas entre métodos dos objetos/classes, para serem realizadas as atividades inerentes a cada um.

É de se esperar que trocas de mensagens ocorram de forma livre e constante durante a execução de um sistema. Só assim os objetos/classes poderão executar suas tarefas. Se durante a execução de um sistema for detectado que certos métodos nunca terão mensagens passadas a eles, vale a pena refletir sobre a real necessidade de sua existência.

Vamos retomar o exemplo do sistema bancário e criar uma classe `Programa` que vai interagir instâncias das duas classes `Cliente` e `Conta`. Alguns exemplos de interações são exibidos a seguir:

``` java
public class Programa {
    public static void main(String[] args) {
        Conta minhaConta;

        Cliente c = new Cliente("Victor", "Machado", "111.222.333-44", "r. X");

        minhaConta = new Conta(123, c, "1111-1");
        minhaConta.depositar(1000.0);

        System.out.println(minhaConta.exibirInfoConta());

        minhaConta.sacar(200.0);
        minhaConta.depositar(500.0);

        System.out.println("Saldo atual: R$" + minhaConta.consultarSaldo());

        minhaConta.sacar(10000);

        Conta c1 = new Conta();
        Conta c2;

        c1.depositar(100);
        c2 = c1; // c2 passa a apontar para o mesmo local na memória que c1
        c2.depositar(300);

        System.out.println(c1.consultarSaldo()); // 400.0
        System.out.println(c2.consultarSaldo()); // 400.0

        if (c1 == c2) {
            System.out.println("Contas iguais");
        } else {
            System.out.println("Contas diferentes");
        }

        c2 = new Conta(); // c2 agora aponta para um novo local na memória
        c2.depositar(400);

        if (c1 == c2) {
            System.out.println("Contas iguais");
        } else {
            System.out.println("Contas diferentes");
        }

        c1.transferir(100, c2);
        System.out.println(c1.consultarSaldo()); // 300.0
        System.out.println(c2.consultarSaldo()); // 500.0
    }
}
```

## Exercícios complementares

1. Crie uma fábrica de carros:

    * Crie uma classe `Carro`, com os atributos `cor`, `modelo`, `velocidadeAtual`, `velocidadeMaxima`. Inicialize `velocidadeAtual` com o valor 0;
    * Crie métodos:
        ** `ligar()`, que emite a mensagem "O carro está ligado";
        ** `acelerar(quantidade)`, que aumenta a velocidade atual no valor passado;
        ** `pegarMarcha()`, que retorna um número de -1 a 3 conforme a velocidade do carro:
            *** Abaixo de 0: -1
            *** Abaixo de 40: 1
            *** Abaixo de 80: 2
            *** Igual ou acima de 80: 3
    * Crie uma classe `Motor`, com os atributos `potencia` e `tipo`, e inclua um Motor no Carro;
    * Crie uma classe de teste e exercite as classes e os métodos criados.

2. Modele uma conta. A ideia aqui é apenas modelar, isto é, só identifique que informações são importantes. Desenhe tudo o que uma `Conta` tem e tudo o que ela faz. Ela deve ter o nome do titular (`String`), o número (`int`), a agência (`String`), o saldo (`double`) e uma data de abertura (`String`). Além disso, ela deve fazer as seguintes ações: sacar, para retirar um valor do saldo; depositar, para adicionar um valor ao saldo; calcularRendimento, para devolver o rendimento mensal dessa conta.
3. Transforme o modelo acima em uma classe Java. Teste-a, usando uma outra classe que tenha o `main`. Você deve criar a classe da conta com o nome `Conta`, mas pode nomear como quiser a classe de testes, contudo, ela deve possuir o método `main`. A classe Conta deve conter pelo menos os seguintes métodos:

    * `sacar` recebe um `valor` como parâmetro e retira esse valor do saldo da conta. O valor não pode ser inferior a 0;
    * `depositar` recebe um `valor` como parâmetro e adiciona esse valor ao saldo da conta;
    * `calcularRendimento` não recebe parâmetro algum e devolve o valor do saldo multiplicado por 0.1.

4. Crie um método `recuperarDadosParaImpressao()`, que não recebe parâmetro mas devolve o texto com todas as informações da nossa conta para efetuarmos a impressão. Veja que ela não imprime o texto na tela (não é responsabilidade da Conta, e sim do Programa que possui uma Conta instanciada).
5. Ao invés de utilizar uma única `String` para representar a data de abertura da conta, crie uma outra classe, chamada `Data`. Ela possui três campos `int`, para dia, mês e ano. Faça com que sua conta passe a usá-la.
6. Crie um método na classe `Data` que devolva o valor formatado da data, isto é, devolva uma String com `dia/mes/ano`.
7. Em um novo projeto, crie uma classe `Fibonacci` que possui um método `calculaFibonacci(num)`. Considere a classe de teste abaixo, que deve imprimir a sequência de fibonacci até a sexta posição (1, 1, 2, 3, 5, 8). Resolva esse exercício de forma recursiva, ou seja, o método `calculaFibonacci` não pode ter nenhum loop, só pode chamar ele mesmo como método.

    ``` java
        class TestaFibo() {
            public static void main(String[] args) {
                Fibonacci fibo = new Fibonacci();
                for (int i = 1; i <= 6; i++) {
                    int resultado = fibo.calculaFibonacci(i);
                    System.out.println(resultado);
                }
            }
        }
    ```
