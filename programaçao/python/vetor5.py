#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
#cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

v1 = []
v2 = []
v3 = []

for i in range(10):
    elementos = int(input(f"Digite o {i+1}° elemento: "))
    v1.append(elementos)

for i in range(10):
    elementos = int(input(f"Digite o {i+1}° elemento: "))
    v2.append(elementos)

for i in range(10):
    v3.append(v1[i])
    v3.append(v2[i])

print(f"Os valores intercalados são: {v3}")
    



