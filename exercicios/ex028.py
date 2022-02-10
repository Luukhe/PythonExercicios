from random import randint
from time import sleep

n1 = int (input('Digite um número: '))
randomizer = randint(0,5)
print ('Processando...')
sleep(2.5)

if randomizer == n1:
    print (f'Você pensou no número {n1}. Parabéns, você \033[32mACERTOU!\033[m')
else:
    print (f'Você pensou no número {n1}. Que pena, você \033[31mERROU...\033[m')
