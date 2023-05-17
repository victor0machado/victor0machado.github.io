# Tratamento de erros e exceções em Java

Nesta nota de aula, abordaremos o tratamento de erros e exceções em Java. O tratamento adequado de erros é fundamental para garantir a robustez e a confiabilidade de um programa. Java oferece recursos poderosos para lidar com exceções, permitindo a detecção, o tratamento e a recuperação de situações inesperadas durante a execução de um programa. Confira mais informações sobre a classe `Exception` na [documentação oficial](https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html), e acompanhe [este tutorial na página da Oracle sobre o assunto](https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html).

## O que são exceções

Em Java, uma exceção é uma ocorrência anormal que interrompe o fluxo normal de execução de um programa. Elas podem ser causadas por diversos motivos, como erros de programação, como acessar um índice inválido de um array, problemas de hardware, como falta de memória disponível, condições imprevistas, como uma conexão de rede interrompida, ou eventos externos, como falhas de acesso a um banco de dados.

Quando uma exceção é lançada, um objeto exceção é criado para representar essa situação inesperada. Esse objeto contém informações sobre o erro, como uma mensagem descritiva do problema, a pilha de chamadas que levou ao erro e outros detalhes relevantes para ajudar na depuração e solução do problema. O tratamento adequado de exceções permite que o programa identifique e lide com essas situações excepcionais de forma apropriada, fornecendo uma resposta adequada ao usuário ou realizando ações de recuperação necessárias.

## Tipos de exceções

Em Java, as exceções são divididas em dois tipos: exceções verificadas (_checked exceptions_) e exceções não verificadas (_unchecked exceptions_). As exceções verificadas são aquelas que o compilador obriga a tratar ou declarar explicitamente em um método. Elas são subclasses da classe `Exception`, exceto subclasses de `RuntimeException`. Um exemplo comum de exceção verificada é a `IOException`, que é lançada por operações de entrada e saída (E/S). Ao usar uma exceção verificada, o compilador força o programador a lidar com possíveis erros de E/S, seja através de um bloco `try-catch` ou declarando que o método pode lançar essa exceção com a cláusula `throws`.

Por outro lado, as exceções não verificadas são subclasses de `RuntimeException`. Elas não precisam ser declaradas explicitamente em um método ou tratadas com blocos `try-catch`. Exemplos de exceções não verificadas incluem a `NullPointerException`, que ocorre quando uma referência nula é usada, e a `ArrayIndexOutOfBoundsException`, que ocorre quando se tenta acessar um índice inválido em um array. As exceções não verificadas são frequentemente relacionadas a erros de programação, como erros de lógica ou uso inadequado de estruturas de dados.

A distinção entre exceções verificadas e não verificadas é importante, pois afeta a forma como o compilador e o ambiente de execução tratam essas exceções. As exceções verificadas garantem que os erros sejam tratados ou propagados corretamente, ajudando a evitar problemas inesperados durante a execução do programa. Por outro lado, as exceções não verificadas fornecem mais flexibilidade e liberdade ao programador, mas também exigem maior responsabilidade na detecção e tratamento dessas exceções para evitar problemas em tempo de execução.

## Bloco `try-catch`

O bloco `try-catch` é uma construção fundamental para o tratamento de exceções em Java. Ele permite que você controle o fluxo de execução do programa e tome medidas apropriadas quando uma exceção ocorre. O bloco `try` contém o código que pode gerar uma exceção. Dentro do bloco `try`, você pode incluir várias linhas de código que potencialmente podem lançar exceções. Em seguida, o bloco `catch` é usado para capturar e tratar a exceção caso ela ocorra.

Cada bloco `catch` é associado a um tipo específico de exceção que você deseja tratar. Dessa forma, é possível ter vários blocos `catch` para lidar com diferentes tipos de exceções de maneira adequada. Quando uma exceção é lançada, o Java procura pelo bloco `catch` correspondente ao tipo de exceção. Se for encontrado um bloco `catch` correspondente, o código dentro desse bloco será executado para tratar a exceção.

Além disso, é possível utilizar o bloco finally junto com o bloco `try-catch`. O bloco `finally` é opcional e é executado independentemente de ter ocorrido ou não uma exceção. É comumente usado para liberar recursos abertos, como fechar conexões com bancos de dados ou arquivos, independentemente do resultado do bloco `try`.

Aqui está um exemplo do uso do bloco `try-catch`:

``` java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ExemploTryCatch {

    public static void main(String[] args) {
        BufferedReader leitor = null;

        try {
            FileReader arquivo = new FileReader("arquivo.txt");
            leitor = new BufferedReader(arquivo);

            String linha = leitor.readLine();
            System.out.println("Conteúdo do arquivo: " + linha);

        } catch (IOException e) {
            System.out.println("Ocorreu um erro de E/S: " + e.getMessage());

        } finally {
            if (leitor != null) {
                try {
                    leitor.close(); // Fechando o leitor
                } catch (IOException e) {
                    System.out.println("Erro ao fechar o leitor: " + e.getMessage());
                }
            }

            System.out.println("Bloco finally executado sempre, independentemente de ter ocorrido uma exceção ou não.");
        }
    }
}
```

