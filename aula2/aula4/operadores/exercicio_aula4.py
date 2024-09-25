"""Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
"""

salario = float(input("Digite o valor do salário fo funcionario "))

#Para os inferiores ou iguais, de 15%
if salario <= 1250:
    salario = salario + (salario * 15)/100
    #salario = salario * 1.15
    print (f'O valor do novo salario e R$: {salario}')

#calcule um aumento de 10%
else:
    salario = salario + (salario * 10)/100
    #salario = salario * 1.1
    print (f'O valor do novo salario e R$: {salario}')  