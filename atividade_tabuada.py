import os
os.system("cls || clear")

numero = int(input("Digite um número para saber a tabuada: "))
soma = 0
for i in range(11):
    soma = numero * i
    print(f"{numero} X {i} = {soma}")