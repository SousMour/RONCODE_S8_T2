#Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas obtidas nos exercícios que fazem parte da sua avaliação. 
# Calcule a média final usando a fórmula:
#Média Final = (Nota 1 + Nota 2 * 2 + Nota 3 * 3 + Média Exercícios) / 7
#A atribuição dos conceitos obedece a tabela abaixo.
#Conceito |Média Final
#A | >= 9.0
#B | >= 7.5 e < 9.0
#C | >= 6.0 e < 7.5
#D | >= 4.0 e < 6.0
#E | < 4.0
#O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado” se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.

def media_final(nota_1, nota_2, nota_3, media_exercicio,matricula):
    media_final = (nota_1 + (nota_2 * 2) + (nota_3 * 3) + media_exercicio) / 7
    if media_final >= 9.0:
        conceito = 'A'
    elif media_final >= 7.5 and media_final < 9.0:
        conceito = 'B'
    elif media_final >= 6.0 and media_final < 7.5:
        conceito = 'C'
    elif media_final >= 4.0 and media_final < 6.0:
        conceito = 'D'
    else:
        conceito = 'E'
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        print(f'{matricula}')
        print(f'{media_final:.2f}')
        print(f'{conceito}')
        print('Aprovado')
    elif conceito == 'D' or conceito == 'E':
        print(f'{matricula}')
        print(f'{media_final:.2f}')
        print(f'{conceito}')
        print('Reprovado')

matricula=input()
nota_1= float(input())
nota_2= float(input())
nota_3= float(input())
media_exercicio= float(input())
nota_final=media_final(nota_1, nota_2, nota_3,media_exercicio,matricula)


