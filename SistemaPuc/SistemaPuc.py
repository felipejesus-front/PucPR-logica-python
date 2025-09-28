# Todo: Apagar função de variaveis Globais ✅
# Criar sistma de pegar arquivos dos arquivos pra usar nas funções que precisam dos dados ✅
# Criar método de obter próximo código ✅
# Criar metodo que salva dados nos arquivos ✅
# Criar método de criar um novo item, já adicionando o novo item usando a função de salvar dados ✅
# Tudo genericamente, passando somente a entidade ✅


import sys
import json
import os

listaMenu = ["Estudantes", "Disciplinas", "Professores", "Turmas", "Matrículas", "Sair"]
listaCrude = ["Incluir", "Listar", "Atualizar", "Excluir", "Voltar ao menu principal"]
mensagemEscolha = "Informe a opção desejada: "
mensagemFinalizando = "Finalizando Aplicação"


def criaArquivoPraCadaEntidade(entidade):
    if entidade != "Sair":
        nomeArquivo = f"{entidade}.json"
        if not os.path.exists(nomeArquivo):
            dados = []

            with open(nomeArquivo, "w", encoding="utf-8") as arquivoJson:
                json.dump(dados, arquivoJson, ensure_ascii=False)
                print(f"Arquivo '{nomeArquivo}' criado com sucesso.")


def carregarDadosDoJson(entidade):
    nomeArquivo = f"{entidade}.json"
    with open(nomeArquivo, "r", encoding="utf-8") as arquivoJson:
        return json.load(arquivoJson)


def salvarDadosNoJson(entidade, dados):
    nomeArquivo = f"{entidade}.json"
    with open(nomeArquivo, "w", encoding="utf-8") as arquivoJson:
        return json.dump(dados, arquivoJson, ensure_ascii=False)


def obterProximoCodigo(entidade):
    dados = carregarDadosDoJson(entidade)
    maiorCodigo = max((item["codigo"] for item in dados), default=0)
    return 0 if dados == [] else maiorCodigo + 1


def incluirItem(entidade, campos):
    dados = carregarDadosDoJson(entidade)
    codigo = obterProximoCodigo(entidade)
    novoItem = {"codigo": codigo}
    novoItem.update({campo: input(f"{campo}:") for campo in campos})
    dados.append(novoItem)
    salvarDadosNoJson(entidade, dados)
    print(f"\n{entidade[:-1]} cadastrado com sucesso!\n")


def listarItens(entidade):
    dados = carregarDadosDoJson(entidade)
    if dados:
        for dado in dados:
            print(f"===== {dado} =====")
    else:
        print(f"===== Não há {entidade} cadastrados =====")


def codigoExiste(entidade, codigo):
    dados = carregarDadosDoJson(entidade)
    return any(item["codigo"] == codigo for item in dados)


def atualizarItem(entidade, campos):
    dados = carregarDadosDoJson(entidade)
    codigo = int(input("informe o codigo do item que deseja atualizar: "))
    for dado in dados:
        print(dado["codigo"])
        if dado["codigo"] == codigo:
            for campo in campos:
                dado[campo] = input(f"Novo {campo}: ")

            salvarDadosNoJson(entidade, dados)

            print(f"{entidade} atualizado com sucesso!")
            return
        else:
            print(f"\n===== {entidade} não encontrado. =====\n")


def incluirItemComValidacao(entidade, campos, validacoes):
    dados = carregarDadosDoJson(entidade)
    novoItem = {"codigo": obterProximoCodigo(entidade)}

    for campo, (entidadeRelacionada, mensagemErro) in validacoes.items():
        codigo = int(input(f"{campo}: "))
        if not codigoExiste(entidadeRelacionada, codigo):
            print(mensagemErro)
            return
        novoItem[campo] = codigo

    novoItem.update(
        {campo: input(f"{campo}: ") for campo in campos if campo not in validacoes}
    )
    dados.append(novoItem)
    salvarDadosNoJson(entidade, dados)
    print(f"{entidade[:-1]} cadastrado com sucesso!")


# Função genérica para atualizar itens com validação de códigos relacionados
def atualizarItemComValidacao(entidade, campos, validacoes):
    dados = carregarDadosDoJson(entidade)
    codigo = int(input("Informe o código do item a atualizar: "))
    for item in dados:
        if item["codigo"] == codigo:
            for campo, (entidadeRelacionada, mensagemErro) in validacoes.items():
                novoCodigo = int(input(f"Novo {campo}: "))
                if not codigoExiste(entidadeRelacionada, novoCodigo):
                    print(mensagemErro)
                    return
                item[campo] = novoCodigo

            for campo in campos:
                if campo not in validacoes:
                    item[campo] = input(f"Novo {campo}: ")

            salvarDadosNoJson(entidade, dados)
            print(f"{entidade[:-1]} atualizado com sucesso!")
            return
    print(f"===== {entidade[:-1]} não encontrado. =====")


def excluirItem(entidade):
    dados = carregarDadosDoJson(entidade)
    codigo = int(input("informe o codigo do item que deseja atualizar: "))
    for dado in dados:
        if dado["codigo"] == codigo:
            dados.remove(dado)

            salvarDadosNoJson(entidade, dados)

            print(f"\n===== {dado} excluído com sucesso. =====")
            return
    print(f"\n===== Não há {entidade} cadatrados(as). =====\n")


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
        else:
            print("\nOpção inválida.\n")


def navegarMenuOperacoes(entidade, campos):
    validacoes = {
        "Turmas": {
            "codigoProfessor": (
                "Professores",
                "===== Código do professor não encontrado. =====",
            ),
            "codigoDisciplina": (
                "Disciplinas",
                "===== Código da disciplina não encontrado. =====",
            ),
        },
        "Matrículas": {
            "codigoTurma": ("Turmas", "===== Código da turma não encontrado. ====="),
            "codigoEstudante": (
                "Estudantes",
                "===== Código do estudante não encontrado. =====",
            ),
        },
    }

    while True:
        print(f"\n***** [{entidade}] Menu de operações: *****\n")
        indice, escolhaCrude = menuOpcoes(listaCrude, mensagemEscolha)
        if escolhaCrude == "Voltar ao menu principal":
            break
        elif escolhaCrude == "Incluir":
            if entidade in validacoes:
                incluirItemComValidacao(entidade, campos, validacoes[entidade])
            else:
                incluirItem(entidade, campos)
        elif escolhaCrude == "Listar":
            listarItens(entidade)
        elif escolhaCrude == "Atualizar":
            if entidade in validacoes:
                atualizarItemComValidacao(entidade, campos, validacoes[entidade])
            else:
                atualizarItem(entidade, campos)
        elif escolhaCrude == "Excluir":
            excluirItem(entidade)


# Campos de cada entidade
camposEntidades = {
    "Estudantes": ["nome", "cpf"],
    "Professores": ["nome", "cpf"],
    "Disciplinas": ["nome"],
    "Turmas": ["codigoProfessor", "codigoDisciplina"],
    "Matrículas": ["codigoTurma", "codigoEstudante"],
}

for entidade in listaMenu:
    criaArquivoPraCadaEntidade(entidade)

while True:
    print("\nEscolha um dos itens do Menu abaixo.")
    indice, escolhaMenu = menuOpcoes(listaMenu, mensagemEscolha)
    if escolhaMenu == "Sair":
        print("\n***** você escolheu Sair, Saindo do sistema*****\n")
        sairDoSistema()
    elif escolhaMenu in camposEntidades:
        navegarMenuOperacoes(escolhaMenu, camposEntidades[escolhaMenu])
    else:
        print(f"\n===== Menu inválido =====\n")
