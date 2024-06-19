#Crie um joguinho que o computador sortei um número de 0 a 10.
#O usuário precisará ficar tentando acertar o número.

from random import randint

n=randint(0,10)
print(n)
usr=11
while (usr!=n):
        
        usr=int(input("Tente adivinhar o número que eu sorteei: \n"))
        
        if usr!=n:
                print("Erroooou!")
        
print("Parabéns! Você acertou!")
