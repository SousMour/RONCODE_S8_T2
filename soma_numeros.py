#Escreva um programa que leia um número inteiro. 
# Mostre a soma dos dígitos para os números entre 0 (zero) e 100 mil ou -1 para outros valores. 
# Por exemplo: Em 16.759 a soma dos dígitos é 1 + 6 + 7 + 5 + 9 = 31 é o valor retornado; 
# Em 136.759 o valor lido é maior que 100 mil e deve retornar -1; Em -100 o valor lido é negativo e deve retornar -1.

def getSum(n):  
     
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum
    
n= input()
if 0 <= int(n) and int(n) < 100000:
    print(getSum(n))
else:
    print(-1)