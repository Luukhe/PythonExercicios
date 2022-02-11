r1 = float (input('Valor da primeira reta: '))
r2 = float (input('Valor da segunda reta: '))
r3 = float (input('Valor da terceira reta: '))
if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    print ('O triangulo PODE ser formado.')
else:
    print ('O triangulo NÃO pode ser formado.')
if r1==r2==r3:
    print ('O triangulo será EQUILÁTERO.')
if r1==r2!=r3 or r2==r3!=r1 or r1==r3!=r2:
    print ('O triangulo será ISOSCELES.')
if r1!=r2!=r3 and r2!=r3!=r1 and r1!=r3!=r2 and r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    print ('O triangulo será ESCALENO.')
