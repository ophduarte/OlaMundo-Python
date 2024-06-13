import datetime
ano_nasc = int(input('Ano de nascimento:      (Entre com o valor inteiro)\n'))
ano_hoje = (datetime.date.strftime(datetime.date.today(), '%Y'))
idade = int(ano_hoje)-int(ano_nasc)

if idade <= 9:
    print('mirim')
elif idade >9 and idade<=14:
    print('iniciante')
elif idade>14 and idade<=19:
    print('amador')
elif idade>19 and idade<=20:
    print('senior')
else:
    print('Master')