#Crie uma função que receba um texto e retorne um dicionário com a contagem de cada vogal.
#Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário,
#onde a chave é a vogal considerada e o valor é a quantidade de vezes que essa vogal aparece no texto.

#A função deve receber o texto como entrada e retornar o dicionário.

#Exemplo:
#texto = 'faculdade fatec'

#A função deve devolver o seguinte dicionário:
#{'a': 3, 'e': 2, 'i': 0, 'o': 0, 'u': 1}

texto =input()
def qtd_vogais(texto):
    d = {"a":0, "e":0, "i":0, "o":0, "u":0}
    for letra in texto:
        if letra in "aeiou":
            d[letra] += 1
    return d
print(qtd_vogais(texto))
    
