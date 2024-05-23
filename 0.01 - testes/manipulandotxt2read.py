import os

def limpatela():
    os.system("cls || clear")

def mostrarLivros():
    while True:
        limpatela()
        op = input("Deseja ver os livros cadastrados?(S/N): ").upper()
        if op == "S":
            break

    with open("Catálogo_Livros.txt", "r", encoding="utf-8")as arquivo:
        livros_cadastrados = arquivo.read()
    print(livros_cadastrados)


mostrarLivros()