#Exercício para compreender o datetime.
#Um Clube de piscinas tem a classificação dos seus alunos de acordo com a idade.
#Peça o ano de nascimento do usuário e determine a classificação da seguinte maneira:
#Se a idade for menor que 9 anos, o usuário é mirim;
#Se a idade for maior que 9 anos e menor que 14 anos, o usuário é iniciante;
#Se a idade for maior que 14 anos e menor que 19 anos, o usuário é amador;
#Se a idade for maior que 19 anos e  menor que 21 anos, o usuário é senior;
#Se a idade for maior que 21 anos, o usuário é master;

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
elif idade>19 and idade<=21:
    print('senior')
else:
    print('Master')
