#Crie um dicionário com o RA e três notas de 5 alunos, calcule e exiba a média de cada um.
#Dicionário
alunos = dict()

for i in range(5):
    RA = int(input("RA: "))
    n1, n2, n3 = input("Notas: ").split()
    n1, n2, n3 = float(n1), float(n2), float(n3)
    alunos[RA] = [n1, n2, n3]

for aluno in alunos.items():
    RA, notas = aluno
    print(f"RA: {RA}")
    media = (notas[0] + notas[1] + notas[2]) / 3
    print(f"Média = {media:.2f}")

