# Pedido da AP1

## Pedido

Você recebeu um pedido de projeto para desenvolver um aplicativo para venda de ingressos online para um evento esportivo. O aplicativo deve permitir que os usuários comprem ingressos para as partidas, selecionem o assento e realizem o pagamento de forma online.

### Funcionalidades do projeto

* O aplicativo deve permitir que o usuário visualize a lista de partidas disponíveis para venda;
* Para cada partida, o usuário deve poder escolher a quantidade e o tipo de ingressos desejados, bem como o assento que deseja ocupar;
* O aplicativo deve calcular o preço total da compra de acordo com a quantidade e o tipo de ingressos selecionados;
* O usuário deve poder realizar o pagamento de forma online através de uma das opções de pagamento disponíveis;
* Após o pagamento, o usuário deve receber um comprovante de compra com as informações sobre a partida, a quantidade e o tipo de ingressos comprados e o assento escolhido.

### Implementações necessárias

Para a primeira entrega, será necessário que você implemente o seguinte:

* **Partida:** classe que representa uma partida do evento esportivo. Deve conter os seguintes atributos e métodos:
    * *Atributo nome (String):* nome da partida;
    * *Atributo data (String):* data e horário da partida;
    * *Atributo local (String):* local onde será realizada a partida;
    * *Atributo ingressosInteira (int):* mapa com a quantidade de ingressos tipo inteira disponíveis;
    * *Atributo ingressosMeia (int):* mapa com a quantidade de ingressos tipo meia disponíveis;
    * *Método getNome():* retorna o nome da partida;
    * *Método getData():* retorna a data e horário da partida;
    * *Método getLocal():* retorna o local onde será realizada a partida;
    * *Método getIngressos():* retorna o número de ingressos disponíveis (soma dos ingressos tipo inteira e meia);
    * *Método isIngressoDisponivel(TipoIngresso tipo, int quantidade):* verifica se há ingressos disponíveis para o tipo e quantidade especificados;
    * *Método venderIngresso(TipoIngresso tipo):* realiza a venda de ingressos do tipo e quantidade especificados e retorna o valor total da venda;
* **TipoIngresso:** enumeração que representa os tipos de ingresso disponíveis. Deve conter os seguintes valores:
    * *INTEIRA:* para ingressos inteiros;
    * *MEIA:* para ingressos com desconto de meia-entrada.
* **Assento:** classe que representa um assento na arquibancada do evento esportivo. Deve conter os seguintes atributos e métodos:
    * *Atributo numero (int):* número do assento;
    * *Atributo fila (char):* letra que representa a fila do assento.
    * *Método getNumero():* retorna o número do assento;
    * *Método getFila():* retorna a letra que representa a fila do assento.
* **Ingresso:** classe abstrata que representa um ingresso vendido para uma partida. Deve conter os seguintes atributos e métodos:
    * *Atributo partida (Partida):* partida para a qual o ingresso foi vendido;
    * *Atributo tipo (TipoIngresso):* tipo de ingresso vendido;
    * *Atributo assento (Assento):* assento ocupado pelo ingresso;
    * *Atributo preço (double):* valor do ingresso;
    * *Método getPreco():* retorna o preço;
* **IngressoInteira e IngressoMeia:** classes concretas que herdam de `Ingresso`, e passam no construtor o tipo adequado de ingresso, utilizando o enum `TipoIngresso`;

Para a criação de enumerações, consulte [este material online](https://blog.betrybe.com/java-enum/).

### Menu de interface

Para a primeira entrega, foi solicitado que você elabore uma interface por linha de comando (CLI), de forma que o usuário possa realizar as seguintes operações:

* Cadastre uma nova partida;
* Realize a venda de um ingresso, em que o usuário escolhe um assento (fila e número), o tipo do ingresso (inteira ou meia), e o programa gera um ingresso e exibe na tela as informações. O usuário deve confirmar se as informações estão corretas e o programa deve sinalizar que a compra foi realizada;
* Exibir informações da partida;
* Exibir o número de ingressos restantes;
* Exibir informações do último ingresso vendido;

O programa só precisa armazenar uma partida e um ingresso por vez. Ou seja, se uma nova partida for cadastrada, a partida anterior é apagada.

## Avaliação

O projeto será avaliado de acordo com os seguintes critérios:

* Qualidade de escrita do código: variáveis foram bem nomeadas, código está de acordo com os padrões discutidos em sala (_casing_, indentação, espaçamento, etc.);
* Qualidade da implementação: o código não apresenta redundâncias ou acoplamento excessivo. O projeto está bem organizado e os métodos estão implementados nas classes adequadas;
* Qualidade da interface de texto: a interface está organizada, as opções estão claras e não há confusão nas informações de dados;
* Testes realizados pelo professor não apresentam falhas;
* Arguição oral feita pelo professor na aula do dia 28/04/23.

Serão dados pontos extras para validações de dados adicionais, como garantir que um paciente já cadastrado não seja cadastrado novamente, etc.

## Informações gerais:

* Prazo: 27/04/2023;
* Grupos de no máximo 3 pessoas;
* Compactar todos os arquivos .java num único arquivo .zip e enviar para o e-mail victor.silva@professores.ibmec.edu.br;
* Incluir o nome de todos os participantes no e-mail enviado.
