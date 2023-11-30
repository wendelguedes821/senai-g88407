
def calculoCustoViagem(distancia, veiculo):
    if veiculo == "carro":
        custo = 0.50
    elif veiculo == "moto":
        custo = 0.20    
    elif veiculo == "bicicleta":
        custo = 0.10  
    else:
        print("Tipo de veiculo invalido ")
    custoDeViagem = distancia * custo
    return custoDeViagem