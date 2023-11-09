# IBM1737 - Programação Estruturada - Pedido da AP2 - Turma de Engenharia de Produção

## Descrição do projeto

O seu time deve desenvolver um notebook no Google Colab utilizando dados extraídos do Portal de Dados Abertos do Banco Central do Brasil (https://dadosabertos.bcb.gov.br/). Devem ser coletados os dados referentes aos anos de 2018 a 2022 para as seguintes categorias:

- Índice de Preços ao Consumidor-Amplo (IPCA) - Bens Não-duráveis
- Índice de Preços ao Consumidor-Amplo (IPCA) - Bens Semi-duráveis
- Índice de Preços ao Consumidor-Amplo (IPCA) - Bens Duráveis
- Índice de Preços ao Consumidor-Amplo (IPCA) - Serviços
- Taxa de Juros - Selic

A coleta de dados deve ser realizada através do pacote `requests` do Python. Deve ser implementada uma função que receba como entrada uma url a ser consultada, e que retorne um dicionário contendo os dados coletados em caso de sucesso, e `None` em caso de falha.

Para cada categoria, deve-se considerar apenas um dado por mês. Caso a fonte dos dados apresente mais de um dado no mês, considere o mais próximo do início do mês. Consolide todos esses dados em um único dicionário cujas chaves possuam o formato `mm/aaaa` e os valores contenham todas as informações solicitadas. O trabalho de consolidação dos dados também deve ser incluído em uma função separada, que recebe todos os dados baixados como entrada, e retorna o dicionário devidamente formatado.

O programa deve salvar em um arquivo .json o dicionário formatado. Crie uma função que recebe um dicionário como entrada, e um nome de arquivo, e cria esse arquivo contendo o dicionário como conteúdo.

Em seguida, estude a documentação das bibliotecas **Pandas** (https://pandas.pydata.org/) e **Matplotlib** (https://matplotlib.org/) para fazer o seguinte:

- Apresentar, no notebook, um DataFrame contendo as informações salvas no dicionário formatado;
- Traçar um gráfico de colunas indicando as quatro categorias do IPCA ao longo do ano de 2020;
- Traçar um gráfico de linha indicando a progressão da taxa Selic durante o ano de 2021.

O notebook deve ser organizado em células coerentes, separadas pelos conteúdos dos códigos. Utilize células de texto para justificar e explicar o processo de raciocínio para a implementação dos códigos e obtenção dos dados.

## Avaliação

Os projetos serão avaliados de acordo com os seguintes critérios:

* Qualidade do código (20%): código de acordo com os padrões de escrita, algoritmos bem estruturados e arquitetura bem organizada;
* Testes realizados pelo professor não apresentam falhas e requisitos foram atendidos integralmente (80%);

## Informações gerais:

* Prazo: entrega até 23/11/2023 (impreterivelmente);
* Grupos de no mínimo 2 e no máximo 4 pessoas;
* Método de entrega: via Sala de Aula Virtual (estudante.ibmec.br). Formato de entrega:
  * Criar um notebook Google Colab no Google Drive;
  * Compartilhar e configurar o compartilhamento para que qualquer pessoa com o link possa **editar** (não apenas ler);
  * Subir no estudante o link para o notebook;
  * Entregas fora do padrão solicitado serão penalizadas!
