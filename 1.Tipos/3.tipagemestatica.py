import os

os.system("cls || clear")

nome: str = input("Digite seu nome: ")
idade: int = int(input("Digite sua idade: "))
peso: float = float(input("Digite seu peso: "))

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.3f}")


