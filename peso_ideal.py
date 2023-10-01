#Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para 'homens' e 2 para 'mulheres'. 
# Usando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:
#para homens: (72.7 * altura) – 58
#para mulheres: (62.1 * altura) – 44.7

def peso(sexo, altura):
    if sexo== 1:
        return (72.7 * altura ) - 58
    elif sexo == 2:
        return (62.1 * altura ) - 44.7
    else:
        return 0
    
altura=float(input())
sexo=int(input())
peso_ideal=peso(sexo, altura)
print(f'{peso_ideal:.2f}')