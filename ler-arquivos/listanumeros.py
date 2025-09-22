lista_numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)


with open("numeros.txt", "w") as arquivo:
    for numero in lista_numeros:
        arquivo.write(str(numero) + "\n")
