#Faça um programa que verifica se o ano é bissexto

ano = int(str(input('Entre com o ano: ')).strip())

if ano%4==0:
    print('O ano é bissexto.')
    
else:
    print('O ano não é bissexto') 