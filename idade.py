dataNascimento = input("Digite sua data de nascimento no formato dd/mm/aaaa: ")

anoUsuario = int(dataNascimento[6:])
anoAtual = 2023

print(f"A sua idade, em 2023 é: ", anoAtual - anoUsuario, "anos")
