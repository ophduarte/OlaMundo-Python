#Crie um programa que leia o nome de uma cidade e diga se ela ela começa com o nome "Santo"

city = str(input('Entre com o nome da sua cidade: ')).strip()
city = city.upper()
print(city[:5] == 'SANTO')
