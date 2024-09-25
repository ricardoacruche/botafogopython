
velocidade = float (input("Digite a velocidade do carro"))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print (f"voce foi multado! em R$: {multa}")
if velocidade <= 80:
    print ("sua velocidade esta ok, boa viagem!")    