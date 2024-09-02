from random import randint
from time import sleep
opcao = int(input('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[opcao]}')
if opcao == 0 and computador == 2 or opcao == 1 and computador == 0 or opcao == 2 and computador == 1:
    print('Vitória do Jogador')
elif opcao == computador:
    print('Empate')
else:
    print('Vitória do Computador')
