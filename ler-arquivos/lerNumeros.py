import os

arquivo = "numeros.txt"

soma = 0

if os.path.exists(arquivo):
    with open("numeros.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            print(linha)
            soma += int(linha)
else:
    print(f"Não existe o arquivo {arquivo}")

print(f"A soma das linhas dá {soma}")
