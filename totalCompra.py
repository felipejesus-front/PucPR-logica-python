nomeProduto = input("Digite o nome do produto: ")
precoProduto = float(input("Digite o valor do produto: "))
quantidadeProduto = int(input("digite a quantidade do produto: "))

valorTotal = precoProduto * quantidadeProduto

valorComDesconto = valorTotal - (valorTotal * 0.15)

print(f"O valor de {quantidadeProduto} {nomeProduto} é: ", valorTotal)
print(
    f"MAS como o gerente está maluco, estamos dando 15% de desconto pra fregueses especiais e com isso o valor total passa a ser: {valorComDesconto}"
)
