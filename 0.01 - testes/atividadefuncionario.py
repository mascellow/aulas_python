import os

class Funcionario:
    def __init__(self, nome, nascimento, rg, cpf):
        self.nome = nome
        self.nascimento = nascimento
        self.rg = rg
        self.cpf = cpf


def limpatela():
    os.system("cls || clear")

def ler_dados_funcionario(funcionarios):
    for i in range(5):
        limpatela()
        print(f"Cadastro - Funcionário {i+1}")
        nome = input(f"Digite o nome: ")
        nascimento = input("Digite a data de nascimento: ")
        rg = input("Digite o RG: ")
        cpf = input("Digite o CPF: ")
        funcionario = Funcionario(nome,nascimento,rg,cpf)
        funcionarios.append(funcionario)

def salvar(funcionarios):
    with open("Funcionarios.txt", "w", encoding="utf-8")as arquivo:
        for funcionario in funcionarios:
            arquivo.write(f"Nome: {funcionario.nome},Data de nascimento: {funcionario.nascimento},RG: {funcionario.rg},CPF: {funcionario.cpf}\n")

def exibir_dados(lista_funcionarios):
    with open("Funcionarios.txt", "r", encoding="utf-8")as arquivo:
        for linha in arquivo:
            nome,nascimento,rg,cpf = linha.split(",")
            lista_funcionarios.append(Funcionario(nome,nascimento,rg,cpf))
    iterador = 0
    for funcionario in lista_funcionarios:
        iterador +=1
        print(f"Funcionário {iterador}\n")
        print(f"{funcionario.nome}")
        print(f"{funcionario.nascimento}")
        print(f"{funcionario.rg}")
        print(f"{funcionario.cpf}")

limpatela()
funcionarios = []
lista_funcionarios = []
print("=== Cadastro de funcinários ===")

ler_dados_funcionario(funcionarios)
salvar(funcionarios)
limpatela()
exibir_dados(lista_funcionarios)