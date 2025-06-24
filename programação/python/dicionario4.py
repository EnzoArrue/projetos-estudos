#Crie uma função que conte a quantidade de cada vogal em um texto digitado pelo usuário.
#Dicionário
def vogais(texto):
    d = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letra in texto:
        if letra in "aeiou":
            d[letra] += 1
    return d

texto = input()
print(vogais(texto))

