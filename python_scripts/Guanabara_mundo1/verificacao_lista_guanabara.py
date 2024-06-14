frase = 'Pedro Henrique Duarte'
print(len(frase)) #mostra a quantidade de caracteres
print(frase.count('e')) #conta quantos caracteres que são iguais a 'e'

print(frase[0]) #mostra o primeiro caracter do "vetor" <frase>
print(frase[1]) #mostra o segundo caracter do "vetor" <frase>
print(frase[2]) #mostra o terceiro caracter do "vetor" <frase>
print(frase[3]) #mostra o quarto caracter do "vetor" <frase>
print(frase[4]) #mostra o quinto caracter do "vetor" <frase>

print(frase[0:5]) #mostra do primeiro caracter até o quinto caracter, o caracter <4> e não o <5>
print(frase[:5])  #faz a mesma coisa, mas sem especificar o começo. Assim, será iniciado no caracter <0>

print(frase[15:21]) #mostra do 16º caracter até o 21º caracter, o caracter <20> e não o <21>
print(frase[15:]) #faz a mesma cois, mas sem especificar o final. Assim, irá terminar no final

print(frase[::2]) #mostra a <frase de começo a final, pulando de 2 em 2 letras. A segunda letra é incluida

print(frase.replace('Pedro', 'Arllen')) #subtitui a palavra Pedro por Arllen, sem mudar a string inicial, ainda continuará com o 'Pedro'
print(frase.find('e')) #Se a palavra existir em <frase> ele retornará o valor de onde começa a primeira letra. Caso a palavra não exista, retornará o valor '-1'.
lista = frase.split() #divide a <frase> em uma lista de palavras, que foram separadas onde tinha espaços
print(lista[0]) #mostra a primeira palavra criada em lista
