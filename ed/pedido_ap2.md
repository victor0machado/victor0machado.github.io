# IBM3114 - Estruturas de Dados - Pedido da AP2

## Contexto

Continuando o sistema de pedidos do McRonald's, faça algumas evoluções para melhorar a eficiência e a sua usabilidade. Para continuar o projeto, utilize o [gabarito fornecido](https://github.com/victor0machado/ed-2023.2/tree/main/ap1).

## Requisitos

Neste momento, existem alguns requisitos funcionais (novos recursos) e outros não funcionais (melhorias na implementação).

* Requisitos funcionais
    * O programa deve incluir a opção de atualizar um produto, modificando o seu preço. O id, o nome e a descrição devem ser mantidos;
    * O programa deve incluir uma nova métrica, chamada *ticket médio*, que calcula o valor médio de cada pedido (total faturado até o momento, dividido pelo número de pedidos já encerrados);
    * O programa deve incluir uma segunda forma de exibir os produtos, ordenados por nome, e não por id;
* Requisitos não funcionais
    * A estrutura de dados que forma a lista de produtos deve ser uma transformada em uma lista simplesmente encadeada. Todas as operações sobre essa lista (adicionar, buscar, excluir, atualizar, exibir etc.) devem ser refatorados para considerar uma lista encadeada;
    * Não há restrição do algoritmo de ordenação utilizado para a exibição dos produtos ordenados pelo nome (pode ser o bubblesort, por exemplo).

Além disso, após os testes iniciais pelo cliente, foram identificados dois bug que precisam ser corrigidos, cujos cenários de teste são os seguintes:

### Bug 1

1. Selecione a opção 6 (adicionar pedido);
2. Insira valores quaisquer para um pedido (p.ex., `s`, depois `1 1` e depois `0 0`);
3. Selecione a opção 7 (expedir pedido);
4. Selecione a opção 7 (expedir pedido).

O programa cai num `panic` e não consegue resolver essa operação. O comportamento desse cenário deve ser idêntico ao caso em que se insere a opção 7 (expedir pedido) assim que o programa é aberto.

### Bug 2

1. Abra o programa, utilizando o arquivo de dados (`dados.csv`) fornecido;
2. Selecione a opção 5 (exibir os produtos);
3. Você verá três produtos criados;
4. Selecione a opção 1 (cadastrar novo produto);
5. Insira quaisquer valores para nome, descrição e preço;
6. Selecione a opção 5 (exibir os produtos).

O programa lista todos os produtos, porém o `id` do produto criado manualmente é 1, e não 4. Ou seja, o programa não está considerando os ids dos produtos pré-carregados.

## Critérios de aceitação

Para o sistema ser aceito pelos clientes, as seguintes condições devem ser satisfeitas:

* O sistema precisa ser desenvolvido na linguagem Go;
* O projeto deve ser entregue no seu formato de código fonte, bem como um executável (.exe), construído a partir do fonte;
* O sistema deve ser entregue em um repositório privado no GitHub, adicionando um dos sócios (@victor0machado) como colaborador;
* O repositório possui um arquivo readme.md, descrevendo as pessoas da equipe e como utilizar o programa (comandos aceitos, exemplos de respostas, etc.);

O não atendimento de algum dos critérios de aceitação pode acarretar em penalização na solução. É recomendado utilizar o mesmo repositório já criado para a fase anterior do projeto.

## Critérios de avaliação

O sistema será avaliado pelos clientes segundo critérios objetivos e subjetivos, quais sejam:

* Testes funcionais (80%): os testes realizados pelos clientes não apresentam falhas. Ou seja, os requisitos funcionais detalhados acima estão sendo atendidos completamente;
* Avaliação estática do código (20%): o código é eficiente e bem escrito, está organizado, não apresenta redundâncias e atende às boas práticas de programação.

## Demais informações

* Prazo do projeto: até 27/11/2023, sem possibilidade de adiamento do prazo;
* Submissão do link do GitHub através do estudante.ibmec.br;
* Apenas uma pessoa de cada grupo precisa enviar o link;
* As equipes podem ser formadas por no mínimo 3 pessoas e no máximo 5.
