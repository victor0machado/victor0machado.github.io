# IBM1737 - Programação Estruturada - Pedido da AP2 - Turmas de Tech

## Descrição do projeto

O seu time deve desenvolver um jogo **Caça ao Tesouro**, por linha de comando. Neste jogo, o jogador controla um aventureiro (representado pelo caractere `@`) que está em busca de um tesouro (representado pelo caractere `X`) localizado em um mapa 10 x 10. Enquanto percorre o mapa atrás do tesouro, o aventureiro pode se deparar com diversos itens e monstros!

### Comandos

O jogador possui os seguintes comandos possíveis, todos controlados pelo teclado:

- Teclas `W`, `A`, `S` e `D`: indicam a movimentação do aventureiro pelo mapa (respectivamente cima, esquerda, baixo e direita);
- Tecla `I`: Abre o menu de itens do aventureiro;
- Tecla `T`: Exibe os atributos do aventureiro;
- Tecla `Q`: Sai do jogo.

### Classes

O aventureiro é uma classe em Python, que possui os seguintes atributos e métodos:

- Atributos:
  - Nome: informado pelo jogador assim que o jogo começa;
  - Força: um inteiro aleatório entre 10 e 18;
  - Defesa: um inteiro aleatório entre 10 e 18;
  - Vida Máxima: um inteiro aleatório entre 100 e 120;
  - Vida Atual: um inteiro, inicialmente igual à Vida Máxima;
  - Mochila: uma lista de objetos do tipo `Item`, que se inicia vazia;
  - Posição: uma lista com dois elementos, inicializado como `[0, 0]`;
- Métodos:
  - Atacar: retorna um inteiro igual à força mais um valor aleatório entre 1 e 6;
  - Defender: recebe como parâmetro um valor de dano, e reduz desse valor a defesa do aventureiro. O valor final é reduzido da vida atual do aventureiro;
  - Mover: muda as coordenadas do aventureiro, na direção indicada;
  - Coletar item: recebe como parâmetro um item, que é adicionado na mochila;
  - Usar item: removeo item da mochila e aplica o seu efeito, a depender do seu tipo:
    - Tipo `Vida`: recupera 20 vezes `intensidade` o valor da vida atual (até a Vida Máxima);
    - Tipo `Força`: aumenta permanentemente 1 vez `intensidade` o valor do atributo Força;
    - Tipo `Defesa`: aumenta permanentemente 1 vez `intensidade` o valor do atributo Defesa;
  - Ver mochila: exibe na tela a lista de itens disponíveis;
  - Esta vivo: retorna um booleano informando se o aventureiro está vivo.

Além disso, o aventureiro pode carregar itens, que também são uma classe com os seguintes atributos:

- Atributos:
  - Nome: nome do item;
  - Tipo: classificação do item;
  - Intensidade: bônus sobre o atributo (a depender do tipo);

O jogo também deve ter uma classe `Monstro`, que possui os seguintes atributos e métodos:

- Atributos:
  - Força: um inteiro aleatório entre 5 e 25
  - Defesa: um inteiro aleatório entre 5 e 10
  - Vida: um inteiro aleatório entre 10 e 100
- Métodos:
  - Atacar: retorna um inteiro igual à força;
  - Defender: recebe como parâmetro um valor de dano, e reduz desse valor a defesa do monstro. O valor final é reduzido da vida atual do monstro;
  - Esta vivo: retorna um booleano informando se o mosntro está vivo.

Por fim, é necessário uma classe `Tesouro`, que tem um único atributo `posicao`, que corresponde a uma lista com dois inteiros.

### Mecânica

O jogo se passa em um mapa de dimensão 10 x 10. O aventureiro sempre começa na posição `[0, 0]`, e o tesouro em uma posição aleatória no mapa (exceto a posição `[0, 0]`). O aventureiro é representado pelo caractere `@`, e o tesouro pelo caractere `X`.

Em cada rodada, o aventureiro pode fazer uma de quatro ações:

- Mover-se: utilizando as teclas `W`, `A`, `S` e `D`, o aventureiro se move pelo mapa (ver efeito disso a seguir);
- Usar um item: utilizando a tecla `I`, o jogo deve exibir a lista de itens, e o aventureiro pode escolher um para ser usado. Caso um item seja selecionado para usar, realiza a ação dele e remove o item da mochila;
- Ver atributos: verifica força, defesa e vida do aventureiro;
- Sair do jogo: utilizando a tecla `Q`, o jogador foge e o jogo encerra.

#### Movimentando

Ao movimentar o aventureiro, o jogo deve recalcular a sua coordenada baseado na direção que ele se moveu. O aventureiro não pode se mover para as extremidades do mapa (sua posição não pode ser inferior a 0 e nem superior a 9).

Caso o aventureiro realmente se mova, um de três efeitos podem ocorrer:

- Nada (40%): simplesmente nada acontece, e o aventureiro anda para a nova posição;
- Item! (20%): um dos seguintes itens aparece para o aventureiro, e ele é adicionado à mochila;
  - Poção de força, intensidade 1 (10% de chance)
  - Poção de força, intensidade 2 (5% de chance)
  - Poção de vida, intensidade 1 (50% de chance)
  - Poção de vida, intensidade 2 (30% de chance)
  - Poção de defesa, intensidade 1 (5% de chance)
- Monstro! (40%): um novo monstro surge para lutar contra o aventureiro! Veja a seção abaixo.

No final do efeito selecionado, se o aventureiro estiver vivo, o mapa é redesenhado com o aventureiro na nova posição.

#### Combate

O combate se dá nas seguintes ações:

- Fase do aventureiro: ataca, armazenando o dano;
- Fase do monstro: defende, atualizando a vida dele;
- Fase do monstro: ataca, armazenando o dano;
- Fase do aventureiro: defende, atualizando a vida dele.

O combate encerra assim que um dos dois, aventureiro ou monstro, chega a uma vida menor que zero.

#### Encerramento

O jogo acaba quando (a) o aventureiro morre, ou (b) o aventureiro chega no tesouro.

## Avaliação

Os projetos serão avaliados de acordo com os seguintes critérios:

* Qualidade do código (30%): código de acordo com os padrões de escrita, algoritmos bem estruturados e arquitetura bem organizada;
* Testes realizados pelo professor não apresentam falhas (60%);
* Seja criativo! Traga uma mecânica nova para o jogo (10%).

## Informações gerais:

* Prazo: entrega até 23/11/2023 (impreterivelmente);
* Grupos de no mínimo 2 e no máximo 4 pessoas;
* Método de entrega: via Sala de Aula Virtual (estudante.ibmec.br). Formato de entrega:
  * Criar um repositório no GitHub exclusivo para a AP2, torná-lo privado e adicionar o professor (@victor0machado) como colaborador. Subir no estudante o link para o repositório;
