import os
class Livros:
    def __init__(self, nome, autor, categoria, preco):
        self.nome = nome
        self.autor = autor
        self.categoria = categoria
        self.preco = preco

def salvar(livros):
    with open("Catálogo_Livros.txt", "w", encoding="utf-8")as arquivo:
        arquivo.write("=== Livros Cadastrados ===")
        for livro in livros:
            arquivo.write(f"Nome: {livro.nome}, Autor: {livro.autor}, Categoria: {livro.categoria}, Preço: {livro.preco}")
livros = []

for i in range(1):
    os.system("cls || clear")
    print("=== Cadastro de livros ===\n")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    categoria = input("Digite a categoria: ")
    preco = float(input("Digite o preço: "))
    livro = Livros(nome,autor,categoria,preco)    
    livros.append(livro)


salvar(livros)