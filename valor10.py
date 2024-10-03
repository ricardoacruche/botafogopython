"""Construir um sistema automatizado para calcular as notas finais, em todas as disciplinas, de todos
os alunos de uma escola.
Elabore um fluxograma que leia dois números (x e y) e escreva como resultado o maior entre eles.
Elabore um fluxograma que permita a entrada de dois valores, x e y, troque seus valores entre si e
então exiba os novos resultados
Elabore um fluxograma que calcule e exiba a média de 500 números fornecidos pelo usuário.
Elabore um fluxograma que calcule quantas notas de 50, 10 e 1 são necessárias para se pagar uma
conta cujo valor é fornecido."""

#criar um dicionario para armazenar as notas dos alunos
alunos = {}
#definir a quantidade de alunos e disciplinas
num_alunos = int(input("Digite o numero de alunos:"))
disciplinas = ["Ingles", "Filosofia", "Ocultismo"] #exemplos de disciplinas

#Loop para coletar os nomes e notas dos alunos
for i in range(500):
    nome = input(f"Digite o nome do aluno {i+1}:")
    alunos [nome] = {}

    for disciplinas in disciplinas:
        nota = float (input(f"Digite a nota de {nome} em {disciplinas}:"))
        alunos [nome][disciplinas] = nota
#calcular e exibir a media dos alunos
for aluno, notas in alunos.items():
    media = sum(notas.values() ) / len(notas)

print (f"A media de {aluno} é {media:.2f}")       


