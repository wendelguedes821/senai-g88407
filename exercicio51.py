
def login(lista):
    usuario = input("Digite seu usuário. ")
    senha = input("Digite sua senha.   ")
    if usuario in lista and lista[usuario] == senha:

        print("Login efetuado com SUCESSO!")

        return True

    else:
        print("Usuário ou senha INCORRETOS")

        return False


def registro(lista):
    usuario = input("Digite o nome de usuário. ")
    senha = input("Digite sua senha.         ")
    lista[usuario] == senha
# ----------------------------------------------------------------


listaUsuarios = {
    "usuario1": "1234",
    "usuario2": "1234",
}
status = False
while status == False:
    menu = input("""
    **************************************************\n
    1 = LOGIN         2 = CRIAR CONTA         3 = SAIR\n
    **************************************************
    """)
    if menu == "1":
        status = login(listaUsuarios)
    elif menu == "2":
        status = criarUsuario(listaUsuarios)
    elif menu == "3":
        print("TCHAI E TOME N EH VDD?? ")
        status = True
    else:
        print("Comando não existe.")
