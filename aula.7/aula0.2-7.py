resposta = int(input("Quantos alunos voce quer calcular?"))

i = 0
alunos = []

while i < resposta: #OUTRA MANEIRA DE CRIAR: for i in range (resposta): 
    nome_aluno = input("Digite seu nome:")
    nota1 = float (input ("Digite sua a primeira nota:"))
    nota2 = float (input ("Digite sua a segunda nota:"))
    nota_media = (nota1 + nota2)/2 #usando /2 para calcular a media 
    resultado = "Aprovado" if nota_media >= 6.5 else "Reprovado"

    if (nota_media >= 6.5):
        print (f"A nota foi {nota_media} do {nome_aluno} e foi aprovado")
    else:
        print (f"A nota foi {nota_media} do {nome_aluno} e foi reprovado")
    
    i = i + 1

    for i in range (2):
        nome = input("Digite o nome:")
        nota1 = int (input("nota 1:"))
        nota2 = int (input("nota 2:"))
        nota_media = (nota1 + nota2)/2
        

    alunos.append = (
            { "nome": nome,
                "nota1": nota1,
                "nota2": nota2,
                "media": nota_media,
                "resultado": resultado
            })


print (resultado)
 