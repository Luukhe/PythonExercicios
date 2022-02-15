print ('Informe a temperatura em Celsius, Fahrenheit ou Kelvin para converter:')
print ('1. De Fahrenheit para Celsius')
print ('2. De Celsius para Fahrenheit')
print ('3. De Celsius para Kelvin')
print ('4. De Kelvin para Celsius')
print ('5. De Fahrenheit para Kelvin')
print ('6. De Kelvin para Fahrenheit')
escolha = int (input('Digite o formato da temperatura desejada: '))
temp = int (input('Agora, digite a temperatura desejada para a conversão: '))
if escolha==1:
    print (f'A temperatura de {temp}ºF, para Celsius é {(temp-32)/1.8:.1f}°C.') #(temp-32)/1.8
elif escolha==2:
    print (f'A temperatura de {temp}°C, para Fahrenheit é {temp* 1.8 +32:.1f}°F.') #temp* 1.8 +32
elif escolha==3:
    print (f'A temperatura de {temp}°C, para Kelvin é {temp+273.15:.1f}°K.')
elif escolha==4:
    print (f'A temperatura de {temp}°K, para Celsius é {temp-273.15:.1f}°C. ')
elif escolha==5:
    print (f'A temperatura de {temp}°F, para Kelvin é {(temp-32)*5/9+273.15:.1f}°K.')
elif escolha==6:
    print (f'A temperatura de {temp}°K, para Fahrenheit é {(temp-273.15)*1.8+32:.1f}°F.')
