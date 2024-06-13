from datetime import date
hoje= date.today().year
nasc= int(input('Digite o ano do seu nascimento no formato inteiro. (Exemplo: 1998) \nNascido em: '))
idade= hoje-nasc

if idade==18:
    print('Está na hora de se alistar.\nProcure o serviço militar de sua região.')

elif idade>18:
    print('Seu período de alistamento passou em {} anos.' .format(idade-18))
    print('Caso não tenha se alistado ainda, procure estar em dia com o serviço militar o mais breve possível.')
elif idade<18:
    if idade==17:
        print('Caso você complete 18 anos esse ano, você precisará procurar o serviço militar para o alistamento.')
    else:
        print('Você ainda não completou a idade necessária para o alistamento militar.')
        print('Faltam {} anos para seu alistamento militar.' .format(18-idade))