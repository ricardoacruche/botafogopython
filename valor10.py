
numeros = []

soma = 0 #variavel acumulador 
cont = 0 #variavel contadora +1
media = 500 #calcular a media

for i in range (500):
    numeros = int (input("Digite um numero:"))
    soma += numeros
    media = soma / 500
    if numeros [i] > media:
        print ("")
    if numeros [i] < media:
        print ("")   

        media = media <- soma/500