# Gabaritos dos exercícios de fixação

[Voltar](001-exercicios_fixacao.md)

1. A resposta certa é (a). A variável `i` não pode ser acessada fora do laço.
2. A resposta certa é (a). A variável `i` não pode ser acessada fora do laço. Repare que o laço não foi declarado com `{}`, uma pegadinha clássica de provas de certificação.
3. A resposta certa é (c). A variável `i` declarada no `for` só é visível dentro do `for`.
4. A resposta certa é (c), a variável `x` declarada como parâmetro do método `main` efetua o que chamamos de _shadowing_. Nesse instante, ao dizermos `x = 200`, tentamos atribuir um `int` a um array de `String`, erro de compilação.
5. A resposta correta é (d). O que está sendo chamado no código é o construtor `Test()`, e não o método `Test()` (definido pelo retorno `void`).
6. A resposta correta é (a). Um método `main` deve ser público, estático e retornar `void`, além de receber apenas um argumento: um array (ou varargs) de String. Varargs (abreviação de argumentos variáveis) é uma funcionalidade do Java que permite que um método receba um número variável de argumentos. Veja mais sobre varargs [aqui](../notas_aula/004-conceitos_estruturais.md).
7. A resposta certa é (d). O código compila e imprime 100. Podemos ter espaços em branco desde que não quebre uma palavra-chave, nome de método, classes, etc. ao meio. Onde pode ter um espaço em branco, pode haver vários.
8. A resposta correta é (b). Não compila pois `boolean` em Java só pode ser `false` ou `true`.
9. A resposta correta é (d). Compila e roda, não imprimindo nada. Lembre-se que os identificadores são _case-sensitive_.
10. A resposta certa é (c). Imprime 47, pois a atribuição é por cópia de valor.
11. A resposta certa é (d). Imprime 48, pois a atribuição de objetos é feita por cópia da referência, criamos somente um único objeto do tipo `B`.
12. A resposta correta á (b). As classes são uma forma de encapsular dados e comportamentos relacionados, permitindo que essas informações sejam reutilizadas em outras partes do código.
13. A resposta correta é (a).
14. A resposta certa é (c). Um construtor não pode ter o tipo de retorno `void` na assinatura. Os parâmetros em um método precisam ter seu tipo especificado.
15. A resposta correta é (c). A sobrecarga do construtor é possível nesse caso pois há uma diferença na ordem dos parâmetros `int` e `String`.
16. O encapsulamento traz diversos benefícios para a programação orientada a objetos. Um dos principais é a segurança e integridade dos dados da classe, uma vez que eles são protegidos e só podem ser acessados ou modificados através de métodos específicos. Isso garante que o estado interno da classe não será corrompido ou modificado indevidamente, evitando erros e bugs no sistema. Além disso, o encapsulamento promove a modularidade e o baixo acoplamento entre as classes, facilitando a manutenção e evolução do código. Com uma interface pública claramente definida, outras classes podem interagir com a classe encapsulada sem precisar conhecer sua implementação interna, o que permite que ela seja modificada sem afetar o restante do sistema. Por fim, o encapsulamento também promove a reutilização do código, uma vez que uma classe encapsulada pode ser utilizada em diferentes contextos sem alterar sua implementação interna.
17. O exemplo de código não está obedecendo, em primeiro lugar, o conceito de abstração. `Cardiologista` é um "tipo" de médico, e poderia estar relacionado de alguma forma à classe `Medico`, porém não está. Da mesma forma, as três classes apresentadas são funcionários, e possuem características similares (nome e CPF), então o projeto poderia apresentar uma abstração das três classes (`Funcionario`, por exemplo). Como consequência direta, o exemplo também falha no reuso, já que os atributos `nome` e `cpf` são representados nas três classes. Caso haja uma mudança no formato da apresentação do nome (por exemplo, colocando o sobrenome no início da String), será necessário modificar os códigos das três classes.
