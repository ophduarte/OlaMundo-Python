comp = float(input('Digite o comprimeto da parede: '))
larg = float(input('Digite a largura da parede: '))
print('Considerando a parede com comprimento de {}m e largura {}m, a área da parede que será pinta é de {}m².'.format(comp, larg, comp*larg))
print('Assim, a quantidade de tinta necessária para pintar essa parede será de {}L.' .format((comp*larg)/2))