import pandas as pd
# dados = {
#     'nome':  ["Paulo", "Gabriel", "Bryan", "Vandsum"],
#     'idade': [20, 20, 18, 21],
#     'cidade':["Camaçari", "Chique-Chique", "Dias davila", "Rolândia"]
# }

# tabela = pd.DataFrame(dados)
# print(tabela)
# for dado in tabela.values:
#    # print(dado)
#     print(dado[0], dado[1], dado[2])

from operator import truediv
from turtle import pen
import pandas as pd

produtos = {

@@ -6, 14 + 8, 28 @ @
"VENDAS": [22, 35, 40, 64, 85, 78]
}

dF = pd.DataFrame(produtos)
# print(dF)
while True:
    dF = pd.DataFrame(produtos)
    print(dF)

    opcoes = input("""
    Aperte 1 para escolher um mês que você deseja ver os dados.\n
    Aperte 2 para saber a maior venda de todos os meses.\n
    Aperte 3 para sair.
    """)

dF2 = dF.set_index("MESES")
filtroMeses = dF2.loc[input(
    "Escreva o mês em que você deseja ver os dados: ").lower()]
print(dF2)
print(filtroMeses)
   if opcoes == "1":
        dF2 = dF.set_index("MESES")
        filtroMeses = dF2.loc[input(
            "Escreva o mês em que você deseja ver os dados: ").lower()]
        print(filtroMeses)

vendas = dF.set_index("MESES")
filtroMeses = dF2.loc[input(
    "Escreva o mês em que você deseja ver os dados: ").lower()]
   elif opcoes == "2":
        maior_venda = dF["VENDAS"].max()
        print(f"A maior venda foi de: {maior_venda}")

    elif opcoes == "3":
        print("Obrigado por acessar.")
        break

    else:
        print("Opção não encontrada.")
