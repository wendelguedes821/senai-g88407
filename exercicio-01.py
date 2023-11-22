from operator import truediv
from re import sub


nome = "wendel"
idade = 20
altura = 1.72
estudante = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudante))

#operadores matemáticos
#soma
soma = 5+3
#subtracao
subtracao = 5-3
#multiplicação
mult = 5*3
divisao = 5/3

#operadores de comparação
engual = 5==3
diferente = 5!=3
maior = 5>3
menor = 5<3

#operadores lógicos
e = True and False
ou = True or False
nao = not True

print ("Operadore matemáticos \n")
print (soma, "soma \n", subtracao, "subtração \n", mult, "multiplicação \n", divisao, "divisão \n")

print ("operadores de comparação \n")
print (engual, "engual \n",diferente, "diferente \n",maior, "maior",menor, "menor")

print ("Operadores Lógicos \n")
print (e, ou, nao, )