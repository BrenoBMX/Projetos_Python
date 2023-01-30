from random import randint
itens = 'pedra', 'papel', 'tesoura'
computer = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual é a sua jogada?'))
print('Computador jogou {}'.format(itens[computer]))
print('Jogador jogou {}'.format(itens[jogador]))
if computer == 0:
    if jogador == 0:
        print('EMPATE')
    if jogador == 1:
        print('JOGADOR GANHOU')
    if jogador == 2:
        print('JOGADOR PERDEU')
    else:
        print('Jogada inválida !')

if computer == 1:
    if jogador == 0:
        print('JOGADOR PERDEU')
    if jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('Jogada inválida !')

if computer == 2:
    if jogador == 0:
        print('JOGADOR PERDEU')
    if jogador == 1:
        print('JOGADOR PERDEU')
    if jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida !')
