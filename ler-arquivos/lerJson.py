import json

with open("exemplo.json", "r", encoding="utf-8") as arquivo:
    conteudo = json.load(arquivo)

print(conteudo)
