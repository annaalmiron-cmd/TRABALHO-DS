#ex 17 - login simples 
usuario = input("usuário: ")
senha = input("sistemas: ")

if usuario == "admin" and senha == "123":
    print("Login realizado")
else:
    print("Usuário ou senha incorretos.")