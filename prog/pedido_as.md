# Pedido da AS

Você deve implementar uma solução que simule uma fila de um estabelecimento de serviços (p.ex., um banco). Para implementar essa solução, resolva os seguintes exercícios em um único arquivo. Nos exercícios 2 a 4, caso `fila` seja uma lista vazia, a função deve imprimir na tela "Fila vazia!".

1. Implemente uma função `chegada_cliente()`, que retorna None e que recebe dois parâmetros:
   - `fila`: lista contendo os clientes que estão aguardando;
   - `cliente`: lista com dois campos:
       - Primeiro campo: conta do cliente;
       - Segundo campo: nome do cliente.

    A função deve inserir `cliente` na primeira posição de `fila`. Após isso, ela deve imprimir na tela a seguinte mensagem (sem aspas), onde "nome" é o nome do cliente, e "n" é o número de clientes na frente de `cliente`:

    "Olá, nome! Aguarde sua vez, existem n clientes na sua frente."

2. Implemente uma função `chamada_cliente()`, que recebe `fila` como parâmetro. A função deve imprimir na tela a seguinte mensagem (sem aspas), onde "nome" é nome do cliente:

    "Chegou a sua vez, nome!"

    O cliente em questão é o último elemento de `fila`. A função deve remover esse elemento da `fila` e deve retorná-lo.

3. Implemente uma função `lista_clientes()`, que recebe `fila` como parâmetro. A função deve imprimir, na tela, a posição na fila, a conta e o nome de cada cliente cadastrado em `fila`, na ordem de chamada. Isto é, a função deve exibir primeiro o último elemento, em seguida o penúltimo, o antepenúltimo, etc., até chegar no primeiro. A função retorna `None`.
4. Implemente uma função `premia_cliente()`, que recebe `fila` como parâmetro. A função deve selecionar, dentre os clientes cadastrados em `fila`, apenas um, aleatoriamente, para receber um prêmio. A função deve retornar esse cliente, e imprimir na tela a seguinte mensagem (sem aspas), em que "nome" é o nome do cliente:

    "Parabéns, nome! Você foi premiado!"

5. (questão bônus) Implemente uma função `main()`, que executa as seguintes ações:
   - Inicializa `fila`, uma lista vazia;
   - Em um loop:
       - Recebe um input de texto do usuário;
       - Age conforme o input do usuário:
           - Caso seja "1", pede o nome e a conta do cliente e chama a função `chegada_cliente()`;
           - Caso seja "2", chama a função `chamada_cliente()`;
           - Caso seja "3", chama a função `lista_clientes()`;
           - Caso seja "4", chama a função `premia_cliente()`;
           - Caso não seja nenhuma das opções anteriores, dispara a mensagem "Opção inválida!"

Faça uma chamada para essa função `main()`. Finalizando, salve o arquivo como .txt e envie pela sala de aula virtual.