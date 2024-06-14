import random
num = random.randint(0,9999)
print('o número sorteado é {}' .format (num))
uni =  num%10
dez = (num//10)%10
cent = (num//100)%10
mil = num//1000
print('numerico {} {} {} {}' .format(mil, cent, dez, uni))

num = str(num)
lista = list(num.zfill(4))

print('O dígito do milhar: {}' .format(lista[0]))
print('O dígito da centena: {}' .format(lista[1]))
print('O dígito da dezena: {}' .format(lista[2]))
print('O dígito da unidade: {}' .format(lista[3]))