# Faça um programa, com uma função que necessite de X argumentos, e que forneça a soma desses X argumentos. OBS: Use def e for.
def somatoria_numeros ():
    soma = 0
    qtd = int(input("Digite uma quantidade de números que deseja escolher: "))
    for i in range (qtd):
        n = int(input(f"Digite o {i+1}° número: "))
        soma = n + soma
    return soma

print(f"O resultado é: {somatoria_numeros()}")
