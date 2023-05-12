# IBM0762 - Programação Orientada a Objetos

Vou colocar nessa página links das aulas e materiais adicionais referentes à disciplina.

* [Agenda](agenda.md)
* [GRID](grid.md)

## Material geral

* [Slides da disciplina](/./assets/poo/slides.pdf)
* [Exercícios de fundamentos](./exercicios/001-exercicios_fixacao.md)
* [Pedido da AP1](./pedido_ap1.md)
* [Gabarito da AP1](https://replit.com/@victor0machado/java-20231-ap1)
* [Repositórios dos exercícios no github](https://github.com/victor0machado/POO-2023.1)

## Notas de aula

* [01 - Introdução ao Curso](./notas_aula/001-intro_curso.md)
* [02 - Fundamentos da Orientação a Objetos](./notas_aula/002-fundamentos_oo.md)
* [03 - Introdução a Java](./notas_aula/003-intro_java.md)
* [04 - Conceitos estruturais](./notas_aula/004-conceitos_estruturais.md)
* [05 - Introdução à UML](./notas_aula/005-intro_uml.md)
* [06 - Conceitos relacionais](./notas_aula/006-conceitos_relacionais.md)
* [07 - Conceitos organizacionais](./notas_aula/007-conceitos_oganizacionais.md)
* [08 - Estruturas de dados em Java](./notas_aula/008-estruturas_dados.md)
* [09 - Persistência de dados em arquivos](./notas_aula/009-persistencia_dados.md)

## Conteúdo das aulas

* [Aula 01 - Conceitos de Java](https://replit.com/@victor0machado/java-20231-aula01#Main.java)
* [Aula 02 - Conceitos de Java - Exercícios](https://replit.com/@victor0machado/java-20231-aula02#Main.java)
* [Aula 03 - Conceitos estruturais](https://replit.com/@victor0machado/java-20231-aula03#Main.java)
* [Aula 04 - Conceitos relacionais](https://replit.com/@victor0machado/java-20231-aula04#Main.java)
* [Aula 04 - Conceitos relacionais - Exercícios](https://replit.com/@victor0machado/java-20231-aula04-exercicio#Main.java)
* [Aula 05 - Conceitos relacionais](https://replit.com/@victor0machado/java-20231-aula05#Main.java)
* [Aula 06 - Conceitos organizacionais](https://replit.com/@victor0machado/java-20231-aula06#Main.java)
* [Aula 07 - Estruturas de dados em Java](https://replit.com/@victor0machado/java-20231-aula07#Main.java)
* [Aula 07 - Estruturas de dados em Java - AP1 v1.1](https://replit.com/@victor0machado/java-20231-aula07-ap1v11)

## Pedidos ACs

### AC6

De posse do [gabarito da atividade anterior](https://replit.com/@victor0machado/java-20231-aula07-ap1v11), atender aos seguintes pedidos:

* Organização do código
  * Tornar todos os atributos privados (ou protegidos) e todos os métodos públicos
  * Criar um pacote "entidades" e mover as classes de entidades para lá
  * Criar um pacote "cli" e mover o código da classe Main (incluindo os métodos) para a classe Cli.java
* Valor do ingresso
  * Alterar a classe Partida para ter um parâmetro `double valorIngresso`
  * Alterar classes Ingresso, IngressoInteira e IngressoMeia para utilizarem o atributo `valorIngresso` da classe `Partida`
  * Alterar o método cli.venderIngresso remover a constante do valor do ingresso
  * Alterar a interface por linha de comando para, ao criar uma partida, pedir para o usuário o valor do ingresso
* CRUD Partida
  * Incluir uma opção para remover uma partida a partir do seu nome
  * Incluir uma opção para editar as informações de uma partida (apenas data, local e valor do ingresso)
  * Altere a opção de criar uma partida para não permitir criar uma partida com nome já definido

---

[Voltar](https://victor0machado.github.io/)