Neste exemplo, estamos lendo o conteúdo de um arquivo utilizando as classes `FileReader` e `BufferedReader`. O bloco `try` envolve o código que pode lançar uma exceção de E/S. No bloco `catch`, estamos capturando uma possível exceção de `IOException`, que pode ocorrer durante a leitura do arquivo. Dentro do bloco `catch`, estamos exibindo uma mensagem de erro para o usuário. Por fim, o bloco `finally` é utilizado para garantir que o leitor seja sempre fechado, mesmo que ocorra uma exceção durante a leitura do arquivo.

As instruções `try-catch` devem ser usadas sempre que você tem um bloco de código que pode lançar uma exceção que você deseja tratar. A frequência do uso de `try-catch` depende das situações específicas do seu código e dos possíveis erros que podem ocorrer.

A recomendação geral é usar `try-catch` de forma seletiva, onde é necessário tratar exceções específicas em pontos específicos do seu código. Você não precisa envolver todo o seu programa em blocos `try-catch` a menos que seja necessário.

É importante lembrar que o tratamento de exceções deve ser orientado a erros que você pode esperar e lidar de forma apropriada. Não é recomendado utilizar `try-catch` para tratar erros triviais que são previsíveis e que podem ser evitados por meio de validações e verificações adequadas.

Além disso, é possível utilizar a cláusula `throws` para propagar exceções não tratadas em métodos e permitir que o código chamador seja responsável pelo tratamento. Isso é especialmente útil quando você não tem a informação ou o contexto necessário para tratar a exceção adequadamente naquele ponto específico.

Em resumo, as instruções `try-catch` devem ser usadas sempre que você precisa tratar exceções específicas em pontos específicos do seu código. Use-as com parcimônia e em locais apropriados, de acordo com as necessidades e requisitos do seu programa.

## Lançamento de exceções

Além de capturar e tratar exceções, é possível lançar exceções manualmente usando a palavra-chave `throw`. Isso permite que você sinalize erros específicos e notifique os chamadores do método sobre a ocorrência de uma exceção.

``` java
public void dividir(int a, int b) throws ArithmeticException {
    if (b == 0) {
        throw new ArithmeticException("Divisão por zero não é permitida.");
    }
    int resultado = a / b;
    System.out.println("Resultado: " + resultado);
}
```

## Cláusula `throws`

A cláusula `throws` é usada na declaração de um método para indicar que o método pode lançar uma exceção específica. Quando um método declara uma exceção com `throws`, ele está indicando que não trata a exceção dentro do método e que a responsabilidade de tratá-la será delegada ao código que chama esse método.

``` java
public void lerArquivo(String nomeArquivo) throws FileNotFoundException {
    FileInputStream file = new FileInputStream(nomeArquivo);
    // ...
}
```

## Uso de blocos `try-with-resources`

O bloco `try-with-resources` é uma construção introduzida a partir do Java 7 que facilita o tratamento de recursos que precisam ser fechados após o uso, como arquivos ou conexões de banco de dados. O bloco `try-with-resources` automaticamente fecha os recursos abertos, sem a necessidade de usar explicitamente o método `close()`.

``` java
try (FileReader reader = new FileReader("arquivo.txt")) {
    // Código para ler o arquivo
    // ...
} catch (IOException e) {
    // Tratamento para exceções de E/S
    // ...
}
```

## Cirando exceções personalizadas

Em Java é possível criar tipos de exceções personalizadas por meio da criação de classes que herdam da classe `Exception` ou de suas subclasses. Essas classes são conhecidas como exceções personalizadas ou exceções de usuário.

Para criar uma exceção personalizada, você pode definir uma nova classe que estende a classe `Exception` (ou uma de suas subclasses, como `RuntimeException`). É comum nomear essas classes com um sufixo "Exception" para indicar que são exceções. Por exemplo, se você deseja criar uma exceção personalizada para representar um erro de validação de dados, poderia criar a classe `ValidationException`.

A classe da exceção personalizada pode ter construtores personalizados para receber informações relevantes sobre o erro. Além disso, você pode adicionar métodos específicos para obter detalhes adicionais sobre a exceção ou realizar operações relacionadas a ela.

Aqui está um exemplo de criação de uma exceção personalizada chamada `CustomException`:

``` java
public class CustomException extends Exception {

    public CustomException() {
        super();
    }

    public CustomException(String message) {
        super(message);
    }

    public CustomException(String message, Throwable cause) {
        super(message, cause);
    }

    public CustomException(Throwable cause) {
        super(cause);
    }

    // Outros métodos e funcionalidades relacionadas à exceção personalizada
}
```

Neste exemplo, a classe `CustomException` herda da classe `Exception`. Ela possui construtores que chamam os construtores correspondentes da superclasse, permitindo a passagem de uma mensagem de erro e/ou uma causa para a exceção personalizada.

Com essa classe de exceção personalizada definida, é possível lançar e capturar essa exceção no código código:

``` java
public class Exemplo {
    public static void main(String[] args) {
        try {
            throwCustomException();
        } catch (CustomException e) {
            System.out.println("Ocorreu uma exceção personalizada: " + e.getMessage());
        }
    }

    public static void throwCustomException() throws CustomException {
        throw new CustomException("Erro personalizado ocorreu!");
    }
}
```

Neste exemplo, estamos lançando a exceção personalizada `CustomException` no método `throwCustomException` e capturando-a no bloco `catch` correspondente. Ao capturar a exceção, podemos acessar sua mensagem e realizar qualquer tratamento necessário.

Criar exceções personalizadas permite que você modele e capture erros específicos do seu domínio de aplicação, proporcionando uma melhor organização e semântica ao tratamento de exceções em seu código.
