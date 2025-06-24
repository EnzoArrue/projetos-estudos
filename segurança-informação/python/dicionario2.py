#Preencha um dicionario com as informações de 5 produtos, utilize o nome como chave e o preço como valor, solicite dados ao usuario, percorra o dicionario e exiba o nome dos produtos com preço maior que 50,00.
produtos = dict()
for i in range (5):
    nome, preco = input("Nome e preço: ").split()
    preco = float(preco)
    produtos[nome] = preco
    print()

print('-' * 30)
print("Produtos com preço acima de R$50:")
print("-" * 30)
for item in produtos.items():
    nome, preco = item
    if preco > 50.00:
        print(f"Nome: {nome}")
    

