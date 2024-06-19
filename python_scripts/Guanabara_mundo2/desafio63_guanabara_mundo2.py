#Crie um programa que leia um número N.
#Mostre na tela o termo da N posição da sequência de Fibonacci.

pos=int(input("Digite a posição final que queira ver o termo da sequencia de Fibonacci: "))
fib=[1,1,]
i=2

if pos>2:
        while i<pos:
                fib.append(0)
                fib[i] = fib[i-2] + fib[i-1]
                i+=1

print(fib)
