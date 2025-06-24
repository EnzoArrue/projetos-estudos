#Preencha um dicionário com as informações de 5 produtos
#-	Utilize o nome do produto como chave e o preço como valor.
#-	Solicite os dados ao usuário
#-	Percorra o dicionário e exiba o nome dos produtos com preço 
#superior a R$ 50,00.

#Exemplo:
#Veja um exemplo da estrutura do dicionário.
#{'mouse': 80.0, 'caneta': 3.0, 'Pen drive': 100.0,'Teclado': 30.0, 'Lápis': 1.5}

produtos = {}
for i in range(5):
    nome=input("Nome: ")
    preco=float(input("Valor: "))
    produtos[nome]=preco

for nome, preco in produtos.items():
    if preco > 50.00:
        print(f"{nome}:{preco:.2f}", end=' ')
                

