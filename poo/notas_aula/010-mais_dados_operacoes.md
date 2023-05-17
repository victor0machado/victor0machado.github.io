# Mais tipos de dados e operações em Java

Nesta nota de aula, vamos apresentar alguns tipos de dados mais avançados em Java, e como podemos aplicá-los no dia-a-dia de desenvolvimento. Também traremos alguns métodos especiais para implementação nas classes.

- [Mais tipos de dados e operações em Java](#mais-tipos-de-dados-e-operações-em-java)
  - [Métodos padrão da superclasse Object](#métodos-padrão-da-superclasse-object)
    - [O método `toString()`](#o-método-tostring)
    - [O método `equals()`](#o-método-equals)
    - [O método `hashCode()`](#o-método-hashcode)
    - [O método `getClass()`](#o-método-getclass)
    - [O método `clone()`](#o-método-clone)
  - [Uso de Strings em Java](#uso-de-strings-em-java)
    - [O StringBuilder](#o-stringbuilder)
  - [Classes para definição de data e hora](#classes-para-definição-de-data-e-hora)
    - [A classe `LocalDate`](#a-classe-localdate)
    - [A classe `LocalTime`](#a-classe-localtime)
    - [A classe `LocalDateTime`](#a-classe-localdatetime)

## Métodos padrão da superclasse Object

Os métodos padrão da superclasse `Object` em Java são herdados automaticamente por todas as classes, sem necessidade de declaração explícita. Esses métodos são importantes para a correta implementação de comportamentos específicos das classes, como a representação em string, comparação de igualdade e geração de códigos hash. Entender e sobrescrever esses métodos é fundamental para garantir o correto funcionamento e comportamento esperado das classes.

Ao longo do curso já trabalhamos com alguns desses métodos. Vamos detalhá-los aqui e trazer mais alguns deles. A lista completa de métodos que podem ser implementados se encontra na [documentação oficial](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html).

### O método `toString()`

O método `toString()` é usado para retornar uma representação em string do objeto. Por padrão, o método `toString()` retorna uma representação do objeto contendo o nome da classe e um identificador único do objeto. É recomendado sobrescrever esse método para fornecer uma representação mais significativa do objeto. Abaixo estão exemplos de uso do método `toString()`:

``` java
public class Pessoa {
    private String nome;
    private int idade;

    // construtor e outros métodos

    @Override
    public String toString() {
        return "Nome: " + nome + ", Idade: " + idade;
    }
}
```

### O método `equals()`

O método `equals()` é usado para comparar a igualdade entre dois objetos. Por padrão, o método compara se as referências dos objetos são iguais, ou seja, se ambos objetos apontam para o mesmo endereço na memória. No entanto, muitas vezes é necessário comparar o conteúdo dos objetos. É necessário sobrescrever o método `equals()` para fornecer uma implementação personalizada. Exemplos de uso do método equals():

``` java
public class Pessoa {
    private String nome;
    private int idade;

    // construtor e outros métodos

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        Pessoa pessoa = (Pessoa) obj;
        return idade == pessoa.idade && Objects.equals(nome, pessoa.nome);
    }
}
```

### O método `hashCode()`

O método `hashCode()` é usado para gerar um código hash único para cada objeto. Esse código hash é um valor numérico de 32 bits que é frequentemente usado em estruturas de dados, como tabelas de hash, para melhorar o desempenho de operações de busca. A função do método `hashCode()` é mapear o objeto para um valor inteiro, de forma que objetos iguais produzam o mesmo código hash. É importante que, se dois objetos são considerados iguais de acordo com o método `equals()`, seus códigos hash também sejam iguais. Exemplo de uso do método `hashCode()`:

``` java
public class Pessoa {
    private String nome;
    private int idade;

    // construtor e outros métodos

    @Override
    public int hashCode() {
        return Objects.hash(nome, idade);
    }
}
```

O motivo de se ter o método `hashCode()` mesmo após a implementação do método `equals()` é a necessidade de cumprir uma regra fundamental: dois objetos iguais de acordo com o método `equals()` devem ter o mesmo código hash. No entanto, a recíproca não é verdadeira: objetos diferentes podem ter o mesmo código hash.

Imagine uma aplicação que utiliza uma estrutura de dados baseada em hash, como `HashMap` ou `HashSet`. Essas estruturas de dados armazenam objetos em coleções com base nos seus códigos hash. Quando um elemento precisa ser encontrado, o código hash é calculado e usado para localizar a localização apropriada, tornando a busca mais eficiente.

Agora, suponha que temos uma classe chamada `Pessoa` que implementa o método `equals()`, mas não implementa o método `hashCode()`. Se tentarmos armazenar instâncias dessa classe em um `HashMap` ou `HashSet`, podemos enfrentar comportamentos inesperados. Embora a comparação de igualdade possa ser feita corretamente usando `equals()`, o mecanismo de busca baseado em código hash pode não funcionar adequadamente, resultando em problemas de desempenho ou comportamentos indesejados.

A implementação correta do método `hashCode()` permite que o mecanismo de busca baseado em hash funcione de forma adequada, garantindo a eficiência da estrutura de dados e a correta localização dos elementos.

### O método `getClass()`

O método `getClass()` retorna um objeto Class que representa a classe do objeto em questão. Esse método pode ser útil para obter informações sobre a classe de um objeto em tempo de execução.

``` java
public class Pessoa {
    private String nome;
    private int idade;

    // construtor e outros métodos

    public void exibirInformacoes() {
        System.out.println("Classe do objeto: " + getClass().getName());
    }
}
```

### O método `clone()`

O método `clone()` cria uma cópia do objeto. É importante observar que, para utilizar esse método corretamente, a classe deve implementar a interface `Cloneable`.

``` java
public class Pessoa implements Cloneable {
    private String nome;
    private int idade;

    // construtor e outros métodos

    @Override
    public Pessoa clone() throws CloneNotSupportedException {
        return (Pessoa) super.clone();
    }
}
```

## Uso de Strings em Java

A imutabilidade das strings em Java é uma característica importante da linguagem. Isso significa que, uma vez que uma string é criada, seu conteúdo não pode ser alterado. Cada operação realizada em uma string, como concatenação, substituição de caracteres ou extração de substrings, resulta na criação de uma nova string com o resultado desejado.

Essa imutabilidade traz algumas vantagens. Por exemplo, torna as strings seguras para compartilhamento entre várias partes do código, uma vez que seu conteúdo não pode ser modificado acidentalmente. Além disso, permite otimizações de desempenho, como o compartilhamento de strings idênticas na memória, por meio do conceito de "string pooling" (ver abaixo).

No entanto, é importante ter cuidado ao lidar com operações frequentes em strings, pois cada operação cria uma nova string e aloca memória adicional. Isso pode resultar em um aumento desnecessário do consumo de memória e impactar o desempenho do programa. Nesses casos, a classe StringBuilder pode ser utilizada como uma alternativa mais eficiente, permitindo a manipulação e modificação de strings sem a necessidade de criar novos objetos a cada operação.

Portanto, ao lidar com strings em Java, é fundamental ter em mente a imutabilidade e suas implicações, considerando o uso adequado das operações e, quando necessário, utilizar a classe StringBuilder para manipulação eficiente de strings mutáveis.

> O String Pooling (ou "piscina de strings") é uma técnica de otimização em Java, na qual as strings literais são armazenadas em uma área especial de memória chamada pool de strings. O objetivo do String Pooling é reduzir a quantidade de memória utilizada pelo armazenamento de várias strings idênticas.
>
> Quando uma string literal é declarada no código-fonte, o compilador Java verifica se essa string já existe no pool de strings. Se existir, a referência para a string já existente é retornada em vez de criar uma nova instância da string. Isso evita a duplicação desnecessária de strings com o mesmo conteúdo, economizando memória.
>
> Essa técnica é possível devido à imutabilidade das strings em Java. Como as strings não podem ser modificadas, é seguro compartilhar a mesma instância entre diferentes partes do código, uma vez que o conteúdo não será alterado.
>
> O String Pooling é especialmente útil quando há muitas ocorrências de uma mesma string no código. Por exemplo, se várias variáveis ou constantes utilizarem a mesma string literal, o pooling garante que apenas uma instância dessa string seja armazenada na memória.
>
> No entanto, é importante mencionar que o String Pooling se aplica apenas a strings literais definidas diretamente no código-fonte. Strings criadas dinamicamente usando construtores ou métodos como new String() não são colocadas no pool de strings.
>
> Em resumo, o String Pooling é uma otimização em Java que evita a duplicação de strings literais idênticas, armazenando apenas uma instância delas no pool de strings. Isso ajuda a economizar memória e melhora o desempenho ao reduzir a alocação desnecessária de objetos String.

### O StringBuilder

O `StringBuilder` é uma classe que oferece uma alternativa eficiente para manipulação de strings em Java, especialmente quando precisamos realizar operações de concatenação ou modificação frequentes. Diferentemente das strings tradicionais, os objetos StringBuilder podem ser modificados, o que reduz a necessidade de criar novos objetos a cada operação.

Aqui estão alguns exemplos de uso do StringBuilder, veja mais informações sobre a classe na [documentação oficial](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuilder.html):

* Criação de um StringBuilder:

``` java
StringBuilder sb = new StringBuilder();
```

* Adição de strings ao StringBuilder:

``` java
sb.append("Olá");
sb.append(" ");
sb.append("Mundo");
```

* Conversão do StringBuilder para uma string:

``` java
String resultado = sb.toString();
```

* Inserção de uma string em uma posição específica:

``` java
sb.insert(4, "Java");
```

* Remoção de parte da string:

``` java
sb.delete(0, 3);
```

* Reversão da string:

``` java
sb.reverse();
```

## Classes para definição de data e hora

Essas classes fornecem métodos e funcionalidades que facilitam a manipulação, formatação e cálculos relacionados a datas e horas. Compreender e utilizar corretamente essas classes é essencial ao lidar com tarefas que envolvem a manipulação de tempo em seus programas. Para mais informações e métodos disponíveis, consulte a documentação sobre as classes [`LocalDate`](https://docs.oracle.com/javase/8/docs/api/java/time/LocalDate.html), [`LocalTime`](https://docs.oracle.com/javase/8/docs/api/java/time/LocalTime.html) e [`LocalDateTime`](https://docs.oracle.com/javase/8/docs/api/java/time/LocalDateTime.html).

### A classe `LocalDate`

A classe `LocalDate` é usada para representar uma data sem levar em consideração o fuso horário ou a hora específica do dia. Ela armazena apenas o dia, mês e ano. Alguns métodos comuns disponíveis nesta classe são:

* `now()`: retorna a data atual;
* `getYear()`, `getMonth()`, `getDayOfMonth()`: obtém o ano, mês e dia da data, respectivamente;
* `isBefore()`, `isAfter()`: verifica se uma data é anterior ou posterior a outra.

``` java
import java.time.LocalDate;

public class ExemploLocalDate {
    public static void main(String[] args) {
        LocalDate dataAtual = LocalDate.now();
        System.out.println("Data atual: " + dataAtual);

        int ano = dataAtual.getYear();
        int mes = dataAtual.getMonthValue();
        int dia = dataAtual.getDayOfMonth();
        System.out.println("Ano: " + ano);
        System.out.println("Mês: " + mes);
        System.out.println("Dia: " + dia);

        LocalDate dataFutura = LocalDate.of(2023, 12, 31);
        boolean dataFuturaIsAfterDataAtual = dataFutura.isAfter(dataAtual);
        System.out.println("A data futura é posterior à data atual? " + dataFuturaIsAfterDataAtual);
    }
}
```

### A classe `LocalTime`

A classe `LocalTime` é usada para representar um horário específico do dia, sem considerar o fuso horário. Ela armazena apenas a hora, minuto, segundo e frações de segundo. Alguns métodos comuns disponíveis nesta classe são:

* `now()`: retorna o horário atual;
* `getHour()`, `getMinute()`, `getSecond()`: obtém a hora, minuto e segundo do horário, respectivamente;
* `plusHours()`, `minusMinutes()`: adiciona ou subtrai uma quantidade específica de horas, minutos ou segundos do horário.

``` java
import java.time.LocalTime;

public class ExemploLocalTime {
    public static void main(String[] args) {
        LocalTime horaAtual = LocalTime.now();
        System.out.println("Hora atual: " + horaAtual);

        int hora = horaAtual.getHour();
        int minuto = horaAtual.getMinute();
        int segundo = horaAtual.getSecond();
        System.out.println("Hora: " + hora);
        System.out.println("Minuto: " + minuto);
        System.out.println("Segundo: " + segundo);

        LocalTime horaDaquiUmaHora = horaAtual.plusHours(1);
        System.out.println("Hora daqui uma hora: " + horaDaquiUmaHora);
    }
}
```

### A classe `LocalDateTime`

A classe LocalDateTime combina uma data e um horário, representando um ponto específico no calendário. Ela é usada quando é necessário trabalhar com informações completas de data e hora. Alguns métodos comuns disponíveis nesta classe são:

* `now()`: retorna a data e hora atuais.
* `plusDays()`, `minusHours()`, etc.: adiciona ou subtrai uma quantidade específica de dias, horas, minutos ou segundos da data e hora.
* `format()`: formata a data e hora em uma string de acordo com um padrão específico.

``` java
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class ExemploLocalDateTime {
    public static void main(String[] args) {
        LocalDateTime dataHoraAtual = LocalDateTime.now();
        System.out.println("Data e Hora atual: " + dataHoraAtual);

        LocalDateTime dataHoraFutura = dataHoraAtual.plusDays(3).minusHours(2);
        System.out.println("Data e Hora daqui 3 dias e 2 horas atrás: " + dataHoraFutura);

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
        String dataHoraFormatada = dataHoraAtual.format(formatter);
        System.out.println("Data e Hora formatada: " + dataHoraFormatada);
    }
}
```
