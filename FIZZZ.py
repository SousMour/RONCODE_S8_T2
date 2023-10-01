#Escreva um programa que leia um número inteiro positivo e escreva na tela:
#FIZZ se o número é divisível por três;
#BUZZ se o número é divisível por cinco;
#FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
#O próprio número caso não seja divisível por três ou por cinco.

def numero(x):
    if x % 3 == 0 and not x % 5 == 0:
        return 'FIZZ'
    elif x % 5 == 0 and not x % 3 == 0:
        return 'BUZZ'
    elif x % 3 == 0 and x % 5 == 0:
        return 'FIZZBUZZ'
    else:
        return x

x= int(input())
x=numero(x)
print(x)