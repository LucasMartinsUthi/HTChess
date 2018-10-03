Olá, instruções para iniciar o jogo:

As configurações atuais estão para criar um servidor local e jogar o jogo em dois terminais diferentes no mesmo computador, caso queira testar o jogo entre dosi computadores entras no arquivo server.py e mudar a na linha 6 o 'localhost', para o ip do host, a mesa alteração deve ser feita em classe/classJogador.py na linha 79.

Para iniciar será necessário o uso de 3 terminais, 1 servidor e 2 clientes. Primeiro inicialiçe o server.py, após isso execute os main.py em ambos clientes, um sendo o jogador número 1 e o outro o jogador número 2. Feito isso só jogar.

Regras:
No primeiro momento os jogadores recebem uma mão inicial, o jogador número 1 começa com 4 cartas, e o jogador número 2 com 3 cartas mais uma moeda(ganha 1 de mana nesse turno). Essa primeira mão é possível descartar quantas cartas desejadas, que elas serão substituídas por outras no deck, as descartadas voltam para o deck.

Para colocar uma carta da  sua mão à mesa, é necessário que o jogador tenha a quantidade certa de mana para jogar a carta, cada jogador começa com 1 de mana máxima, que vai aumentado por turno. Ao olhar a carta é possível perceber 3 valores, que são attack, vida, custo de mana. Attack: indica a quantidade de dano que uma carta causa. Vida: indica quanto dano uma carta pode receber antes de ser eliminado do tabuleiro. Custo de Mana: quantidade de mana necessário para colocá-la no tabuleiro.

Ao terminar o turno as cartas do tabuleiro atacam. Elas seguem as seguintes regras, cartas atacam inimigas opostas, ou seja, uma carta ataca a carta a sua frente, porém é possível que uma carta ataque duas cartas ao mesmo tempo. Caso não houver nenhuma carta inimiga para defender seu ataque, a carta ataca o adversário. Quando a vida de um jogador chega 0 ou menor o jogo acaba.

Av ida do jogador pode ser vista ao lado das cartas na mão, onde informa a vida, mana atual, mana total, cartas no deck. Quando acaba as cartas do deck o jogador começa a receber dano de fadiga, que aumenta 1 de dano a cada turno que passa.
