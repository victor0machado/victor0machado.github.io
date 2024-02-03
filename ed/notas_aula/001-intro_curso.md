# Introdução ao curso

Neste material discutiremos sobre a importância do entendimento de algoritmos e estruturas de dados na formação profissional de um desenvolvedor de software, e faremos um breve histórico da linguagem Golang, que será usada durante este curso. Por fim, traremos algumas opções de configurações de ambientes de desenvolvimento.

### Índice

- [Introdução ao curso](#introdução-ao-curso)
    - [Índice](#índice)
  - [O que são algoritmos e estruturas de dados?](#o-que-são-algoritmos-e-estruturas-de-dados)
    - [Sobre algoritmos](#sobre-algoritmos)
    - [O que são estruturas de dados?](#o-que-são-estruturas-de-dados)
  - [Sobre a linguagem Go](#sobre-a-linguagem-go)
    - [Vantagens e desvantagens](#vantagens-e-desvantagens)
  - [Configurando e preparando o ambiente de trabalho](#configurando-e-preparando-o-ambiente-de-trabalho)
    - [Configuração básica](#configuração-básica)
    - ["Olá, mundo"](#olá-mundo)
    - [Simplificando um pouco](#simplificando-um-pouco)
    - [Automatizando a execução dos programas em Go](#automatizando-a-execução-dos-programas-em-go)

## O que são algoritmos e estruturas de dados?

### Sobre algoritmos

Um algoritmo é um processo sistemático para a resolução de um problema. O desenvolvimento de algoritmos é particularmente importante para problemas a serem solucionados em um computador, pela própria natureza do instrumento utilizado.

Um algoritmo computa uma saída, o resultado do problema, a partir de uma entrada, as informações inicialmente conhecidas e que permitem encontrar a solução do problema. Durante o processo de computação o algoritmo manipula dados, gerados a partir da sua entrada.

Parte do trabalho diário de quem desenvolve software é entender e descrever as etapas necessárias para que o computador tenha condições de executar aquilo que foi planejado inicialmente. Além disso, não basta que o programa desenvolvido seja eficaz -- ele também precisa ser eficiente. Este segundo aspecto é, hoje em dia, muitas vezes subestimado, haja vista a alta capacidade de processamento dos computadores modernos. Independentemente da complexidade do algoritmo, as chances são de que a máquina do usuário consiga processar o código normalmente, sem muitos problemas.

No entanto, considerando que muitas das aplicações em produção estão rodando na nuvem, a preocupação por eficiência tem que ser levada em consideração. Uma melhoria de eficiência de 10% em um algoritmo, se considerar a larga escala do número de transações processadas na nuvem, pode provocar uma redução significativa de custos.

Essa preocupação por eficiência fica mais acentuada em casos que envolvam computação de alto desempenho, como por exemplo processamento de imagens para visão computacional, desenvolvimento de jogos AAA ou aplicações em dispositivos embarcados com capacidade limitada.

### O que são estruturas de dados?

Estruturas de dados nada mais são que padrões e técnicas de organização e agrupamento de conjuntos de dados. Durante o processo de desenvolvimento, é comum ter que ler, armazenar e processar grandes volumes de dados. Para que isso possa ser feito de forma eficiente, é necessário adotar um padrão para que esses dados possam ser processados dentro da memória do computador. A linha de pesquisa em Algoritmos e Estruturas de Dados estuda como realizar essas ações no menor tempo possível.

É importante, para o desenvolvedor, conhecer os tipos mais comuns de estruturas de dados, seus algoritmos básicos e as suas possíveis aplicações em projetos. O desenvolvedor deve conseguir analisar um problema e um projeto e decidir pela melhor estrutura de dados aplicável para este problema, de forma a reduzir, sempre que possível, a complexidade do algoritmo desenvolvido.

Para o estudo de estruturas de dados e algoritmos, é interessante aplicarmos uma linguagem de programação que tenha um baixo nível de abstração, de forma a entendermos cada etapa dos algoritmos estudados. Dessa forma, utilizar linguagens como Python dificulta o entendimento do conteúdo, já que boa parte dos algoritmos já é abstraída pela própria linguagem.

## Sobre a linguagem Go

Nesta disciplina, optei por adotar a linguagem Go (ou Golang). Esta linguagem foi lançada em 2007 pelo Google, como forma de resolver alguns problemas ao desenvolver sistemas, particularmente aqueles executados em processadores com múltiplos núcleos, sistemas distribuídos e softwares altamente escaláveis, com um grande volume de transações.

Linguagens como Python possibilitam o desenvolvimento de código extremamente simples e fácil de ler e manter, porém a linguagem tende a não desempenhar bem com um volume muito grande de transações. Por outro lado, linguagens como C ou C++, apesar de serem extremamente eficientes, possuem dificuldades com relação à sua aplicação em sistemas web, com um baixo número de bibliotecas pré-definidas e ainda uma complexidade elevada para manutenção e evolução.

Tendo isso em vista, uma equipe do Google, liderada por Robert Griesemer, Rob Pike e Ken Thompson, atuou no desenvolvimento de uma nova linguagem, que possa ser aplicável em larga escala e ainda tenha uma alta eficiência. A linguagem se tornou open source em 2009, e em 2010 passou a ser adotada por desenvolvedores fora do Google.

### Vantagens e desvantagens

Dentre as principais vantagens da linguagem, é possível citar:

* É uma linguagem compilada
* Possui garbage collector
* Sintaxe simples
* Possui um ótimo pacote padrão, com vários módulos pré-definidos
* É multiplataforma
* Linguagem de tipagem estática
* Fortemente tipada
* Possui execução concorrente
* Suporte a ponteiros

Entretanto, existem algumas desvantagens sobre a linguagem. Apesar de muitos afirmarem que Go possui suporte a orientação a objetos, a verdade é que Go não é OO. Em seu lugar, a linguagem suporta **tipos**, que são criados usando a instrução `struct`, de forma bem similar à linguagem C. Com os tipos, é possível simular algumas operações como criação de métodos e definição de atributos. Porém, vários conceitos de OO importantes se perdem, como herança e polimorfismo.

Outras funcionalidades comuns em outras linguagens não estão presentes em Go, como tratamento de erros e assertions. Porém, a linguagem possui recursos e proteções para não depender dessas operações.

## Configurando e preparando o ambiente de trabalho

### Configuração básica

Para instalar o Go no computador, basta fazer o download na [página oficial da linguagem](https://go.dev/dl/), conforme o seu SO e arquitetura. Realize a instalação do arquivo normalmente. Eu recomendo que a instalação seja feita na raiz do seu diretório principal (p.ex., `C:\go`).

Lembre-se de adicionar as pastas `C:\go` e `C:\go\bin` (ou as equivalentes que você tenha instalado) ao PATH nas variáveis de ambiente da sua conta (ou equivalente no caso de MacOS). Para isso, basta clicar no ícone do Windows e digitar "Variáveis de Ambiente da sua Conta". Em seguida, selecione a variável `PATH` e clique em "Editar". Inclua os caminhos indicados anteriormente e clique em "Ok" nas duas janelas.

Após isso, inicie o seu VSCode. Eu recomendo a instalação da extensão da própria linguagem, [desenvolvida pelo time de Go no Google](https://marketplace.visualstudio.com/items?itemName=golang.Go).

### "Olá, mundo"

Com tudo instalado e configurado, vamos rodar um "Olá, mundo" para ver se não houve problemas. Inicie uma nova pasta no VSCode e crie um arquivo `olaMundo.go`. Neste arquivo, entre com o seguinte código:

``` go
package main

import "fmt"

func main() {
	fmt.Println("Olá, mundo!")
}
```

Abra o terminal e entre com o comando:

``` cmd
go build olaMundo.go
```

Este é o comando básico para "buildar" (ou construir) um binário em Go. Go é uma linguagem compilada, como C e C++, e portanto é necessário compilar o código antes de executá-lo. No terminal, chame o arquivo executável (basta digital `olaMundo.exe`) e você verá a mensagem aparecer na tela. Tudo funcionando!

### Simplificando um pouco

Apesar de ser sempre necessário compilar o código antes de executá-lo, o Go possui um "atalho" que simplifica um pouco as coisas. O comando `go run` automaticamente compila o código e executa o binário gerado, sem a necessidade de inserir dois comandos.

O que acontece é que o Go armazena o binário do programa em uma pasta temporária no computador (normalmente o caminho `C:\Users\seu_usuario\go\tmp`). É comum que o antivírus da máquina [bloqueie a execução do arquivo binário](https://stackoverflow.com/questions/75481994/vscode-go-compilation-blocked-by-antivirus). Caso isso aconteça, adicione a pasta temporária à lista de exceções do seu antivírus.

Feito isso, basta rodar o seguinte comando no terminal:

``` cmd
go run olaMundo.go
```

O terminal deve exibir a mensagem normalmente na tela.

### Automatizando a execução dos programas em Go

Utilizando o VSCode, podemos melhorar a execução dos nossos programas através das tarefas. Podemos criar duas tarefas: uma para executar apenas um arquivo .go e outra para executar um pacote Go, através de seu arquivo principal (normalmente `main.go`).

Para isso, navegue até a pasta `C:\Users\seu_usuario\AppData\Roaming\Code\User` no seu computador e crie um arquivo `tasks.json` (ou edite o já existente). Também é possível acessar este arquivo diretamente no VSCode, digitando ctrl+shift+P e selecionando o comando `Tasks: Open User Tasks`.

No arquivo `tasks.json`, insira o seguinte:

``` json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "go: executar arquivo",
            "type": "shell",
            "command": "go",
            "args": [
                "run",
                "${file}"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        },
        {
            "type": "shell",
            "label": "go: executar pacote",
            "command": "go",
            "args": [
                "run",
                "main.go"
            ],
            "problemMatcher": [
                "$go"
            ],
            "group": "build",
            "detail": "cd {workspaceFolder}"
        }
    ]
}
```

Este JSON descreve as duas tarefas que estamos querendo criar. O próximo passo é definir qual é a tarefa padrão para ser executada usando o atalho. Para isso, entre com ctrl+shift+P novamente e pesquise por `Tasks: Configure Default Build Task`. Como no início do curso estaremos trabalhando com arquivos isolados, selecione a tarefa `go: executar arquivo`. Futuramente, quando começarmos a trabalhar com pacotes, passaremos para a próxima tarefa.

Tendo tudo configurado, volte para o arquivo `olaMundo.go` que você criou, e lá execute o atalho ctrl+shift+B. Este arquivo executa o comando de build e execução do binário gerado.

Agora sim, estamos prontos para começar o curso!
