import os

os.system("cls || clear")

notas = []
soma = 0
iterador = 1
for i in range(4):
    nota = float(input("Digite uma nota: "))
    soma += nota
    notas.append(nota)
    

os.system("cls || clear")
for notaa in notas:
    print(f"{iterador}ª Nota: {notaa}")
    iterador += 1
    
media = soma / 4

print("-------------")
print(f"MÉDIA: {media:.1f}")