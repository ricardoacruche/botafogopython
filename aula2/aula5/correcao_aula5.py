"""Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
resultado da operação solicitada.
"""

num1 = int (input("Digite o primeiro numero para calcular:"))
num2 = int (input("Agora digite o segundo numero:"))

operacao = input ("Deseja calcular soma (+), subtração (-), multiplicação (*) e divisão (/):")


if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2        

else: 
    print ("operacao invalida")       

print ("Resultado: ", resultado)    