from cProfile import run
from operator import truediv
import os


def limparTerminal():
    if os.name == 'nt':       
        os.system('cls')

    else:
    
        os.system('clear')


def Menu():
    print("""
    |=================================================|
    |                    M E N U                      |
    |=================================================|                   
    |       Opções          |         Preço           |
    |=================================================|
    | 1 -  Lasanha          |   R$ 10.00              |           
    | 2 -  Macarrão         |   R$ 15.00              |
    | 3 -  Pizza            |   R$ 20.00              |
    | 4 -  burguer          |   R$ 12.00              |
    | 5 -  Bauru            |   R$ 6.00               |
    |=================================================|
    """)


def exibirMenu():
    while True:
        print("""
    |=================================================|
    |                    M E N U                      |
    |=================================================|                   
    |       Opções          |         Preço           |
    |=================================================|
    | 1 -  Lasanha          |   R$ 10.00              |           
    | 2 -  Macarrão         |   R$ 15.00              |
    | 3 -  Pizza            |   R$ 20.00              |
    | 4 -  Burguer          |   R$ 12.00              |
    | 5 -  Bauru            |   R$ 6.00               |
    |=================================================|
    """)
        voltarMenu = input("Digite 's' para voltar ao menu. ")
        if voltarMenu.lower() == 's':
            break


def AddItem(lista):

    Menu()
    while True:
        produto = input(
            "Digite o número do pedido ou aperte 's' para voltar ao menu. ")
        if produto.lower() == 's':
            break
        elif produto.isdigit() and int(produto) in range(1, 6):
            produto = int(produto)
            nomeProduto = {
                1: "Lasanha", 2: "Macarrão", 3: "Pizza", 4: "Burguer", 5: "Bauru"
            }[produto]
            precoProduto = {
                1: 10.00, 2: 15.00, 3: 20.00, 4: 12.00, 5: 6.00
            }[produto]
            lista[nomeProduto] = precoProduto
            print(
                f"O item {nomeProduto} foi adicionado com sucesso e o preço dele é: {precoProduto}")
        else:
            print("Opção inválida")


def removerItem(lista):
    while True:
        if (lista):
            print("Produtos no pedido.")
            for i, produto in enumerate(lista, start=1):
                print("{}. {}".format(i, produto))

                escolha = input(
                    "Digite o número do produto que deseja remover ou 's' para voltar ao menu. ")
                if escolha.lower() == "s":
                    break
                elif escolha.isdigit() and int(escolha) in range(1, len(lista)+ 1 ):
                    itemRemovido = list(lista.keys())[int(escolha) - 1]
                    del lista[itemRemovido]
                    print("{} removido do pedido.".format(itemRemovido))
                else:
                    print("Opção inválida ou não há pedidos no pedido para remover.")
                    break


def mostrasPedido(lista):
    while True:
        if lista:
            print(""" 
|*******************************************4|
|           NOME                   PREÇO    |
|*******************************************|""")

        for produto, preco in lista.items():
            print("|           {}               |   R${:.2f} |".format(produto, preco))

        escolha = input("Pressione 's' para voltar ao menu")
        if escolha.lower() == 's':
            break
        else:
            print("Opção inválida ou não há pedidos no pedido para remover.")


def calcularTotal(lista):
    while True:
        if lista:
            total = sum(lista.values())
            print("O total do pedido é R${}".format(total))
            escolha = input("Pressione 's' para voltar ao meunu")
            if escolha.lower() == 's':
                break
            else:
                print("Opção inválida")
        else:
                print("Não há items no pedido")
        
        break

listaProdutos = {}
run = True
while run:
    limparTerminal()
    sistema = input("""
        l*********************************************************l
        l                    SELECIONE UMA OPÇÃO                  l                                 
        l                                                         l
        l*********************************************************l                
        l  1 = Exibir Menu   2 = Add item        3 = Remover item l                                         
        l  4 = Exibir Pedido 5 = Calcular total  6 = Sair         l                             
        l*********************************************************l
        """)
    if sistema == "1":
        exibirMenu()
    elif sistema == "2":
        AddItem(listaProdutos)
    elif sistema == "3":
        removerItem(listaProdutos)
    elif sistema == "4":
        mostrasPedido(listaProdutos)
    elif sistema == "5":
        calcularTotal(listaProdutos)
    elif sistema == "6":
        break
    else:
        print("Função não identificada")
