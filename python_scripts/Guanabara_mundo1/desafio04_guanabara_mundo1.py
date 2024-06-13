#Faça um programa que avalie o texto que o usuário digitar com a função .is

text = input('Entre com um texto: ')
print('Tipo do texto: {}' .format(type(text)))
print('Só tem espaços? {}' .format(text.isspace()))
print('É do tipo numérico? {}' .format(text.isnumeric()))
print('é do tipo alfabético? {}' .format(text.isalpha()))
print('é do tipo alfanumérico? {}' .format(text.isalnum()))
print('Está tudo em maiúculo? {}' .format(text.isupper()))
print('Está tudo em minúsculo? {}' .format(text.islower()))
print('Está capitalizado? {}' .format(text.istitle()))
