import funcao
distancia = int(input("Qual é a distância da viagem? "))
veiculo = input("Qual o veiculo que irá ser usado nessa viagem? ")

custo = funcao.calculoCustoViagem(distancia, veiculo)
print (custo)
