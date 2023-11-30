loginsSenhas = {
    "usuario1": "123451",
    "usuario2": "123452",
    "usuario3": "123453",
}

usuario = input("Digite seu usuário. ")
senha = input("Digite sua senha. ")
if usuario and senha in loginsSenhas[usuario] == senha:
    print("Login bem sucessdido!")
else:
    print("Login inválido")