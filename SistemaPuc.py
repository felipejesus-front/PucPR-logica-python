import sys

listaMenu = ["Estudantes", "Disciplinas", "Professores", "Turmas", "Matrículas", "Sair"]
listaCrude = ["Incluir", "Listar", "Atualizar", "Excluir", "Voltar ao menu principal"]
mensagemEscolha = "Informe a opção desejada: "
mensagemFinalizando = "Finalizando Aplicação"
Estudantes = []
idEstudante = 0


def sairDoSistema():
    sys.exit()


def printaCRUD():
    for indice, item in enumerate(listaCrude):
        print(f"({indice+1})", item)


def menuOpcoes(lista, mensagem):
    while True:
        for indice, item in enumerate(lista):
            print(f"({indice+1})", item)
        escolha = input(mensagem)
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(lista):
                return indice, lista[indice]
            else:
                print("\nOpção inválida.\n")
        elif escolha in lista:
            return lista.index(escolha), escolha
        else:
            print("\nOpção inválida.\n")


def listarEstudantes():
    if Estudantes:
        for item in Estudantes:
            print(f"===== {item} =====")
    else:
        print("===== Não há estudantes cadastrados =====")


def incluirEstudante():
    global idEstudante
    nome = input("Nome do estudante: ")
    cpf = input("CPF do estudante: ")
    estudante = {"codigo": idEstudante, "nome": nome, "cpf": cpf}
    Estudantes.append(estudante)
    idEstudante += 1
    print("Estudante cadastrado com sucesso!")


def excluirEstudantePorCodigo(codigo):
    for estudante in Estudantes:
        if estudante["codigo"] == codigo:
            Estudantes.remove(estudante)
            print("Estudante excluído com sucesso!")
            return
    print("\n===== Estudante não encontrado. =====\n")


def atualizarEstudantePorCodigo(codigo):
    for estudante in Estudantes:
        if estudante["codigo"] == codigo:
            novoNome = input("Novo nome do estudante: ")
            novoCpf = input("Novo CPF do estudante: ")
            estudante["nome"] = novoNome
            estudante["cpf"] = novoCpf
            print("Estudante atualizado com sucesso!")
            return
    print("\n===== Estudante não encontrado. =====\n")


def navegarMenuOperacoes(nomeMenu):
    while True:
        print(f"\n***** [{nomeMenu}] Menu de operações: *****\n")
        indice, escolhaCrude = menuOpcoes(listaCrude, mensagemEscolha)
        if escolhaCrude == "Voltar ao menu principal":
            break
        else:
            executarOperacao(indice, escolhaMenu)


def executarOperacao(indice, escolhaMenu):
    if indice == 0 and escolhaMenu == listaMenu[0]:
        incluirEstudante()
    elif indice == 1 and escolhaMenu == listaMenu[0]:
        listarEstudantes()
    elif indice == 3 and escolhaMenu == listaMenu[0]:
        codigo = int(input("Informe o código do estudante a excluir: "))
        excluirEstudantePorCodigo(codigo)
    elif indice == 2 and escolhaMenu == listaMenu[0]:
        codigo = int(input("Informe o código do estudante a atualizar: "))
        atualizarEstudantePorCodigo(codigo)
    else:
        print(f"\n===== [EM DESENVOLVIMENTO] =====\n")


while True:
    print("\nEscolha um dos itens do Menu abaixo.")
    indice, escolhaMenu = menuOpcoes(listaMenu, mensagemEscolha)
    if escolhaMenu == "Sair":
        print("\n***** você escolheu Sair, Saindo do sistema*****\n")
        sairDoSistema()
    elif indice != 0:
        print(f"\n===== [EM DESENVOLVIMENTO] =====\n")

    else:
        print(f"\n***** [{escolhaMenu}] selecionado *****\n")
        navegarMenuOperacoes(escolhaMenu)
