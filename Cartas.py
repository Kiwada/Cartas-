from random import choice
Lista = [ 1 ,2 ]
cpu = choice(Lista)
print('-=-' * 20)
print('Vou pensar em um número ente 1 a 2 , tente adivinhar..')
print('-=-' * 20)

#print('Pensei no Número {}'.format(cpu))#

Escolha = int(input('Escolha um Numero de 1 a 2 :'))
if cpu == Escolha:
 print('Você Venceu o Jogo')
else:
 print('Você Perdeu o jogo , eu pensei no {} não no {}'.format(cpu , Escolha))
