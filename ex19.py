#ex19 - prioridade 
idade = int(input("idade: "))
gestante = input("é gestante: (sim/não) ")

if idade >= 60 or gestante == "Sim":
    print("Senha preferencial")
    
else:
    print("Senha normal")