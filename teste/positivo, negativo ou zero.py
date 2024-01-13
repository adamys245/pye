#Desafio em Python: Crie um programa que solicite ao usuário um número e, em seguida, 
#determine se o número é positivo, negativo ou zero, usando apenas estruturas if e else.

n1= int(input("Insira um número: "))
#sistema de decisão

if n1==0:
    print("neutro")
elif n1>=1:
    print ("Positivo")
else:
    print("Negativo")
