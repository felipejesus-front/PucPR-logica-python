import os

nomeArquivo = "alunos.txt"

if os.path.exists(nomeArquivo):
    with open(nomeArquivo, "r") as arquivo:
        notas = []
        for linha in arquivo:
            dados = linha.split(",")
            notas.append(float(dados[2]))

media = sum(notas) / len(notas)
print("A média das notas dos alunos é:", media)
