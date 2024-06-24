#Faça um programa que jogue par ou ímpar com o computador.
#O jogo deve ser interrompido se o usuário perder.
#Mostrar quantas vitórias consecutivas ele atingiu.
import random

usr=""
stop=0
counter=0

print("Bem vindo ao jogo de Par ou ímpar!")

while True: 
    
    while usr!="P" and usr!="I":
        usr=str(input("Faça sua escolha:\n[P] PAR \n[I] ímpar \nEscolher: ")).upper()
        
        if usr!="P" and usr!="I":
            print("Entrada Inválida.")
    
    while usr=="P":
        print("\nVocê escolheu Par. Então eu escolho ÍMPAR.")
        pc=random.randrange(1,5,2)

        while not usr.isdecimal():
            usr=str(input("Digite um número PAR entre 0 e 5:\nEscolha: "))

            if usr.isdecimal():
                usr=int(usr)
                if usr%2==0:
                    if usr>=0 and usr<=5:        
                        if usr>pc:
                            print("Ganhou")
                            counter+=1
                            break
                        else:
                            print("Perdeu.")
                            stop=1
                            break
                    else:
                        print("Número fora do intervalo de 0 a 5.")
                        usr="P"                    
                else:
                    print("Número não é PAR")
                    usr="P"         
            else:
                print("Não é um número inteiro.")
                usr="P"

    while usr=="I":
        print("\nVocê escolheu ÍMPAR. Então eu escolho PAR.")
        pc=random.randrange(0,5,2)

        while not usr.isdecimal():
            usr=str(input("Digite um número ÍMPAR entre 0 e 5:\nEscolha: "))

            if usr.isdecimal():
                usr=int(usr)
                if usr%2==1:
                    if usr>=0 and usr<=5:        
                        if usr>pc:
                            print("Ganhou")
                            counter+=1
                            break
                        else:
                            print("Perdeu.")
                            stop=1
                            break
                    else:
                        print("Número fora do intervalo de 0 a 5.")
                        usr="I"                    
                else:
                    print("Número não é ÍMPAR")
                    usr="I"         
            else:
                print("Não é um número inteiro.")
                usr="I"

    if stop==1:
        print(f"Você ganhou {counter} partidas em sequência. Parabéns")
        break
        
        
            
            



            
            
        
    
