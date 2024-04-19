import os

os.system("cls || clear")
numeros = []
programa = True
while programa:
    numero = int(input("Digite um número:"))
    if numero <= 0:
        break
    else:
        numeros.append(numero)
        
minimo = min(numeros)
maximo = max(numeros)

os.system("cls || clear")

for i in numeros:
    print(i, end="|")
print(f"\nMaior número: {maximo}")
print(f"\nMenor número: {minimo}")