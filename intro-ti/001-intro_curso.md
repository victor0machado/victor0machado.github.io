# Introdução ao curso

Neste material discutimos sobre alguns tópicos introdutórios ao curso e à carreira de um programador de software, e vamos entender o porquê a programação é um conhecimento fundamental para os próximos anos.

### Índice

1. [Afinal, o que é programar?](#afinal-o-que-é-programar)
2. [Linguagens de programação](#linguagens-de-programação)
3. [Por que aprender a programar?](#por-que-aprender-a-programar)
4. [Sugestões de conteúdos](#sugestões-de-conteúdos)

## Afinal, o que é programar?

### Um pouco de história...

Os computadores como conhecemos hoje, eletrônicos e de uso geral, surgiram na década de 1940, com o ENIAC (_Eletronic Numerical Integrator and Computer_). Este computador começou a ser desenvolvido no final da II Guerra Mundial para cálculos balísticos de grande complexidade, mas ele só entrou em operação após o final da guerra. Ele pesava cerca de 30 toneladas e ocupava uma sala inteira de 10m x 15m.

Para que ele funcionasse, era necessário dezenas de pessoas (normalmente mulheres, chamadas de computadores humanos), que percorriam longas filas de interruptores. Cada interruptor representava um valor binário, 0 ou 1, conforme ele estivesse desligado ou ligado, respectivamente. A sequência de interruptores possibilitava que o ENIAC processasse os cálculos inseridos pelos computadores humanos. Era possível realizar até 5000 somas por segundo, ou 300 multiplicações (para referência, em computadores modernos esse número está na casa dos trilhões).

Essa operação de configurar o computador para que ele realizasse as operações desejadas é chamada de **programação**. Conceitualmente, hoje ainda fazemos a mesma coisa que os computadores humanos faziam na década de 1940: passamos instruções específicas para o computador, para que ele possa apresentar um comportamento específico. Na prática, temos algumas diferenças entre a programação contemporânea e a programação nos primeiros computadores eletrônicos.

### Um computador para cada programa

O ENIAC e outros computadores à sua época eram considerados com programas fixos, ou seja, eles executavam exatamente as mesmas operações definidas no momento do seu projeto. Uma alteração simples no programa do ENIAC significava religar os componentes eletro-eletrônicos, o que poderia demorar até três semanas para que ele começasse a trabalhar. Guardadas as devidas proporções, o ENIAC era como uma calculadora de mesa tradicional: era possível realizar operações matemáticas e até mesmo cálculos complexos, mas era inviável desenvolver uma solução de editor de textos, por exemplo.

O matemático John von Neumann, um dos construtores do ENIAC, percebeu essa limitação e propôs uma arquitetura de tal forma que o programa e os dados processados seriam armazenados em um mesmo lugar, a memória do computador. Essa solução possibilitou o desenvolvimento de **computadores de programas armazenados**. Um computador dessa categoria inclui, inicialmente, um conjunto de instruções, e pode armazenar na memória um outro conjunto de instruções (programa) que detalha o cálculo a ser realizado. A arquitetura de von Neumann ainda permite que os programas possam se modificar durante a execução. Ela ainda é a arquitetura usada nos computadores modernos, apesar de já haverem discussões em torno de outras arquiteturas, como a do computador quântico.

### Programando com zeros e uns

O processo de programação no ENIAC e em computadores similares era, claramente, pouco produtivo. Codificar um programa era algo muito similar à forma que as telefonistas estabeleciam conexões entre diferentes telefones. Mesmo que o processo de configuração dos interruptores fosse simplificado, o programador ainda precisaria codificar o seu programa em valores binários, zeros e uns. Isso criava uma barreira enorme no entendimento e na disseminação do conhecimento da programação de computadores, fazendo desse trabalho algo de nicho, específico a grandes corporações e a entidades governamentais.

Com a arquitetura de von Neumann e o conceito de computadores de programas armazenados, surgiram computadores que possibilitavam a simplificação do processo de programação. Em 1951, o UNIVAC I se tornou o primeiro computador comercialmente disponível que utilizava o conceito de programa armazenado. Em 1952, uma das pessoas que participou do time que projetou o UNIVAC I, Grace Hopper, desenvolveu o programa **A-0** que convertia instruções simples em inglês em código de máquina. Este programa é considerado o primeiro **compilador**, e revolucionou o processo de programação. A partir deste momento não era mais necessário programar um computador utilizando zeros e uns: bastava inserir alguns comandos pré-definidos em inglês, que um outro programa armazenado no computador fazia a conversão para o código da máquina.

### Programando nos tempos modernos

Com a criação dos compiladores e a constante evolução tanto dos hardwares, quanto dos softwares desenvolvidos, o processo de programação se tornou muito mais simples. Em essência, sua definição continua a mesma: **programar um computador significa fornecer à máquina um conjunto de instruções que indica o que você quer que ela faça**. Se você está desenvolvendo um aplicativo de mensagens e precisa criar um botão "enviar", você define uma série de instruções que devem ser executadas pelo computador na sequência correta, de forma a realizar o envio da mensagem de um celular para outro. A programação atual, então, passa por acessar as características e funcionalidades internas do computador, de forma a ser capaz de usá-las.

A programação se resume a uns poucos conceitos fundamentais:

- _Entrada de dados_: define de que forma a máquina obtém informações, que podem ser recebidas via teclado, arquivos, rede, mouse ou outros dispositivos. Essas informações tanto podem estar sendo produzidas por usuários humanos quanto por outros dispositivos;
- _Saída de dados_: define como a máquina apresenta respostas ao mundo externo, que podem ser exibidas através de um monitor, impressora ou outros dispositivos. Da mesma forma que as entradas, as saídas podem ser enviadas usuários humanos ou a outros dispositivos.
- _Processamento_: define como os dados de entrada são transformados e combinados com outras informações eventualmente já armazenadas pela máquina, ou obtidas por ela, para produzir as saídas. O processamento segue uma lógica de execução que é conhecida como “algoritmo”. Um algoritmo é basicamente uma lista finita de instruções que resolve um problema específico e se estrutura a partir de:
  - _Comandos_: instruções individuais que o programador dá à máquina e que ela é capaz de executar;
  - _Seleção_: estruturas que permitem à máquina decidir quando executar uma determinada lista de comandos ou outra;
  - _Repetição_: estruturas que permitem à máquina repetir uma lista de comandos um número fixo de vezes ou até que uma determinada condição seja obtida.

## Linguagens de programação

O conceito de compiladores criado inicialmente por Grace Hopper trouxe para os programadores uma nova perspectiva sobre como programar. A partir de então, já não era mais necessário desenvolver código em linguagem de máquina, ou seja, zeros e uns. Os conjuntos pré-definidos de instruções em inglês (ou qualquer outro idioma), que são traduzidos pelo compilador, passaram então a ser chamados de **linguagens de programação**. Alan Turing, considerado hoje um dos pais da computação moderna, também esteve interessado na programação das operações de um computador. Turing estava convencido de que operações de cálculo eram apenas a ponta do iceberg em termos de utilização dos computadores. Ele elaborou tabelas de instruções que automaticamente converteriam a escrita decimal em códigos binários, que poderiam ser lidos pelas máquinas.

As linguagens que utilizavam, então, os conceitos propostos por Hopper e Turing, foram chamadas de **linguagens de alto nível**, ou seja, linguagens que são facilmente lidas e interpretadas por seres humanos, em oposição às linguagens de máquina, denominadas de **linguagens de baixo nível**. Atualmente, programadores de linguagens de baixo nível são pouquíssimos, sendo altamente especializados e focados em situações muito específicas, ligadas ao controle das funções mais básicas da máquina.

Apesar de terem existido linguagens de alto nível anteriores, a primeira a ser comercializada foi o **FORTRAN**, em 1957. O FORTRAN teve diversas versões e atualizações ao longo dos anos, e em 2022 está na 23ª posição no índice TIOBE, que mede a popularidade de linguagens de programação. Sua aplicação hoje se restringe a cálculos complexos e que exijam alto desempenho e precisão. Outras linguagens criadas nas décadas de 1950 e 1960 que são usadas até hoje incluem o COBOL (usado em praticamente todos os sistemas bancários governamentais) e o BASIC (suas versões mais recentes ainda são muito usadas para aplicações desktop). Dentre as linguagens compiladas mais populares atualmente, temos C e C++

Um pouco depois, em 1958, surgiu a linguagem **LISP**, a primeira **linguagem interpretada**. Ao invés das linguagens compiladas, como o FORTRAN, uma linguagem interpretada não exige uma "tradução" prévia do código. Ao invés de um compilador, entra em cena um interpretador, que lê cada linha do código inserido e a executa independentemente. Nas linguagens interpretadas mais populares hoje em dia, podemos mencionar Python, Ruby e Lua.

Linguagens compiladas tendem a ser, usualmente, mais eficientes que linguagens interpretadas, já que, no momento da execução do código, este já foi traduzido para linguagem de máquina e não precisa ser processado em alto nível. Como nas linguagens interpretadas essa tradução é em tempo real, isso causa um custo computacional que pode reduzir sua eficiência. Por outro lado, linguagens interpretadas tendem a permitir uma melhor análise linha a linha do código, já que é possível executá-las separadamente, estudando os seus resultados e permitindo modificações sem a necessidade de recompilar todo o código.

### Linguagens formais

Existe uma diferença fundamental entre a linguagem humana (ou natural) e as linguagens de programação. Os seres humanos são capazes de compreender expressões mesmo que elas não estejam escritas corretamente. Considere, por exemplo, a frase "Olá! Td bem c vc?". Um ser humano (que entenda português, claro) compreende facilmente que, nesse contexto, "td" significa "tudo" e "c vc" significa "com você". Com os computadores, no entanto, não há essa análise de contexto. A não ser que ele seja programado para entender que "vc" e "você" são a mesma coisa em uma linguagem, é necessário utilizar aquilo que está previsto na sua documentação.

Ou seja, programas são escritos em uma linguagem formal. Cada letra e cada sinal matemático ou de pontuação têm um significado muito preciso. Mudar qualquer um destes sinais pode, muitas vezes, mudar o sentido do programa, ou até fazê-lo parar de funcionar. No caso do Python, linguagem que usaremos nesse curso, até mesmo um espaço mal colocado pode significar uma mudança radical no comportamento. Portanto, sempre tome cuidado com a forma com que as informações estão sendo construídas dentro do código.

## Por que aprender a programar?

É indiscutível que, atualmente, computadores fazem parte da nossa vida. No entanto, apesar de hoje sermos grandes utilizadores de computadores, dos celulares na nossa mão aos aviões em que embarcamos para viajar, a maiora das pessoas simplesmente ignora o funcionamento interno dessas máquinas.

As pessoas confiam quase que cegamente na tecnologia que lhes é apresentada. Muitos utilizam, no dia-a-dia, computadores para ler e enviar e-mail, preencher planilhas e elaborar relatórios. Mas como as mensagens são enviadas de uma conta de e-mail para a outra? Como uma célula de uma planilha consegue realizar uma operação de soma? Como o processador de texto entende quando uma palavra foi digitada incorretamente? Quem entende os princípios básicos de programação pode ter a real consciência do que está acontecendo por trás desses programas, e poderá ser capaz, inclusive, de modificar esses processos para obter resultados diferenciados.

Muitos profissionais poderão precisar de cálculos especiais para os dados que estão utilizando, sejam eles números ou textos, e nem sempre os aplicativos disponíveis no mercado oferecem as funções necessárias. Uma pessoa que saiba programar poderá criar praticamente qualquer função de que necessite de forma muito mais flexível, sem depender de aplicativos específicos. Alguém que saiba programar ainda pode modificar aplicativos existentes, de forma a provocar comportamentos específicos que não ocorreriam normalmente.

Além das possibilidades apresentadas, que podem favorecer praticamente qualquer profissional em um escritório hoje em dia, talvez um dos maiores motivos para se aprender programação hoje em dia seja porque a sociedade **precisa** de cada vez mais programadores. O número de computadores circulando no mercado é gigantesco, variando desde geladeiras a carros autônomos, passando por celulares, relógios e televisores, e chegando a satélites e ônibus espaciais. A demanda pelo desenvolvimento de software tem crescido exponencialmente desde que a computação contemporânea surgiu, nas décadas de 1940 e 1950, e não dá sinais de estar desacelerando.

Então, por que tão poucas pessoas aprendem a programar? A resposta talvez esteja no fato de que, para ser realmente compreendida, uma linguagem de programação precisa ser aplicada. Da mesma forma que ler um livro ou assistir a um curso teórico que explique a gramática e a sintaxe de uma língua estrangeira não é suficiente para que uma pessoa se torne fluente, apenas assistir a um curso de programação não torna uma pessoa programadora. Para uma língua estrangeira, é preciso não apenas saber sua gramática e sintaxe, mas também resolver pequenos problemas, como pedir um copo d'água ou informações sobre um determinado percurso. Com programação é o mesmo: é necessário muita prática, esbarrar em alguns obstáculos, entendê-los e eliminá-los. Aos poucos a pessoa adquire fluência e terá desenvoltura para escrever códigos complexos e sofisticados usando uma linguagem de programação.

## Sugestões de conteúdos

* Filmes:
  * [O Jogo da Imitação](https://www.primevideo.com/detail/0RE594TD30MV9KITHPFBQ312IA/ref=atv_dp_share_cu_r) (Prime Video), que conta a história de como Alan Turing foi essencial para antecipar o encerramento da II Guerra Mundial;
  * [Estrelas Além do Tempo](https://www.disneyplus.com/pt-br/movies/estrelas-alem-do-tempo/2xa2YdiOJXQt) (Disney+), fala sobre os bastidores da NASA na década de 1960 sob a perspectiva de três mulheres que atuaram em diferentes frentes no desenvolvimento tecnológico que fizeram o homem chegar à Lua em 1969.
* Livros:
  * WAZLAWICK, R.S. [História da Computação](https://www.amazon.com.br/Hist%C3%B3ria-Computa%C3%A7%C3%A3o-Raul-Sidnei-Wazlawick-ebook/dp/B01JMAC3F8/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=HG6K4QWB6SEJ&keywords=hist%C3%B3ria+da+computa%C3%A7%C3%A3o&qid=1646582183&sprefix=hist%C3%B3ria+da+computa%C3%A7%C3%A3%2Caps%2C203&sr=8-1). Rio de Janeiro: Elsevier, 2016.
* Material online:
  * [TecMundo - A história do ENIAC](https://www.youtube.com/watch?v=dy0wpDfnpzo);
  * [Biografia de Grace Hopper](https://president.yale.edu/biography-grace-murray-hopper), pela Universidade Yale, onde ela cursou seu PhD;
  * [Evolução das linguagens de programação entre 1965 e 2019](https://www.youtube.com/watch?v=Og847HVwRSI).
