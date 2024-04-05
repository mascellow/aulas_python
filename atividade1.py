import os

os.system("cls||clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
notaUm = float(input("Digite sua 1ª nota: "))
notaDois = float(input("Digite sua 2ª nota: "))
notaTres = float(input("Digite sua 3ª nota: "))
notaQuatro = float(input("Digite sua 4ª nota: "))

media = (notaUm+notaDois+notaTres+notaQuatro)/4
os.system("cls||clear")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print("-----------------")
print(f"Nota 1: {notaUm}")
print(f"Nota 2: {notaDois}")
print(f"Nota 3: {notaTres}")
print(f"Nota 4: {notaQuatro}")
print("")
print(f"Média: {media:.1f}")