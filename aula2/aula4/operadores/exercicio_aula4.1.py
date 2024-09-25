"""Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,45 para viagens mais longas.

"""

km = float (input ("Digite a distancia percorrida"))

#cobrando R$ 0,50 por km para viagens de até de 200 km
if km <= 200:
    passagem = 0.5 *km
    print (f'O valor a pagar por percorrer {km} e R$ {passagem}') 
      
#R$ 0,45 para viagens mais longas    
else:
    passagem = 0.45 *km
    print (f'O valor a pagar por percorrer {km} e R$ {passagem}')    