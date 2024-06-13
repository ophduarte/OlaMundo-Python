#Faça um programa que calcule a média das provas de um aluno.
#Se a média for menor que 5, o aluno estará reprovado.
#Se a média estiver entre 5 e 7, o aluno precisará fazer recuperação.
#Se a média é maior que 7, o aluno foi aprovado.

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1+nota2)/2

if media<5:
    print('A média atingida pelo aluno foi de {:.2f}.\nInfelizmente ele foi reprovado.'.format(media))
elif media>=5 and media<=6.9:
    print('A média atingida pelo aluno foi de {:.2f}.\nAluno precisará fazer recuperação.' .format(media))
else:
    print('Aluno aprovado com média {:.2f}.' .format(media))
