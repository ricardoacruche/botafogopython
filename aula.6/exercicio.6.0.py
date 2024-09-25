"""Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até
que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados,
assim como a soma e a média aritmética
"""
import math

soma = 0 ; quantidade = 0

while True:
    numero = int (input("Digite um numero:"))
    #O programa deve ler os números até que o usuário digite 0 (zero)
    if numero == 0:
     break

    quantidade = quantidade +1
    soma = soma + numero

print ("A soma e:", soma)
print ("Total de numeros digitados:", quantidade)
print ("Media aritmetica:", math.ceil (soma/quantidade) )
    