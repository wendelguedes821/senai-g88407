
conta = {
    "12345": 1450.00

}

senha = input("Digite sua senha ")
saldo = input("Digite seu saldo ")
if senha and saldo in conta[senha] == saldo:
    print("Login efetuado com sucesso!")
else:
    print("Login inválido")


def operacoesBasicas():
    while True:
        print("""

    1 = Verificar Saldo
    2 = Depositar Dinheiro
    3 = Retirar Dinheiro

    """)


def verificarSaldo():
    operacoesBasicas()
    while True:
        print(saldo)


def depositarValor():
    operacoesBasicas()
    deposito = input("Digite o valor que deseja depositar.")
    depositado = deposito + saldo
    print("Seu saldo agora é", depositado)


def retirarValor():
    operacoesBasicas()
    saque = ("digite o valor que deseja sacar")
    saque = saldo - saque
    print(saque)
