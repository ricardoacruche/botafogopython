"""Tendo como dados de entrada a altura e o sexo de uma pessoa
(M de masculino e F de feminino), construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes formulas"""

#Para homens (72.7*h) - 58
#Para mulheres (62.1*h) - 44.7

altura = float (input("Digite sua altura:"))
sexo = input ("Digite seu sexo (M/F):")

if (sexo == "M"):
    peso = (72.7*altura) -58 #formula definida para calcular peso
else:
    peso = (62.1*altura) -44.7

print ("Seu peso ideal é", peso)

