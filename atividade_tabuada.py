import os
os.system("cls || clear")

numero = int(input("Digite um número para saber a tabuada: "))
iterador = 0
soma = 0
for i in range(11):

    soma = numero * iterador
    print(f"{numero} X {iterador} = {soma}")
    iterador += 1