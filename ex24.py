# exercícios 24 - total de pedidos 

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
quantiedade = int(input("Digitea quantiedade: "))

total = preco * quantiedade

print(f"Produto: {produto}")
print(f"Quantiedade{quantiedade}")
print(f"Total: R$ {total: .2f}")