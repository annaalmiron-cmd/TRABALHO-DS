# Exercícios 21 - Aprovação alternativa

nota = float(input("Nota: "))
frequencia = float(input("Frequência (%): "))

if nota >= 7 or frequencia >= 90:
    print("Sistema especial de Aprovação")
else:
    print("Aluno em avaliação")