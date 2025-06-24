#Cadastre o RA e três notas de 5 alunos em um dicionário e exiba a média de cada um.
alunos = {}
for i in range(5):
    RA = int(input("RA:"))
    n1 = float(input("N1: "))
    n2 = float(input("N2: "))
    n3 = float(input("N3: "))
    notas =[n1, n2, n3]
    alunos[RA]= [n1, n2, n3] #ou alunos[RA]= notas

for aluno in alunos.items():
    RA, notas = aluno
    media = (notas[0] + notas[1] + notas[2])/ 3
    print(f"Média: {media:.2f}")

