# Exercícios de fixação

Neste material são apresentados alguns exercícios conceituais, voltados à fixação dos conhecimentos da linguagem Java e dos fundamentos do Paradigma Orientado a Objetos. O gabarito para os exercícios se [encontra aqui](000-gabaritos_exercicios.md).

1. Escolha a opção adequada ao tentar compilar e rodar o código a seguir:

``` java
class Test {
    public static void main(String [] args) {
        for (int i = 0; i < 20; i++) {
            System.out.println(i);
        }
        System.out.println(i);
    }
}
```

- a) Erro de compilação.
- b) Compila e roda, imprimindo de 0 até 19 e depois 19.
- c) Compila e roda, imprimindo de 0 até 19, depois ocorre um erro de execução.
- d) O código compila e roda normalmente.

2. Escolha a opção adequada ao tentar compilar e rodar o código a seguir:

``` java
class Test {
    public static void main(String [] args) {
        for (int i = 0; i < 20; i++)
            System.out.println(i);
            System.out.println(i);
        System.out.println("finished");
    }
}
```

- a) Erro de compilação.
- b) Compila e roda, imprimindo de 0 até 19 e depois 19.
- c) Compila e roda, imprimindo de 0 até 19, depois 19, depois `finished`.
- d) Compila e roda, imprimindo de 0 até 19, depois ocorre um erro de execução.

1. Escolha a opção adequada ao tentar compilar e rodar o código a seguir:

``` java
class Test {
    public static void main(String [] args) {
        for (int i = 0; i < 20; i++) {
            System.out.println(i);
        }
        int i = 15;
        System.out.println(i);
    }
}
```

- a) Erro de compilação na linha 6. A variável `i` não pode ser redeclarada.
- b) Erro de compilação na linha 7. A variável `i` é ambígua.
- c) Compila e roda, imprimindo de 0 até 19 e depois 15.
- d) Compila e roda, imprimindo de 0 até 19, depois ocorre um erro de execução na linha 6.

4. Escolha a opção adequada ao tentar compilar e rodar o código a seguir:

``` java
class Test {
    static int x = 15;

    public static void main(String [] x) {
        x = 200;
        System.out.println(x);
    }
}
```

- a) O código compila e roda, imprimindo 200.
- b) O código compila e roda, imprimindo 15.
- c) O código não compila.
- d) O código compila mas dá erro em execução.

5. Escolha a opção adequada ao tentar compilar e rodar o código a seguir:

``` java
class Test {
    int Test = 305;

    void Test() {
        System.out.println(Test);
    }

    public static void main(String[] args) {
        new Test();
    }
}
```

- a) O código não compila: erros nas linhas 2, 4, 5 e 6.
- b) O código não compila: erro na linha 5.
- c) O código compila e, ao rodar, imprime `305`.
- d) O código compila e não imprime nada.

6. Qual é uma assinatura válida do método `main` para executar um programa Java?

- a) `public static void main(String[] args)`
- b) `public static int main(String[] args)`
- c) `public static Void main(String []args)`
- d) `protected static void main(String[] args)`

7. Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir:

``` java
class A {
    public static void main(String[] args) {
        int
        age
        = 100;
        System.out.println(age);
    }
}
```

- a) O código não compila: erros a partir da linha que define uma variável do tipo `int`.
- b) O código não compila: a variável `age` não foi inicializada, mas foi usada em `System.out.println`.
- c) O código compila e imprime 0.
- d) O código compila e imprime 100.

8. Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir:

``` java
class A {
    public static void main(String[] args) {
        boolean argis;
        if (args.length > 0)
            argis = 1;
        else
            argis = 0;
        System.out.println(argis);
    }
}
```

- a) Não compila: o método de impressão não recebe `boolean`.
- b) Não compila: atribuição inválida.
- c) Compila e imprime 0 ou 1.
- d) Compila e imprime `false` ou `true`.

9. Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir:

``` java
class A {
    public static void main(String[] args) {
        boolean BOOLEAN = false;
        if (BOOLEAN) {
            System.out.println("Yes");
        }
    }
}
```

- a) Não compila: não podemos declarar uma variável com o nome de uma palavra reservada.
- b) Não compila: não podemos declarar uma variável iniciando com letras maiúsculas.
- c) Compula e roda, imprimindo `Yes`.
- d) Compila e roda, não imprimindo nada.

10. Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir:

``` java
class A {
    public static void main(String[] args) {
        int x = 15;
        int y = x;
        y++;
        x++;
        int z = y;
        z--;
        System.out.println(x + y + z);
    }
}
```

- a) Imprime 45.
- b) Imprime 46.
- c) Imprime 47.
- d) Imprime 48.

11. Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir:

``` java
class B {
    int v = 15;
}

class A {
    public static void main(String[] args) {
        B x new B();
        B y = x;
        y.v++;
        x.v++;
        B z = y;
        z.v--;
        System.out.println(x.v + y.v + z.v);
    }
}
```

- a) Imprime 45.
- b) Imprime 46.
- c) Imprime 47.
- d) Imprime 48.

12. Qual é o objetivo principal de se criar uma classe em POO?

- a) Armazenar variáveis globais.
- b) Permitir a reutilização de código.
- c) Acelerar o tempo de compilação.
- d) Permitie a criação de objetos genéricos.

13. Qual é a palavra-chave utilizada para definir uma classe em Java?

- a) class
- b) object
- c) this
- d) super

14. Em Java, qual é a forma correta de definir um construtor para uma classe `ClassName`, que precisa utilizar um parâmetro do tipo `int` chamado `parameter`?

- a) `void ClassName(int parameter)`
- b) `ClassName()`
- c) `ClassName(int parameter)
- d) `ClassName(parameter)`

15. Escolha a opção adequada ao tentar compilar e rodar o arquivo a seguir:

``` java
class B {
    int a;
    String b;

    B(int param1, String param2) {
        this.a = param1;
        this.b = param2;
    }

    B(String param1, int param2) {
        this.a = param2;
        this.b = param1;
    }
}

class A {
    public static void main(String[] args) {
        B b1 = new B(1, "oi");
        B b2 = new B("oi", 1);

        System.out.println(b1.a);
        System.out.println(b2.b);
    }
}
```

- a) O código não compila.
- b) O código compila, mas dá um erro de execução ao atribuir a variável `b1`.
- c) O código compila e exibe na tela os valores `1` e `oi`.
- d) O código compila e exibe na tela os valores `1` e `1`.

16. Quais são os benefícios do encapsulamento na POO?
17. Considere o bloco de código abaixo. Quais critérios fundamentais do POO (reuso, abstração, encapsulamento) não são obedecidos? Justifique.

``` java
class Médico {
    String nome;
    String cpf;
    String especialidade;

    // métodos
}

class Cardiologista {
    String nome;
    String cpf;
    String especialidade = "Cardiologia";

    // métodos
}

class Enfermeiro {
    String nome;
    String cpf;
    String departamento;

    // métodos
}
```
