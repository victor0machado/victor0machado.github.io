# IBM0516 - Programação Orientada a Objetos

Vou colocar nessa página links das aulas e materiais adicionais referentes à disciplina.

* [GRID](grid.md)

## Material geral

* [Slides da disciplina](/./assets/poo/slides.pdf)
* [Exercícios de fundamentos](./exercicios/001-exercicios_fixacao.md)
* [Conteúdo da disciplina no github](https://github.com/victor0machado/poo-2023.2)
* [Gabaritos das ACs](https://github.com/victor0machado/poo-2023.2/tree/main/gabaritosACs)

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
* [10 - Mais tipos de dados e operações em Java](./notas_aula/010-mais_dados_operacoes.md)
* [11 - Tratamento de exceções](./notas_aula/011-erros_excecoes.md)

## Pedidos das ACs

Antes de começar:

* Crie um repositório para a disciplina no Github;
* Garanta que o repositório esteja público;
* Sempre que entregar uma AC, envie o link do repositório via SAVA (estudante).

### AC1

Faça todos os exercícios em um único projeto Java, separando por métodos cada um.

1. Faça um método que receba como parâmetros as três notas da disciplina (AP1, AP2 e AC) e mostre a média. A média é calculada de acordo com a fórmula M = (AP1 + AP2) * 0.4 + AC * 0.2.
2. Implemente um método que exiba todos os números de 150 a 200.
3. Elabore um método `ePrimo(int num)` que retorna se um número `num` é primo ou não. Caso o número não seja primo, liste todos os números pelos quais ele é divisível.
4. Implemente um método que receba como parâmetro um número inteiro e exiba o dia correspondente da semana (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer o texto "valor inválido".
5. Elabore um método `eBissexto(int ano)` que receba como parâmetro um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

### AC2

* Faça todos os pedidos em uma única classe, `Main`;
* Estruture as funcionalidades em métodos;
* Use como referência a demonstração apresentada em sala (mas o resultado não precisa ficar igual!).

1. Desenvolva uma calculadora. Implemente métodos para as operações de soma, subtração, multiplicação e divisão, que retornem os respectivos resultados;
2. Implemente uma interface por linha de comando, em que o programa pede um número, em seguida pede para escolher uma operação, pede um segundo número e apresenta um resultado;
3. Após o primeiro resultado exibido, o programa dá a opção do usuário limpar a memória e recomeçar o cálculo, ou escolher uma nova operação, para então pedir um outro número e calcular um novo resultado;
4. O programa continua nesse loop até o usuário pedir para sair (escolha uma mensagem para ser inserida pelo usuário, como `sair` ou `x`).

---

[Voltar](https://victor0machado.github.io/)
