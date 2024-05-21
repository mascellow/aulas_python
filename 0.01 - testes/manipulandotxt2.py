import os
class Livro:
    def __init__(self, nome, autor, categoria, preco):
        self.nome = nome
        self.autor = autor
        self.categoria = categoria
        self.preco = preco
os.system("cls || clear")
livros = []
for i in range(3):
    nome = input("Nome do livro: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    livro = Livro(nome,autor,categoria,preco)
    livros.append(livro)

with open("Catálogo_Livros.txt", "a") as arquivo:
    for livro in livros:
        arquivo.write(f"Nome: {livro.nome},Autor: {livro.autor},Categoria: {livro.categoria},Preço: {livro.preco}\n")