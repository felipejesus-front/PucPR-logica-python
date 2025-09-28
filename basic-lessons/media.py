nomeDisciplina = input("Digite o nome da sua disciplina: ")
disciplina1 = float(input(f"Digite sua 1º nota na disciplina {nomeDisciplina}: "))
disciplina2 = float(input(f"Digite sua 2º nota na disciplina {nomeDisciplina}: "))
disciplina3 = float(input(f"Digite sua 3º nota na disciplina {nomeDisciplina}: "))
disciplina4 = float(input(f"Digite sua 4º nota na disciplina {nomeDisciplina}: "))
mediaDisciplinas = (disciplina1 + disciplina2 + disciplina3 + disciplina4) / 4

print(f"A média das suas notas na disciplina {nomeDisciplina} é: {mediaDisciplinas}")
