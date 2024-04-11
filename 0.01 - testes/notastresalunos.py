import os
os.system("cls || clear")
notas_alunos = [[0,0,0],[0,0,0],[0,0,0]]
alunos = [" "," "," "]
medias = [0,0,0]


for i in range(0,3):
    soma = 0
    print(" ")
    alunos[i] = input("Digite o nome do aluno: ")
    for l in range(0,3):
        notas_alunos[i][l] = float(input(f"{i+1}ª ALUNO: |{alunos[i]}| - Digite a {l+1}ª nota:"))
        soma += notas_alunos[i][l]
        medias[i] = soma / 3
        
        
        
os.system("cls || clear")

for i in range(0,3):
    print("")
    print(f"NOME DO ALUNO: {alunos[i]}")
    print("")
    for l in range(0,3):
        print(f"{l+1}ª Nota: {notas_alunos[i][l]}")
    print(f"MÉDIA: {medias[i]:.1f}")