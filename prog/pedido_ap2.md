# Pedido da AP2

Para a AP2, cada time deve implementar o projeto indicado abaixo.

## Jogo da Memória

### Pedido

Desenvolva um jogo da memória utilizando o pacote `pygame`. O jogo deve conter os seguintes requisitos mínimos:

- 20 cartas, contendo 10 pares numerados de 0 a 9. Todas as cartas devem começar o jogo viradas para baixo, como na imagem abaixo:

    ![Tela inicial do jogo da memória](/prog/img/memoria1.png)

- Ao clicar em uma carta, o jogo deve "virá-la" e exibir o número naquela posição:

    ![Uma carta virada](/prog/img/memoria2.png)

- Quando uma segunda carta for virada, o jogo deve tomar uma decisão:
    - Se as duas cartas viradas formarem um par, o jogo deve mantê-las viradas;
    - Se as cartas não formarem um par, o jogo deve esconder seus valores novamente.
- O jogo continua rodando até todos os pares forem descobertos.

### Dicas

- Utilize o [modelo de código](/prog/projetos/modelo_ap2.txt) passado para o trabalho. Substitua as instruções `pass` pelos códigos necessários para executar as instruções de forma que o jogo seja executado corretamente.
- Utilize a função de desenhar um retângulo para desenhar as cartas viradas para baixo;
- Verifique se o mouse foi liberado através do evento de tipo `pygame.MOUSEBUTTONUP`;
- Obtenha as coordenadas da posição do mouse com a função `pygame.mouse.get_pos()`, que retorna um par `(pos_x, pos_y)`;
- Utilize a documentação de cada função ou método para montar a lógica.

### Avaliação

O projeto será avaliado de acordo com os seguintes critérios:

- (1,0 pontos) Qualidade de escrita de código: variáveis foram bem nomeadas, código está de acordo com os padrões discutidos em sala (será rodado o pylint para avaliar a qualidade do código);
- (2,0 pontos) Qualidade dos algoritmos: o código não apresenta redundâncias ou trechos não solicitados. O algoritmo está completo e atende a todos os pedidos nos requisitos do projeto;
- Testes realizados pelo professor não apresentam falhas (ver abaixo).

Os seguintes eventos serão pontuados caso ocorram sem falhas:

- (1,0 ponto) Carta vira após um clique;
- (1,0 ponto) Nada acontece se clicar fora de uma carta;
- (1,0 ponto) Clicar em duas cartas que não possuem o mesmo valor faz com que elas sejam ocultadas após 1s;
- (1,0 ponto) Clicar em duas cartas que possuem o mesmo valor não as oculta novamente;
- (1,0 ponto) Clicar em duas cartas que não possuem o mesmo valor e com alguns pares já revelados faz com que apenas as duas últimas cartas sejam viradas;
- (1,0 ponto) Ao virar cada carta, o seu valor está centralizado;
- (0,5 ponto) A tela do jogo apresenta uma borda, conforme já exibido;
- (0,5 ponto) As cartas são distribuídas uniformemente pela tela.

## Informações gerais:

* Prazo: 21/11/2022
* Grupos de no mínimo 3 e no máximo 4 pessoas
* Subir na Sala de Aula Virtual o código salvo no formato .txt
* Incluir o nome de todos os participantes como docstring no início do código
