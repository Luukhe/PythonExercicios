from time import sleep
from random import choice

print ('JO')
sleep(0.5)
print ('KEN...')
sleep(0.5)
print('PO!')
sleep(0.5)
print ('É hora do Jokenpo! Escolha entre pedra, papel e tesoura. VAMOS LÁ!')
escolha = (input('Digite sua escolha: ')).strip().upper()
pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'
lista = [pedra,papel,tesoura]
pc = choice(lista)

if pc==pedra and escolha==tesoura:
    print (f'Eu escolhi {pedra} e você {escolha}. EU GANHEI!')
elif pc==pedra and escolha==papel:
    print (f'Eu escolhi {pedra} e você {escolha}. VOCÊ GANHOU...')
elif pc==papel and escolha==pedra:
    print (f'Eu escolhi {papel} e você {escolha}. EU GANHEI!')
elif pc==papel and escolha==tesoura:
    print (f'Eu escolhi {papel} e você {escolha}. VOCÊ GANHOU...')
elif pc==tesoura and escolha==papel:
    print (f'Eu escolhi {tesoura} e você {escolha}. EU GANHEI!')
elif pc==tesoura and escolha==pedra:
    print (f'Eu escolhi {tesoura} e você {escolha}. VOCÊ GANHOU...')
else:
    print (f'Eu escolhi {escolha} e você {escolha}. EMPATAMOS!')