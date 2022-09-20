# Pedido da AP1

## Pedido

Baseado no exercício iniciado na [nota de aula 05](./notas_aula/005-intro_uml.md) e continuado na [nota de aula 06](./notas_aula/006-conceitos_relacionais.md), continue o seu desenvolvimento, elaborando as seguintes atividades:

- Evolua o [modelo UML](https://drive.google.com/file/d/10tCu5qsdaT_GQvRYBJNIMl9FtzwQoTqa/view?usp=sharing), incluindo classes e associações necessárias para atender aos seguintes requisitos:
    - A agenda de um médico também deve em qual consultório o médico vai atender. Um consultório pertence a uma clínica, e deve conter apenas um telefone;
    - O sistema deve permitir emitir uma nota de cobrança para cada consulta, que possui como informações o dia da consulta, o CNPJ da clínica e quem deve fazer o pagamento. Uma nota de cobrança é gerada para um paciente no valor de R$400,00 ou R$200,00 em caso da consulta ser a primeira daquele paciente. Caso o paciente possua plano de saúde, a nota de cobrança deve ser direcionada para o plano, e possui valor de R$100,00 independente de ser a primeira consulta ou se ser uma consulta de revisão;
- Atualize o [código do projeto](https://replit.com/@victor0machado/nota06-exercicio#Main.java) para considerar as classes e associações indicadas no modelo evoluído;
- Atualize a classe `Main.java` e crie uma classe `CadastraDados.java` para realizar as seguintes operações:
    - Na classe `Main.java`, crie uma interface de texto que permita cadastrar até 5 pacientes, até 5 médicos, até 20 agendas e até 20 consultas, além de uma clínica. A classe também deve possibilitar exibir os dados armazenados, usando o índice no array como identificador do objeto;
    - Na classe `CadastraDados.java` implemente o processo de cadastro (pergunta informações como nome, CPF e e-mail do paciente) para os dados.

## Avaliação

O projeto será avaliado de acordo com os seguintes critérios:

* Qualidade de escrita do código: variáveis foram bem nomeadas, código está de acordo com os padrões discutidos em sala (_casing_, indentação, espaçamento, etc.);
* Qualidade da implementação: o código não apresenta redundâncias ou acoplamento excessivo. O projeto está bem organizado e os métodos estão implementados nas classes adequadas;
* Qualidade da interface de texto: a interface está organizada, as opções estão claras e não há confusão nas informações de dados;
* Testes realizados pelo professor não apresentam falhas.

Serão dados pontos extras para validações de dados adicionais, como garantir que um paciente já cadastrado não seja cadastrado novamente, etc.

## Informações gerais:

* Prazo: 09/10/2022
* Grupos de no mínimo 3 e no máximo 4 pessoas
* Compactar todos os arquivos .java num único arquivo .zip e enviar para o e-mail victor.silva@professores.ibmec.edu.br
* Incluir o nome de todos os participantes no e-mail enviado
