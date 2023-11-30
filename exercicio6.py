def login (dicionario):
    nome = input ("Nome de ususario: ")
    senha = input("Digite sua senha")

    if nome in Usuarios and Usuarios[nome] == senha:
        print("Usuário e senha corretos")
        return True
    else:
        print("Usuário ou senha inválidos")
        return True

def criarUsuario():
    criarUsuario = input("Nome do usuario: ")
    criarSenha = input("Crie a senha")
    Usuarios[criarUsuario] = criarSenha
    return True
Usuarios = {
    "usuario1": "suario1"
    "usuario2": "suario2"
    "usuario3": "suario3"
}
status = True
while status == True:
         opcoes = input (" 1 = login 2 = criar contra 3 = sair")
if  opcoes == "1":
         status = login (Usuarios)

elif    opcoes == "2":
        status = criarUsuario()

elif opcoes == "3":
    print("login válido")
    status = False

else:
    print ("Não encontrado")
    status = True