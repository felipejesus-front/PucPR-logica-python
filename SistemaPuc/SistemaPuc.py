# Parei pra pesquisar sobre ler e criar arquivos pensei em criar os arquivos automaticamente a partir do listaMenu
# pro caso de os itens mudarem, por exemplo.
# acabei me empolgando e pensei "será q eu n consigo criar as variaveis globais também baseado no listaMenu?"
# pesquisei e descobri que posso fazer isso utilizando a função globals(), vou testar essa possibilidade de
# gerar as variaveis globais a partir do listaMenu
# Deixei o Estudante já preenchido pra mostrar q ele só cria o arquivo se já não existir um. e tbm pra mostrar a leitura dele ao inicar a aplicação.

import sys
import json
import os

listaMenu = ["Estudantes", "Disciplinas", "Professores", "Turmas", "Matrículas", "Sair"]
listaCrude = ["Incluir", "Listar", "Atualizar", "Excluir", "Voltar ao menu principal"]
mensagemEscolha = "Informe a opção desejada: "
mensagemFinalizando = "Finalizando Aplicação"
idEstudante = 0


def criaArquivoPraCadaEntidade(entidade):
    if entidade != "Sair":
        nomeArquivo = f"{entidade}.json"
        if not os.path.exists(nomeArquivo):
            dados = []

            with open(nomeArquivo, "w", encoding="utf-8") as arquivoJson:
                json.dump(dados, arquivoJson, ensure_ascii=False)
                print(f"Arquivo '{nomeArquivo}' criado com sucesso.")


def iniciaVariaveisGlobais():
    escopoGlobal = globals()
    global idEstudante

    for entidade in listaMenu:
        nomeArquivo = f"{entidade}.json"
        criaArquivoPraCadaEntidade(entidade)

        if entidade != "Sair":
            with open(nomeArquivo, "r", encoding="utf-8") as f:
                escopoGlobal[entidade] = json.load(f)

            print(f"Entidade carregada:\n {entidade} = {escopoGlobal[entidade]}\n")

        if Estudantes and entidade == "Estudantes":
            idEstudante = max(e["codigo"] for e in Estudantes) + 1
            print(f"\nPróximo ID de estudante será: {idEstudante}\n")


iniciaVariaveisGlobais()


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
        print(Estudantes)
        for item in Estudantes:
            print(f"===== {item} =====")
    else:
        print("===== Não há estudantes cadastrados =====")


def incluirEstudante():
    global idEstudante
    global Estudantes
    nome = input("Nome do estudante: ")
    cpf = input("CPF do estudante: ")
    estudante = {"codigo": idEstudante, "nome": nome, "cpf": cpf}
    Estudantes.append(estudante)
    idEstudante += 1

    with open("Estudantes.json", "w", encoding="utf-8") as f:
        json.dump(Estudantes, f, ensure_ascii=False)

    print("Estudante cadastrado com sucesso!")


def excluirEstudantePorCodigo(codigo):
    for estudante in Estudantes:
        if estudante["codigo"] == codigo:
            Estudantes.remove(estudante)

            with open("Estudantes.json", "w", encoding="utf-8") as f:
                json.dump(Estudantes, f, ensure_ascii=False)

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

            with open("Estudantes.json", "w", encoding="utf-8") as f:
                json.dump(Estudantes, f, ensure_ascii=False)

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
