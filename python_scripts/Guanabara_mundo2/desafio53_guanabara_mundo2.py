#Crie um programa que leia uma frase e diga se é palíndroma
#Palíndroma é a frase que quando escrita de trás para frente fica igual ao normal

frase = str(input("Digite a frase para saber se é palíndroma: ")).lower().strip()
lista = list(frase)

lista_end=[]
for i in range(len(lista)-1,-1,-1):
                 if lista[i]==" ":
                         lista.pop(i)
                 else:
                        lista_end.append(lista[i])  

if "".join(lista)=="".join(lista_end):
        print("A frase inserida é palíndroma")

else:
        
        print("A frase não é palíndroma")