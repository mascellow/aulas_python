import os
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
os.system("cls || clear")

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

p1 = Pessoa(nome,idade,peso,altura)

with open("Dados_pessoais.txt", "a") as arquivo:
    arquivo.write(f"Nome: {p1.nome},idade: {p1.idade},Peso: {p1.peso},altura: {p1.altura}\n")
    

print("Dados salvos com sucesso!")
os.system("cls || clear")
listaPessoa = []

with open("Dados_pessoais.txt", "r") as arquivo:
    for linha in arquivo:
        nome, idade, peso, altura = linha.split(',')
        listaPessoa.append(Pessoa(nome,idade,peso,altura))
iterador = 0       
for pessoas in listaPessoa:
    iterador+=1
    print(f"Pessoa {iterador}:\n")
    print(f"{pessoas.nome}")
    print(f"{pessoas.idade}")
    print(f"{pessoas.peso}")
    print(f"{pessoas.altura}")