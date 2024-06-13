#Faça um programa que receba as dimensões de uma parede e calcule a área que será pintada.
#O programa deve determinar a quantidade de tinta necessária para pintar essa parede. Considere que 2L de tinta pintam 1m²

comp = float(input('Digite o comprimento da parede: '))
larg = float(input('Digite a largura da parede: '))
print('Considerando a parede com comprimento de {}m e largura {}m, a área da parede que será pinta é de {}m².'.format(comp, larg, comp*larg))
print('Assim, a quantidade de tinta necessária para pintar essa parede será de {}L.' .format((comp*larg)/2))
