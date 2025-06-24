# Crie um programa que solicite ao usuário diversos números inteiros,
# exiba a média e todos os números que estejam abaixo da média.

qtd = int(input("Digite quantos números deseja: "))
v = qtd * [0]

for i in range(qtd):
    v[i] = int(input("Valor do número: "))

print(f"Números digitados: {v}")

soma = 0
for i in range(qtd):
    soma = soma + v[i]

m = soma / qtd
print(f"A média é: {m:.2f}")

print("Números abaixo da média:")
for i in range(qtd):
    if v[i] < m:
        print(v[i])

