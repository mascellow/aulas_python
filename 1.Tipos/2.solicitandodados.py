import os

os.system('cls || clear')

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
op = True
os.system('cls || clear')

while op:
    decisao = input("Deseja imprimir os dados?: (S/N)")
    decisao = decisao.upper()
    if decisao == 'S':
        os.system('cls || clear')
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Altura: {altura}")
        print(f"peso: {peso:.1f}")
    elif decisao == 'N':
        op = False
    else:
        print("Decisão inválida. Tente novamente!")