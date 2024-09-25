"""Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para
indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
"""

quantidade_de_kwh = int (input("Digite a quantidade de kWh consumida:"))
tipo_de_instalacao = input ("Digite o tipo de instalação \n R - residências \n C - comércios \n I - industria").upper()


if tipo_de_instalacao == "R":
    if quantidade_de_kwh <= 500:
      precoapagar = 0.40
    else:
     precoapagar = 0.65

elif tipo_de_instalacao == "C":
    if quantidade_de_kwh <= 1000:
      precoapagar = 0.55
    else: 
     precoapagar = 0.60 

elif tipo_de_instalacao == "I":
    if quantidade_de_kwh <= 5000:
      precoapagar = 0.70
    else:
      precoapagar = 0.80

else:
  precoapagar = 0
print ("Erro! Tipo de instalacao desconhecido")

custo = quantidade_de_kwh * precoapagar

print (f"O valor a pagar R$ {custo} ")