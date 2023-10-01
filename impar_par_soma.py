#Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja ímpar. 
# Mostre na tela o resultado da operação.

x= int(input())

if x %2 == 0:
    par= x + 5
    print(par)
elif x %2 != 0:
    impar= x + 8
    print(impar)

    
