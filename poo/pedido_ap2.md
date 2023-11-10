# IBM0516 - Programação Orientada a Objetos - Pedido da AP2

## Pedido

Sua equipe foi solicitada para evoluir o projeto desenvolvido anteriormente, para venda de ingressos para eventos. Você pode utilizar o seu projeto no estado atual, ou utilizar [este projeto](https://github.com/victor0machado/poo-2023.2/tree/main/ap1) como ponto de partida. Caso utilize o seu projeto, garanta que todas as funcionalidades anteriores estejam funcionando!

Dessa vez, novas funcionalidades foram detalhadas. Ao contrário da entrega anterior, não estão apresentadas as classes a serem implementadas. O seu time será avaliado pela qualidade da organização do código e das classes.

### Novas funcionalidades

* O programa deve permitir a criação de múltiplos eventos, que devem ser armazenados durante toda a execução do programa;
* O programa deve possibilitar, durante a venda do ingresso, que o usuário escolha de qual evento ele deseja realizar a venda;
* O programa não deve mais exibir a opção de mostrar o último ingresso vendido;
* O programa deve permitir a busca de um evento pelo nome;
* O programa deve permitir excluir um evento já criado;
* O programa deve permitir atualizar um evento criado, modificando data e local (os demais dados devem ser preservados);
* O programa deve poder exibir todos os eventos cadastrados;
* As datas armazenadas ao longo do programa devem ser do tipo `LocalDate`, e não mais `String`;
* Ao exibir o número de ingressos restantes para um dado evento, o programa deve exibir os ingressos tipo meia e ingressos tipo inteira, e não os dois combinados;
* O programa deve persistir os dados dos eventos ao ser encerrado, salvando-os em um arquivo de texto;
  * Não é necessário ler os dados do arquivo ao inicializar, apenas salvar os dados quando for finalizar;
* Os casos de exceção (evento inválido, lista de eventos vazia, etc.) devem ser criados de acordo;
* O programa precisa ter a sua interface de texto atualizada com as novas opções descritas acima.

## Avaliação

O projeto será avaliado de acordo com os seguintes critérios:

* Qualidade da implementação (20%): código está bem escrito, e não apresenta redundâncias ou acoplamento excessivo. O projeto está bem organizado e os métodos estão implementados nas classes adequadas. O projeto possui pacotes claros e que separam logicamente as diferentes unidades do programa;
* Qualidade da interface de texto (10%): a interface está organizada, as opções estão claras e não há confusão nas informações de dados;
* Testes realizados pelo professor não apresentam falhas (70%).

## Informações gerais:

* Prazo: 24/10/2023;
* Grupos de no mínimo 3 e no máximo 5 pessoas;
* Entrega via Sala de Aula Virtual (estudante.ibmec.br);
* Submeter pelo estudante um link para um repositório privado específico para o projeto, adicionando o professor (@victor0machado) como colaborador. O repositório precisa ter o nome de todos os participantes.
