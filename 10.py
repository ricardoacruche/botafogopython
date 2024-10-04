"""Elabore um fluxograma que calcule quantas notas de 50, 10 e 1 são necessárias para se pagar uma
conta cujo valor é fornecido."""

#for é usado para por limites, quando voce sabe quando acaba.
while True:
    valor = int (input("Qual valor para saque:"))

    n50 = valor // 50
    r50 = valor % 50 #r de resto da divisao
    n10 = r50 // 10
    n1 = r50 % 10

    #Tambem pode fazer assi, eliminando mais uma linha
    #n50 = valor // 50
    #n10 = (valor % 50) // 10
    #n1 = (valor % 50) % 10

    print ("Notas de 50 é", n50)
    print ("Notas de 10 é", n10)
    print ("Moedas de 1", n1)

    resposta = input ("Deseja fazer outro saque (S/N)?")

    if resposta == "N":
        break