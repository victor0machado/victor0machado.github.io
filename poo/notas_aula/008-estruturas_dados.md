# Estruturas de dados em Java

Em Java, as estruturas de dados estão representadas na linguagem no Java Collections Framework, e você pode acessar todos os detalhes sobre ele no [tutorial oficial](https://docs.oracle.com/javase/tutorial/collections/index.html).

> A collection — sometimes called a container — is simply an object that groups multiple elements into a single unit. Collections are used to store, retrieve, manipulate, and communicate aggregate data. Typically, they represent data items that form a natural group, such as a poker hand (a collection of cards), a mail folder (a collection of letters), or a telephone directory (a mapping of names to phone numbers).

A seguir, vamos fazer uma breve descrição sobre o conceito, propósito e operações de cada estrutura e, sem seguida, um exemplo de implementação em Java.

### Índice

- [Estruturas de dados em Java](#estruturas-de-dados-em-java)
    - [Índice](#índice)
  - [Vetor (Array)](#vetor-array)
  - [ArrayList](#arraylist)
  - [Lista encadeada (Linked list)](#lista-encadeada-linked-list)
  - [Pilha (Stack)](#pilha-stack)
  - [Conjunto (Set)](#conjunto-set)
  - [Mapas (HashMap)](#mapas-hashmap)

## Vetor (Array)

É uma estrutura linear onde dados homogêneos são armazenados em espaços contínuos da memória. O acesso a cada elemento é feito através de um índice.A principal desvantagem dos arrays, e o principal motivo pelo qual ele é pouco usado, é que um array, após definido, não pode ser redimensionado. Para "aumentar" o tamanho de um array, é necessário criar um novo array, e transferir os dados de um array para outro.

``` java
import java.util.Arrays;

class ArrayDemo {
    public static void main(String[] args) {
        int[] arrayInteiros = new int[5]; // Declara um array de 5 posições, vazio
        int[] numeros = {2,3,1,5,4}; // Um array com os elementos já preenchidos
        System.out.println(numeros.length); // Informa o tamanho do array, ou seja, 5
        System.out.println(numeros[0]); // Vai imprimir "2"
        Arrays.sort(numeros); // Ordena o array 
        System.out.println(Arrays.toString(numeros)); // Imprime cada um dos elementos
    }
}
```

## ArrayList

O ArrayList é uma estrutura particular a Java, que caracteriza um vetor redimensionável. Assim, conseguimos utilizar a ideia de vetores sem ter que ficar criando novos objetos sempre que quisermos aumentar o diminuir o conjunto de dados.

``` java
import java.util.ArrayList; // Importa a classe ArrayList
import java.util.Collections; // Importa a classe Collections

public class Main() {
    ArrayList<String> cars = new ArrayList<String>(); // Cria um objeto ArrayList
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    System.out.println(cars);
    System.out.println(cars.get(0)); // Pega o elemento de índice 0
    cars.set(0, "Fiat");
    System.out.println(cars.get(0));
    cars.remove(1); // Remove o elemento de índice 1
    cars.clear(); // Limpa o objeto
    cars.size(); // Retorna o númeo de elementos
    Collections.sort(cars); // Ordena o objeto cars
}
```

## Lista encadeada (Linked list)

Existe um elemento "raiz", logo, cada elemento está ligado a outro. O tamanho é dinâmico e a lista pode ser "espalhada" pela memória.

Essa estrutura costuma ser negligenciada devido suas semelhanças com ArrayList. No entanto, a principal vantagem está em listas com tamanho dinâmico que costumam crescer quando necessário. Enquanto no melhor caso da operação de adição, ambas tem custo `O(1)` (em notação [Big O](https://pt.wikipedia.org/wiki/Grande-O)), caso seja necessário redimensionar o array, o custo será `O(log(n)`).

Portanto, sempre que for necessário criar uma estrutura com alta variabilidade de tamanho, é interessante considerar uma lista encadeada ao invés de um ArrayList.

``` java
import java.util.LinkedList;

class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList<String> linkedList = new LinkedList<>(List.of("maçã", "uva", "banana")); // Cria uma nova lista encadeada 
        linkedList.push("laranja"); // Adiciona ao início
        String headElement = linkedList.poll(); // Remove o elemento da frente
        System.out.println("Removido: " + headElement); // Imprime "Removido: laranja"
    }
}
```

## Pilha (Stack)

Representa uma pilha (como um baralho de cartas ou livros empilhados), seguindo o algoritmo LIFO. As quatro operações principais são:

- `push(e)`: insere um elemento no topo;
- `pop()` - remove o elemento do topo;
- `isEmpty()` - informa verdadeiro/falso se a pilha está vazia;
- `peek()` - acessa o elemento do topo (sem remover).

Essa estrutura é muito usada para representações de estado ou histórico de navegação, onde o mais recente está sempre no topo.

``` java
import java.util.Stack;

class StackDemo {
    public static void main(String[] args) {
        Stack<String> history = new Stack<>();
        history.push("Algoritmos");
        history.push("Estruturas de Dados");  
        history.push("Java");  
        System.out.println("Topo: " + history.peek());  
        String collect = String.join(", ", history);  
        System.out.println("Todos: "+ collect);
    }
}
```

## Conjunto (Set)

Representa um grupo de dados homogêneos únicos, sem repetições. Por isso, deve haver uma forma de comparar os elementos de forma a decidir se são iguais ou não. Em Java, essa comparação é feita pelos métodos `equals` e `hashcode`. As principais classes que implementam a interface `Set` são: `HashSet`, `TreeSet` e `LinkedHashSet`.

``` java
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class SetDemo {
    public static void main(String[] args) {
        Set<String> setFrutas = new HashSet<>(List.of("maçã", "uva", "banana"));  
        setFrutas.add("abacaxi");  
        setFrutas.add("abacaxi"); // Não adiciona o elemento repetido
        String collect = String.join(", ", setFrutas); 
        System.out.println("Todos: "+ collect); // Todos: banana, uva, maçã, abacaxi
    }
}
```

## Mapas (HashMap)

O HashMap trabalha com o conceito de _key-value pairs_, ou seja, cada elemento de sua lista possui uma chave e valor associado, assim podemos realizar uma busca rápida pela chave que desejamos, sem precisar percorrer toda lista ou saber o índice/posição que desejamos consultar.

Esta estrutura usa funções hash para determinar a posição de cada elemento. Uma função hash é um algoritmo que mapeia dados de entrada de comprimento variável em dados de comprimento fixo. Assim, cada elemento a ser inserido na estrutura tem o seu endereço calculado. Isso evita "colisões" e acelera as operações de leitura.

``` java
import java.util.HashMap;
import java.util.Map;

public class ExemploHashMap {
    public static void main (String args[]){
        Map<String,String> example = new HashMap<String,String>();

        example.put( "K1", new String( "V1" ));
        example.put( "K2", new String( "V2" ));
        example.put( "K3", new String( "V3" ));
        example.put( "K4", new String( "V4" ));

        String keyToSearch = "K1";


        if (example.containsKey(keyToSearch)) {
            System.out.println("Valor da Chave " + keyToSearch + " = " + example.get(keyToSearch));
        } else {
            System.err.println("Chave não existe");
        }

        /*
        * O método "keySet()" retorna um Set com todas as chaves do
        * nosso HashMap, e tendo o Set com todas as Chaves,
        * podemos facilmente pegar
        * os valores que desejamos
        * */
        for (String key : example.keySet()) {
            //Capturamos o valor a partir da chave
            String value = example.get(key);
            System.out.println(key + " = " + value);
        }
    }
}
```
