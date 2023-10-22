# IBM3114 - Estruturas de Dados

Vou colocar nessa página links das aulas e materiais adicionais referentes à disciplina.

* [GRID](grid.md)
* [Slides da disciplina](/assets/ed/slides.pdf)
* [Soluções para problemas do SPOJ](https://github.com/victor0machado/ed-2023.2/blob/main/spoj/solu%C3%A7%C3%B5es.md)
* [Pedido da AP1](./pedido_ap1.md)

## Conteúdo complementar sobre Golang

* [Página oficial da linguagem](https://go.dev/)
* [Lista de extensões interessantes para o VS Code](https://preettheman.medium.com/awesome-vs-code-extensions-for-golang-1d88f951d6bd)
* [Curso interessante na Udemy](https://www.udemy.com/course/aprenda-golang-do-zero-desenvolva-uma-aplicacao-completa/)
* [Apostila sobre Golang do IME-USP](https://www.ime.usp.br/~gold/cursos/2015/MAC5742/reports/GoLang.pdf)
* [Guia de estilo da linguagem](https://google.github.io/styleguide/go/)
* [Curso sobre Golang do FreeCodeCamp.org](https://www.youtube.com/watch?v=un6ZyFkqFKo)
* [Arquivo de configuração do build para executar Go com o atalho Ctrl + Shift + B](/assets/ed/tasks.json)

## Conteúdos específicos das turmas

* [Gabaritos das ACs](https://github.com/victor0machado/ed-2023.2/tree/main/ac)
* [Turma 1 (segundas noite)](https://github.com/victor0machado/ed-2023.2/blob/main/turma_1)
* [Turma 2 (segundas e quartas 1º tempo manhã)](https://github.com/victor0machado/ed-2023.2/blob/main/turma_2)
* [Turma 3 (segundas e quartas 2º tempo manhã)](https://github.com/victor0machado/ed-2023.2/blob/main/turma_3)

## Pedidos da AC

### AC1

- Criar repositório no github para os exercícios da disciplina
- Fazer todos os exercícios em um único arquivo, separado por funções
- Submeter link via estudante

1. Elabore uma função `e_primo()` que retorna se um número é primo ou não. Caso o número não seja primo, liste todos os números pelos quais ele é divisível.
2. Implemente uma função `fibo()` que recebe um número e calcule o “n-ésimo” elemento da série de Fibonacci. A série de Fibonacci é dada de tal forma que um número em uma dada posição é igual à soma dos dois números anteriores. Considere que a série é formada pela sequência 1, 1, 2, 3, …
3. Implementa uma função que receba um número e exiba o dia correspondente da semana (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
4. Elabore uma função e_bissexto() que receba um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

### AC2

- Subir no mesmo repositório enviado para a AC1
- Fazer todo o projeto em um único arquivo
- Submeter link via estudante

1. Elabore um struct `Contato`, que deve conter os campos nome e e-mail. O struct deve conter um método para alterar o e-mail.
2. Elabore uma função `adicionaContato`, que recebe um contato e um array com até 5 elementos e inclui o contato no primeiro elemento vazio do array.
3. Elabore uma função `excluiContato`, que recebe um array de 5 elementos e elimina o último contato válido.
4. Elabore uma interface por linha de comando na função `main`, que cria um array de 5 elementos e permite a inclusão ou exclusão de contatos.

### AC3

- Subir no mesmo repositório enviado para as ACs anteriores
- Submeter link via estudante

Evolua o projeto desenvolvido na AC2 (utilize o gabarito fornecido), incluindo as seguintes modificações e funcionalidades:

1. Organize o projeto em pacotes: um pacote para o tipo `Contato`, um para a operação sobre os arrays e um arquivo `main.go`.
2. Refatore as funções que retornam arrays para que elas utilizem ponteiros.
3. Crie uma nova função `editaEmail`, que recebe o índice do elemento no array e altera o e-mail do elemento indicado.
4. Atualize a interface por linha de comando para incluir a opção de exibir todos os contatos salvos. Cada contato deve ser exibido em uma linha, precedido pelo número do índice daquele elemento.
5. Atualize a interface por linha de comando para poder editar o e-mail de um contato previamente salvo. A interface deve exibir os contatos armazenados e pedir para o usuário indicar o índice do contato que quer ser alterado. Em seguida, o programa pede o novo e-mail e chama a função `editaEmail`, implementada no exercício 3.

### AC4

- Subir no mesmo repositório enviado para as ACs anteriores
- Submeter link via estudante

Implemente o algoritmo da Torre de Hanói. O código deve ter uma função `main` e uma função `hanoi`. A função `main` deve chamar a função `hanoi` e, em seguida, informar pelo terminal o número de movimentos necessários para a solução da torre.

### AC5

- Subir no mesmo repositório enviado para as ACs anteriores
- Submeter link via estudante

Elabore um programa em Go que implemente e teste o seguinte problema:

- Dado um array de números inteiros positivos, considerado ordenado crescentemente, e um valor alvo, encontre um par de números no array cuja soma seja igual ao valor alvo. Se nenhum par for encontrado, retorne um valor (-1, -1) indicando que nenhum par foi encontrado. Resolva esse problema com um algoritmo cuja complexidade é O(n).

### AC6

Implemente um programa em Go que faça inserção de valores inteiros em uma lista alocada sequencialmente, de forma que a lista permaneça sempre ordenada. A solução final deve ser O(n). Caso precise utilizar alguma função de busca, escolha a de menor complexidade para o caso.

Exemplo do código:

``` go
package main

import "fmt"

const M = 5

func main() {
	var lista [M]int
	var n = 0

	insereOrd(&lista, &n, 4)
	fmt.Println(lista)

	insereOrd(&lista, &n, 12)
	fmt.Println(lista)

	insereOrd(&lista, &n, 2)
	fmt.Println(lista)

	insereOrd(&lista, &n, 6)
	fmt.Println(lista)

	insereOrd(&lista, &n, 17)
	fmt.Println(lista)

	insereOrd(&lista, &n, 1)
	fmt.Println(lista)
}

func insereOrd(v *[M]int, n *int, novoValor int) {

}
```

Exemplo de saída:

``` txt
tentando inserir 4
4 não encontrado, inserindo na lista
[4 0 0 0 0]
tentando inserir 12
12 não encontrado, inserindo na lista
[4 12 0 0 0]
tentando inserir 2
2 não encontrado, inserindo na lista
[2 4 12 0 0]
tentando inserir 6
6 não encontrado, inserindo na lista
[2 4 6 12 0]
tentando inserir 17
17 não encontrado, inserindo na lista
[2 4 6 12 17]
tentando inserir 1
Overflow
[2 4 6 12 17]
```

### AC7 - Estudo Dirigido 1

Para este estudo dirigido, estude os casos particulares de *listas circulares simplesmente encadeadas* e *listas lineares duplamente encadeadas*. A entrega deve ser composta de quatro arquivos:

* Um arquivo .md descrevendo uma lista circular, incluindo os seguintes algoritmos em pseudocódigo:
  * Exibição dos nós em uma lista circular;
  * Inserção de um nó no início da lista;
  * Exclusão do primeiro nó da lista;
* Um arquivo .md descrevendo uma lista duplamente encadeada com os seus nós *ordenados*, incluindo os seguintes algoritmos em pseudocódigo:
  * Exibição dos nós em uma lista duplamente encadeadas;
  * Busca de um nó;
  * Inserção de um nó;
  * Remoção de um nó;
* Dois arquivos .go, um para cada tipo de lista, com as implementações das estruturas e dos algoritmos citados.

Esta atividade pode ser feita em dupla ou individualmente. Caso seja feita em dupla, apenas um aluno deve subir o trabalho no estudante.ibmec.br (lembrando de mencionar os nomes da dupla). A atividade terá peso 2 no cálculo da média de ACs ao final do semestre. O prazo para entrega é 23/10.

### AC8 - Estudo Dirigido 2

Para este estudo dirigido, consulte os slides da disciplina sobre o assunto *Árvores Binárias de Busca* e resolva o exercício proposto, entregando um único arquivo .go, com os algoritmos implementados, os tipos (`struct`) para o nó e a árvore, e uma função `main` que testa a implementação realizada.

Esta atividade pode ser feita em dupla ou individualmente. Caso seja feita em dupla, apenas um aluno deve subir o trabalho no estudante.ibmec.br (lembrando de mencionar os nomes da dupla). A atividade terá peso 2 no cálculo da média de ACs ao final do semestre. O prazo para entrega é 06/11.

---

[Voltar](https://victor0machado.github.io/)
