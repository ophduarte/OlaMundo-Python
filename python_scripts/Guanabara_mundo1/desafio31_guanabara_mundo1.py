#Crie um progrtama que pergunte a distância de uma viagem.
#Será cobrado R$0.5 por km para viagens até 200km
#Será cobrado R$0.45 por km para viaganes mais longas.

km = float(str(input('Entre com a distância de sua viagem: ')).strip())

if km<=200:
    print('O valor da passagem será de R${:.2f}.' .format(km*0.5))
    
else:
    print('O valor da passagem será de R${:.2f}.' .format(km*0.45)) 
