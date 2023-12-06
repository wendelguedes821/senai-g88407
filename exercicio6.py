from curses.ascii import isdigit


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

    def ExibirMenu():
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

    def AddItem():

        Menu()
        while True:
            produto = input(
            "Digite o número do pedido ou aperte 's' para voltar ao menu. ")
            if voltarMenu.lower() == 's':
                break
            elif produto.isdigit() and int (produto) in range (1,6):
                produto = int(produto)
                nomeProduto = {
                    1: "Lasanha", 2: "Macarrão", 3: "Pizza", 4: "Burguer", 5: "Bauru"
                } [produto]
                precoProduto = {
                    1: 10.00, 2: 15.00, 3: 20.00, 4: 12.00, 5: 6.00
                } [produto]
                lista [nomeProduto] = precoProduto
                print(f"O item {nomeProduto} foi adicionado com sucesso e o preço dele é: {precoProduto}")
            else:
                print("Opção inválida")
