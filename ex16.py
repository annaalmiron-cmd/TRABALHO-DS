# Exercícios 16 - condição com AND

idade = int(input("Digite sua idade: "))
carteira = input("Possui carteira ? (sim/não) ")

if idade >= 18 and carteira == "Sim" :
    print("Pode Dirigir")
else:
    print("Não pode dirigir")