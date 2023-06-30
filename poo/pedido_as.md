# Pedido da AS

## Pedido

Você foi requisitado para desenvolver uma solução de aluguel de filmes e séries em DVD e Blu-Ray. Os produtos devem armazenar informações como formato (DVD ou Blu-ray), gênero e ano de lançamento. Filmes devem armazenar ainda a duração, enquanto que séries devem armazenar o número de temporadas e o total de episódios. O sistema deve permitir o aluguel dos produtos, e deve armazenar a data da locação e uma flag se o produto está alugado no momento ou não. Considere que há apenas uma cópia de cada produto. Caso a devolução ocorra mais de 7 dias após a locação, o programa deve exibir uma mensagem "Produto em atraso! Deve pagar multa!".

Requisitos técnicos:

* Crie um `enum` para definir o formato do produto (DVD ou Blu-ray);
* Utilize herança para os dados dos produtos;
* Crie uma classe `Locação`, com métodos `alugar` e `devolver`;
* Todos os atributos devem ser privados, e todos os métodos públicos;
* Crie uma classe `Main` que adicione produtos a um `ArrayList` (não é necessário implementar funções para alugar ou devolver).

## Avaliação

O projeto será avaliado de acordo com os seguintes critérios:

* Qualidade de escrita do código: variáveis foram bem nomeadas, código está de acordo com os padrões discutidos em sala (_casing_, indentação, espaçamento, etc.);
* Qualidade da implementação: o código não apresenta redundâncias ou acoplamento excessivo. O projeto está bem organizado e os métodos estão implementados nas classes adequadas;
* Qualidade da interface de texto: a interface está organizada, as opções estão claras e não há confusão nas informações de dados;
* Testes realizados pelo professor não apresentam falhas.

## Informações gerais:

* Prazo: 30/06/2023;
* Trabalho individual;
* Compactar todos os arquivos .java num único arquivo .zip e enviar para o e-mail victor.silva@professores.ibmec.edu.br;
