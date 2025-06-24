#Peça as 4 notas de 5 alunos, calcule e armazene a média de cada um, e mostre quantos alunos tiveram média maior ou igual a 7.
media_aluno = []
qtd_aluno = 0

for i in range(5):  # Corrigido de 3 para 5
    media = 0

    for x in range(4):
        nota = float(input(f"Digite a {x+1}ª nota do {i+1}º aluno: "))
        media += nota

    nova_media = media / 4
    if nova_media >= 7:
        qtd_aluno += 1

    media_aluno.append(nova_media)

print(f"Médias dos alunos: {media_aluno}")
print(f"Número de alunos com média maior ou igual a 7.0: {qtd_aluno}")

