from time import sleep
valor = float (input('Digite o valor do produto: R$'))
print ('Agora, escolha uma das formas de pagamento abaixo: ')
print ('1. À vista, dinheiro ou cheque: 10% de desconto')
print ('2. À vista, no cartão: 5% de desconto')
print ('3. Em até 2x no cartão: preço normal')
print ('4. Em 3x ou mais no cartão: 20% de juros')
pagamento = int (input('Digite a forma de pagamento: '))
print ('Processando sua compra...')
sleep(2)

if pagamento==1:
    print (f'Você escolheu a opção 1. Total a ser pago: R${valor*90/100:.2f}')
elif pagamento==2:
    print (f'Você escolheu a opção 2. Total a ser pago: R${valor*95/100:.2f}')
elif pagamento==3:
    print (f'Você escolheu a opção 3. Total a ser pago: R${valor:.2f}')
elif pagamento==4:
    print (f'Você escolheu a opção 4. Total a ser pago: R${valor*120/100:.2f}')

print ('Tenha um bom dia!')