from operator import truediv
from turtle import pen
import pandas as pd

produtos = {
    "MESES": ["janeiro", "fevereiro", "março", "janeiro", "fevereiro", "março"],
    "PRODUTOS": ["Xiaomi", "iPhone", "Samsung", "Huawei", "Nokia", "Motorola"],
    "VENDAS": [22, 35, 40, 64, 85, 78]
}

while True:
    dF = pd.DataFrame(produtos)
    print(dF)

    opcoes = input("""
    Aperte 1 para escolher um mês que você deseja ver os dados.\n
    Aperte 2 para saber a maior venda de todos os meses.\n
    Aperte 3 para sair.
    """)

    if opcoes == "1":
        dF2 = dF.set_index("MESES")
        filtroMeses = dF2.loc[input("Escreva o mês em que você deseja ver os dados: ").lower()]
        print(filtroMeses)

    elif opcoes == "2":
        maior_venda = dF["VENDAS"].max()
        print(f"A maior venda foi de: {maior_venda}")

    elif opcoes == "3":
        print("Obrigado por acessar.")
        break
    
    else:
        print("Opção não encontrada.")