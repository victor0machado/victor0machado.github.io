# IBM0516 - Programação Orientada a Objetos

Vou colocar nessa página links das aulas e materiais adicionais referentes à disciplina.

* [GRID](grid.md)

## Material geral

* [Slides da disciplina](/./assets/poo/slides.pdf)
* [Exercícios de fundamentos](./exercicios/001-exercicios_fixacao.md)
* [Conteúdo da disciplina no github](https://github.com/victor0machado/poo-2023.2)
* [Gabaritos das ACs](https://github.com/victor0machado/poo-2023.2/tree/main/gabaritosACs)
* [Pedido da AP1](./pedido_ap1.md)
* [Pedido da AP2](./pedido_ap2.md)

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

### AC3

1. Considere o seguinte pedido de projeto. A partir desse requisito, implemente pelo menos três classes, detalhando seus atributos e métodos.

    Desenvolva um sistema de gestão de eventos universitários. O sistema deve permitir o cadastro de eventos com detalhes como nome, data, local e número máximo de participantes, além de possibilitar a inscrição de alunos em eventos, inclusive com informações adicionais para eventos específicos. Um painel de controle também é desejado para visualizar eventos futuros, palestrantes e disponibilidade de vagas. O objetivo é simplificar a administração e melhorar o engajamento dos alunos por meio de uma solução tecnológica eficiente.

### AC4

1. Implemente uma solução em Java para o seguinte problema:

    Nossa biblioteca está buscando modernizar o sistema de reservas de livros e recursos. Atualmente, enfrentamos desafios com a gestão de empréstimos e devoluções. Precisamos de um sistema que permita aos usuários reservar livros e verificar a disponibilidade. Além disso, alguns recursos especiais, como e-books, não podem ser emprestados, apenas reservados para leitura online. Tanto livros físicos quanto e-books precisam constar título e autor. Os e-books também devem registrar o formato, que pode ser ePub ou PDF. Desenvolva classes para livros físicos e e-books e inclua uma herança entre essas classes para agregar informações comuns. Para testar o projeto, considere a seguinte classe principal:

    ``` java
    public class App {
        public static void main(String[] args) {
            LivroFisico livro1 = new LivroFisico("Aventuras em Java", "João Autor");
            Ebook ebook1 = new Ebook("Programação Java Avançada", "João Autor", "PDF");

            livro1.emprestar(); // Vai exibir um texto dizendo que o livro precisa ser reservado primeiro.

            // As mensagens abaixo devem exibir na tela que os livros foram reservados com sucesso
            livro1.reservar();
            ebook1.reservar();

            ebook1.cancelarReserva(); // Deve dizer que a reserva foi cancelada


            livro1.emprestar(); // Vai informar que o livro foi emprestado com sucesso
            livro1.emprestar(); // Vai exibir um texto dizendo que o livro já está emprestado
            livro1.devolver(); // Vai exibir um texto dizendo que o livro foi devolvido
        }
    }
    ```

### AC5

Implemente um CRUD para uma classe Aluno. A classe possui os atributos `nome`, `curso` e `matricula`, todos do tipo `String`. O CRUD precisa ter operações para:

- Adicionar um novo aluno à estrutura;
- Remover um aluno da estrutura, a partir da matrícula;
- Atualizar o curso de um aluno, a partir da matrícula;
- Listar as informações de um aluno, a partir da matrícula;
- Listar todos os alunos.

Escolha a estrutura de dados mais adequada para o caso, e monte uma classe de teste para validar o funcionamento do CRUD. Não é necessário montar uma interface com o usuário.

Esta atividade pode ser feita em dupla.

### AC6 - Estudo Dirigido

Leia a [nota de aula 09](./notas_aula/009-persistencia_dados.md) e a [nota de aula 10](./notas_aula/010-mais_dados_operacoes.md). Após a leitura, faça o exercício pedido abaixo:

Evolua o exercício feito na AC anterior. Monte na classe principal do programa uma interface por linha de comando que faça o seguinte:

- Ao iniciar o programa, carregue um arquivo de texto com dados pré-configurados de alunos, e alimente a lista de alunos;
- Ao encerrar o programa, salve a lista de alunos em um arquivo de texto (pode ser o mesmo arquivo);
- Tenha opções para incluir, remover, editar ou listar alunos. Considere sempre a matrícula como identificador único de um aluno;

Mantenha as classes organizadas em pacotes adequados. Utilize o `StringBuilder` para compor dados do tipo `String` sempre que necessário. Utilize os métodos `equals` e `toString`, de forma a manter a interface com o usuário (scans e prints) fora das classes de entidades ou das classes DAO.

Esta atividade pode ser feita em dupla ou individualmente. Caso seja feita em dupla, apenas um aluno deve subir o trabalho no estudante.ibmec.br (lembrando de mencionar os nomes da dupla). A atividade terá peso 2 no cálculo da média de ACs ao final do semestre. O prazo para entrega é 05/11.

---

[Voltar](https://victor0machado.github.io/)
