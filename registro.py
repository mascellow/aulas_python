import os
import math

os.system("cls || clear")
#variáveis 
programa = True
cont = 0
soma_salario = 0
qtd_m = 0
idade_maior = -math.inf
idade_menor = math.inf
idades = []

#inicio programa.
while programa:
    os.system("cls || clear")
    #Solicitando operação.
    print("Código | Descrição")
    print("   1   | Adicionar.")
    print("   2   | Exibir resultados.")
    print("   3   | Sair.")
    op = int(input("\n"))
    #Opção onde registramos dados.
    if op == 1:
        os.system("cls || clear")
        cont+=1
        idades.append(int(input("Digite a idade: ")))
        sexo = input("Digite o sexo (F/M): ").upper()
        salario = float(input("Digite o salário: "))
        soma_salario += salario
        if sexo == "F" and salario > 5000:
            qtd_m +=1
    #For para definir idade maior e menor registrada.
    for i in range(len(idades)):
        if idades[i] > idade_maior:
            idade_maior = idades[i]
        if idades[i] < idade_menor:
            idade_menor = idades[i]      
    media_salarial = soma_salario / cont
    #Opção onde exibe todos os dados registrados!    
    if op == 2:
        programa_op = True
        while programa_op:
            os.system("cls || clear")
            print(f"Média Salarial: {media_salarial:.2f}")
            print(f"Maior idade: {idade_maior}")
            print(f"Menor idade: {idade_menor}")
            print(f"QTD Mulheres - Salário > R$5000,00: {qtd_m}")
            opp2 = input("\nDeseja voltar pro menu principal?(S/N): ").upper()
            if opp2 == "S":
                programa_op = False
        
    #Opção que para o programa.
    if op == 3:
        break
