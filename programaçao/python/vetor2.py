#Faça um Programa que leia 4 notas, mostre as notas e a média na tela. OBS: Use listas
notas = []
media = 0
for i in range(4):
    nota = float(input(f"Digite a {i+1}° nota: "))
    notas.append(nota)
    media += nota

media = media/4

print(f"As notas são:{notas} e a média é: {media} ")


