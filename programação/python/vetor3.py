# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas vogais foram lidas. Imprima as vogais.
v = []
vogais = ["a","e","i","o","u","A","E","I","O","U"]
qtd_vogais = 0
vogais_nova = []

for i in range (10):
    caracter = input("Digite um caracter: ")
    v.append(caracter)
    if caracter in vogais:
        qtd_vogais += 1
        vogais_nova.append(caracter)
        print(f"Vogal digitada: {caracter}")

print(f"Vetor completo: {v}. Tiveram {qtd_vogais} vogais e foram {vogais_nova}.")
