import os
import time
login_aproved = "mascellow"
password_aproved = "lixeira123"
os.system("cls || clear")
op = True

while op == True:
    os.system("cls || clear")
    print("==== SENAI ====")
    print("")
    login = input("LOGIN: ")
    password = input("PASSWORD: ")

    if login == login_aproved and password == password_aproved:
        op = False
        os.system("cls || clear")
        print(f"Seja bem vindo, {login}")
    else: 
        op = True
        os.system("cls || clear")
        print("Usuário ou senha inválidos!!")
        time.sleep(2)