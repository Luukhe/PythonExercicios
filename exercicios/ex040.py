n1 = float (input('Primeira nota: '))
n2 = float (input('Segunda nota: '))
media = (n1+n2)/2
if media>=7:
    print (f'Sua média foi de {media}. Você está \033[32mAPROVADO!\033[m')
elif media>5 and media<6.9:
    print (f'Sua média foi de {media}. Você está de \033[33mRECUPERAÇÃO!\033[m')
elif media<=5:
    print (f'Sua média foi de {media}. Você está \033[31mREPROVADO!\033[m')
