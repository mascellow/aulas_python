import os
class Livros:
    def __init__(self, nome, autor, categoria, preco):
        self.nome = nome
        self.autor = autor
        self.categoria = categoria
        self.preco = preco

def limpatela():
    os.system("cls || clear")

def menu():
    print("=== GERENCIADOR BIBLIOTECA ===")
    print("==============================")
    print("|Código | Descrição          |")
    print("|----------------------------|")
    print("| 1     | Cadastrar Livro    |")
    print("| 2     | Livros Cadastrados |")
    print("|============================|")

def salvar(livros):
    with open("Catálogo_Livros.txt", "a", encoding="utf-8")as arquivo:
        for livro in livros:
            arquivo.write(f"Nome: {livro.nome}, Autor: {livro.autor}, Categoria: {livro.categoria}, Preço: R${livro.preco:.2f}\n")

def mostrarLivros():
    with open("Catálogo_Livros.txt", "r", encoding="utf-8")as arquivo:
        livros_cadastrados = arquivo.read()
    print(livros_cadastrados)

livros = []

while True:
    limpatela()
    menu()
    cod = int(input("Digite uma opção: "))
    match cod:
        case 1:
            limpatela()
            qtd_livros = int(input("Quantos livros deseja cadastrar?: "))
            for i in range(qtd_livros):
                os.system("cls || clear")
                print("=== Cadastro de livros ===\n")
                nome = input("Digite o nome do livro: ")
                autor = input("Digite o nome do autor: ")
                categoria = input("Digite a categoria: ")
                preco = float(input("Digite o preço: "))
                livro = Livros(nome,autor,categoria,preco)    
                livros.append(livro)
            salvar(livros)
        case 2:
            while True:
                limpatela()
                mostrarLivros()
                op = input("\nDeseja voltar ao menu principal?(S/N): ").upper()
                if op == "S":
                    break


