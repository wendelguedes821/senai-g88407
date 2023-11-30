import string
nome = (input("Qual é o seu nome?   "))

print ("Olá ", nome)

idade = int(input("Qual a sua idade?"))

if idade <13:
     print ("Você é uma criança.    ")
elif idade <18:
     print ("Você é um adolescente. ")
elif idade >18 and idade < 60:
     print ("Você é um adulto.      ")
else:
     print ("Você é um idoso.       ")