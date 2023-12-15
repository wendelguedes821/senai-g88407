

conta = {
    "saldo": 100,
    "senha": "1234"
}

dado = conta["saldo"]

def autenticar():
    senha = (input("Digite sua senha \n"))
    if senha in conta:
        print("Login com sucesso\n"),

    else:
        print("Login inválido\n")
    return True

def verificarSaldo():
    autenticar()
    print(dado)

def depositarDinheiro():
    autenticar()
    deposito = int(input("Digite o valor que deseja depositar \n"))
    total = deposito + dado
    print(total)


def retirarDinheiro():
    autenticar
    saque = int (int("Digite o valor que deseja sacar \n"))
    total = saque - dado


def sair():
    if sistema == "4":
        return False


run = True
while run:
    sistema = input("""
    l===========================l
    l 1 = Verificar Saldo       l  
    l 2 = Depositar Dinheiro    l
    l 3 = Retirar Dinheiro      l
    l 4 = Sair                  l
    l===========================l
    """)
    if sistema == "1":
        verificarSaldo()
    elif sistema == "2":
        depositarDinheiro()
    elif sistema == "3":
        retirarDinheiro()
    elif sistema == "4":
        sair()
    else:
        run = False
