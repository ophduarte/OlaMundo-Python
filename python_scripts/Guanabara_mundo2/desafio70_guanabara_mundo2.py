#Crie um programa que leia o nome e o preço de vários produtos.
#A cada produto cadastrado, o programa deverá perguntar se o usuário quer ou não acrescentar mais produtos.
#No final mostre: quantos produtos foram cadastrados, quantos produtos custam mais do que R$1000 e qual é o produto com o menor preço.

mais_mil=0
produtos_nome=[]
produtos_preco=[]
choice=""
i=0

while True:
    
    produtos_nome.append(str(input("Digite o nome do produto: ")).strip())
    produtos_preco.append(float(input("Digite o preço do produto: R$ ")))         
    
    if produtos_preco[i]>1000:
        mais_mil+=1

    while choice!="S" and choice!="N":
        choice=str(input("Deseja adicionar outro produto? [S/N] \nEscolha: ")).upper()

        if choice!="S" and choice!="N":
            print("Entrada errada!")
        
    if choice=="S":
        i+=1
        choice=""

    else:
        break

print(f"\nQuantidade de itens adicionados na lista: {len(produtos_nome)}")
print(f"\nQuantidade de itens adicionados com valor maior do que mil reais: {mais_mil}")
print(f"\nNome do item que tem o menor preço entre os itens adicionados: {produtos_nome[(produtos_preco.index(min(produtos_preco)))]}")
    
        



