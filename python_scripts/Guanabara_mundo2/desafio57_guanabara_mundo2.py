#Crie um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo=str("0")
print("Digite o seu sexo:")
print("(M) - Masculino")
print("(F) - Feminino")
print("(O) - Outros")

while (sexo!="M" and sexo!="F" and sexo!="O"):
        sexo=str(input("Qual seu sexo?\n")).upper()
        if sexo!="M" and sexo!="F" and sexo !="O":
                print("Entrada inválida.")
        
print(f"Sexo inserido {sexo}")
