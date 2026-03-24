#Exercícios 25 - Desconto no pedido

produto = input("Digite o nome do produto")
preco = float(input("Digite o preço do produto: R$ "))
quantiedade =int(input("Digite a quantiedade: "))

total = preco * quantiedade 

if total >50
    desconto = total * 0.10
    total_final = total - desconto
    print("Desconto aplicado: 10%")
else:
    total_final = total - desconto
    print("Sem desconto")

print(f"Produto: {produto}")
print(f"Total a pagar: R$ {total_final: .2f}")
