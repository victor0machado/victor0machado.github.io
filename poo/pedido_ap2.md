# Pedido da AP2

## Pedido

Neste projeto vocês devem evoluir o sistema de partidas que foi sendo desenvolvido nas atividades anteriores. Vocês devem iniciar o desenvolvimento a partir do gabarito da última AC (disponível no [github](https://github.com/victor0machado/POO-2023.1/tree/main/aula08_ap1_v12) ou [replit](https://replit.com/@victor0machado/java-20231-aula08-ap1v12)).

### Requisitos para o projeto

* Refatore o código para evitar construção de mensagens por concatenação de strings. Utilize o `StringBuilder` no lugar;
* Refatore o código para substituir as informações de data por objetos da classe `LocalDate`, `LocalTime` ou `LocalDateTime` conforme necessário;
* Implemente os métodos `toString()`, `equals()` e `hashCode()` onde for necessário;
* Refatore organização do projeto:
  * Criar pacote `dao`, responsável por armazenar as classes DAO;
  * Refatorar pacote `cli` para pacote `programa`, responsável por armazenar as classes de operação do sistema;
  * Refatorar classe `Cli.java` para `Gestor.java`;
  * Criar pacote `util`, junto com classes para manipulação de arquivo e leitura de dados do usuário;
  * Criar um subpacote `ingresso` dentro do pacote `entidades`, para armazenar as classes de ingressos;
  * Refatorar o código para a nova organização de pacotes;
* Mover da classe `Gestor.java` códigos de leitura de dados de usuário;
* Implementar classes `PartidaDAO.java` e `IngressoDAO.java`, que vão realizar as operações de armazenamento e controle dos dados de partidas e de ingressos, respectivamente;
* Possibilitar que a aplicação realize as seguintes operações, através de comandos por texto:
  * Operações de partida:
    * Criar, excluir, editar e atualizar partidas;
    * Listar todas as partidas;
    * Exibir informações sobre uma partida específica;
  * Operações de ingressos:
    * Realiza a venda de um ingresso;
    * Exibe o número de ingressos restantes para todas as partidas;
    * Exibe o número de ingressos restantes para uma partida;
    * Lista todos os ingressos vendiddos de uma partida;
    * Exibe os dados do último ingresso vendido;
* O programa deve salvar automaticamente os dados em arquivos de texto.

## Avaliação

O projeto será avaliado de acordo com os seguintes critérios:

* Qualidade de escrita do código: variáveis foram bem nomeadas, código está de acordo com os padrões discutidos em sala (_casing_, indentação, espaçamento, etc.);
* Qualidade da implementação: o código não apresenta redundâncias ou acoplamento excessivo. O projeto está bem organizado e os métodos estão implementados nas classes adequadas;
* Qualidade da interface de texto: a interface está organizada, as opções estão claras e não há confusão nas informações de dados;
* Testes realizados pelo professor não apresentam falhas.

## Informações gerais:

* Prazo: 18/06/2023 (não serão aceitos atrasos!);
* Grupos de no máximo 3 pessoas;
* Compactar todos os arquivos .java num único arquivo .zip e enviar para o e-mail victor.silva@professores.ibmec.edu.br;
* Incluir o nome de todos os participantes no e-mail enviado.
