#Crie um programa que leia uma frase e diga se é palíndroma

frase = str(input("Digite a frase para saber se é palíndroma: ")).lower().strip()
lista = list(frase)

lista_end=[]
for i in range(len(lista)-1,-1,-1):
                 if lista[i]==" ":
                         lista.pop(i)
                 else:
                        lista_end.append(lista[i])  

if 
print("".join(lista))
print("".join(lista_end))
