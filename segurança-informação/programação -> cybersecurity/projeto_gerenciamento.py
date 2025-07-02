#Você foi contratado para desenvolver um sistema de gerenciamento de inventário de produtos para uma loja. 
#Esse sistema deve conter acesso seguro por login e senha e oferecer funcionalidades básicas como adicionar, remover, 
#atualizar, buscar e exibir produtos, além de permitir criptografia dos dados sensíveis e ordenação do inventário com diferentes algoritmos.
#Requisitos do sistema:
#Autenticação segura
#O sistema deve solicitar login e senha para acesso.
#As senhas devem ser armazenadas em um arquivo (login.txt) utilizando hash SHA-256.
#Caso o arquivo esteja ausente ou vazio, o sistema solicitará o cadastro inicial do usuário.
#Gerenciamento de produtos
#Cada produto do inventário deve conter:
#ID único
#Nome
#Quantidade (criptografada)
#Preço (criptografado)
#Informação se é importado
#Criptografia
#Os valores de quantidade e preço devem ser cifrados usando uma cifra de substituição personalizada ao serem armazenados.
#Deve ser possível decifrar os dados para exibição correta.
#Operações disponíveis
#O usuário, ao acessar o sistema, poderá:
#Adicionar um novo produto
#Remover produtos por ID ou nome
#Atualizar os dados de um produto
#Buscar produtos por ID ou nome
#Exibir todos os produtos do inventário (com dados decifrados)
#Ordenar o inventário por preço usando os algoritmos Bubble Sort ou Selection Sort
#Atualizar a senha do usuário
#Ordenação e desempenho
#O usuário poderá escolher o algoritmo de ordenação.
#Caso o inventário ultrapasse 100 itens, o sistema deverá usar Merge Sort automaticamente.
import hashlib

def criar_hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()
def verificar_login():
    try:
        with open('login.txt', 'r') as f:
            conteudo = f.readlines()
        if not conteudo:
            print("Arquivo de login vazio, crie um novo login e senha.")
            usuario = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            hash_senha = criar_hash_senha(senha)
            with open('login.txt', 'w') as f:
                f.write(usuario + '\n')
                f.write(hash_senha + '\n')
            print("Usuário e senha criados com sucesso!")
            return usuario, hash_senha
        usuario = conteudo[0].strip()
        hash_senha_armazenada = conteudo[1].strip()
        usuario_input = input("Digite o nome de usuário: ")
        senha_input = input("Digite a senha: ")
        hash_senha_input = criar_hash_senha(senha_input)
        if usuario_input == usuario and hash_senha_input == hash_senha_armazenada:
            print("Login bem-sucedido!")
            return usuario, hash_senha_armazenada
        else:
            print("Usuário ou senha incorretos.")
            return None, None
    except FileNotFoundError:
        print("Arquivo de login não encontrado. Criando novo arquivo...")
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        hash_senha = criar_hash_senha(senha)
        with open('login.txt', 'w') as f:
            f.write(usuario + '\n')
            f.write(hash_senha + '\n')
        print("Usuário e senha criados com sucesso!")
        return usuario, hash_senha
      
def adicionar_produto(inventario):
    id_produto = input("Digite o ID do produto: ").strip()
    nome = input("Digite o nome do produto: ").strip()
    quantidade = input("Digite a quantidade do produto: ").strip()
    preco = input("Digite o preço do produto: ").strip()
    quantidade_cifrada = ''.join(cifrado(c) for c in quantidade)
    preco_cifrado = ''.join(cifrado(c) for c in preco)
    importado = input("O produto é importado? (sim/não): ").strip().lower() == "sim"
    inventario[id_produto] = [nome, quantidade_cifrada, preco_cifrado, importado]
    print("Produto adicionado com sucesso!")
    
def remover_produto(inventario):
    if not inventario:
        print("Inventário vazio. Nenhum produto para remover.")
        return
    print("Escolha o método para remoção:")
    print("1. Remover pelo ID")
    print("2. Remover pelo nome")
    opcao = input("Digite sua escolha (1/2): ").strip()
    if opcao == '1':
        id_produto = input("Digite o ID do produto a ser removido: ").strip()
        if id_produto in inventario:
            inventario.pop(id_produto)
            print(f"Produto com ID {id_produto} removido com sucesso!")
        else:
            print("Produto com o ID fornecido não encontrado.")
    elif opcao == '2':
        nome_produto = input("Digite o nome do produto a ser removido: ").strip().lower()
        encontrados = [(id_produto, dados) for id_produto, dados in inventario.items() if nome_produto in dados[0].lower()]
        if encontrados:
            for id_produto, dados in encontrados:
                print(f"Produto encontrado: ID: {id_produto}, Nome: {dados[0]}")
            confirmar = input("Deseja remover todos os produtos encontrados? (sim/não): ").strip().lower()
            if confirmar == 'sim':
                for id_produto, _ in encontrados:
                    inventario.pop(id_produto)
                print("Todos os produtos encontrados foram removidos.")
            else:
                id_especifico = input("Digite o ID do produto específico a ser removido: ").strip()
                if id_especifico in inventario:
                    inventario.pop(id_especifico)
                    print(f"Produto com ID {id_especifico} removido com sucesso!")
                else:
                    print("Produto com o ID fornecido não encontrado.")
        else:
            print("Nenhum produto com o nome fornecido foi encontrado.")
    else:
        print("Opção inválida. Tente novamente.")
        
def exibir_inventario(inventario):
    if not inventario:
        print("Inventário vazio.")
    else:
        for id_produto, dados in inventario.items():
            nome = dados[0]
            quantidade_cifrada = dados[1]
            preco_cifrado = dados[2]
            quantidade_decifrada = ''.join(decifrado(c) for c in quantidade_cifrada)
            preco_decifrado = ''.join(decifrado(c) for c in preco_cifrado)
            print(f"ID: {id_produto}, Nome: {nome}, Quantidade: {quantidade_decifrada}, Preço: {preco_decifrado}, Importado: {'Sim' if dados[3] else 'Não'}")
            
def atualizar_produto(inventario):
    id_produto = input("Digite o ID do produto a ser atualizado: ").strip()
    if id_produto in inventario:
        nome = input(f"Digite o novo nome (atual: {inventario[id_produto][0]}): ")
        quantidade = input(f"Digite a nova quantidade (atual: {inventario[id_produto][1]}): ").strip()
        preco = input(f"Digite o novo preço (atual: {inventario[id_produto][2]}): ").strip()
        quantidade_cifrada = ''.join(cifrado(c) for c in quantidade)
        preco_cifrado = ''.join(cifrado(c) for c in preco)
        importado = input(f"O produto é importado? (atual: {'sim' if inventario[id_produto][3] else 'não'}): ").strip().lower() == "sim"
        inventario[id_produto] = [nome, quantidade_cifrada, preco_cifrado, importado]
        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

        
def cifrado(caractere):
    chave = 3  # Valor fixo para a chave

    # Se o caractere for um número (0-9), mapeia para uma letra (0 -> 'a', 1 -> 'b', ..., 9 -> 'j')
    if '0' <= caractere <= '9':  
        numero = int(caractere)
        novo_caractere = chr((numero + chave) % 10 + ord('a'))  # Desloca e mapeia para letras de 'a' a 'j'
    
    # Se o caractere for uma letra minúscula (a-z)
    elif 'a' <= caractere <= 'z':  
        novo_caractere = chr(((ord(caractere) - ord('a') + chave) % 26) + ord('a'))

    # Se o caractere for uma letra maiúscula (A-Z)
    elif 'A' <= caractere <= 'Z':  
        novo_caractere = chr(((ord(caractere) - ord('A') + chave) % 26) + ord('A'))
    
    else:
        novo_caractere = caractere  # Não cifrar outros caracteres (ex: pontuação, espaços, etc.)

    return novo_caractere

# Função para decifrar os caracteres
def decifrado(caractere):
    chave = 3  # Valor fixo para a chave

    # Se o caractere for uma letra de 'a' a 'j', converte de volta para um número (a -> 0, b -> 1, ..., j -> 9)
    if 'a' <= caractere <= 'j':  
        numero = ord(caractere) - ord('a')
        novo_caractere = str((numero - chave) % 10)  # Deslocamento reverso e retorna ao número

    # Se o caractere for uma letra minúscula (a-z)
    elif 'a' <= caractere <= 'z':  
        novo_caractere = chr(((ord(caractere) - ord('a') - chave) % 26) + ord('a'))

    # Se o caractere for uma letra maiúscula (A-Z)
    elif 'A' <= caractere <= 'Z':  
        novo_caractere = chr(((ord(caractere) - ord('A') - chave) % 26) + ord('A'))
    
    else:
        novo_caractere = caractere  

    return novo_caractere
  
def bubble_sort(d):
    items = list(d.items())  # Converte o dicionário em uma lista de tuplas
    fim = len(items)
    while fim > 0:
        i = 0
        while i < fim - 1:
            # Comparando os preços dos produtos (acessados via items[i][1][1])
            if items[i][1][1] > items[i + 1][1][1]:
                temp = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temp
            i += 1
        fim -= 1
    # Retorna o dicionário ordenado
    return dict(items)

# O selection sempre está interessado em descobrir quem é o menor elemento da vez
def selection_sort(d):
    items = list(d.items())
    
    i = 0
    while i < len(items) - 1:
        menor = i
        j = i + 1
        while j < len(items):           
            if items[j][1][1] < items[menor][1][1]:  # Comparando os preços
                menor = j
            j += 1
        if menor != i:
            temp = items[i]
            items[i] = items[menor]
            items[menor] = temp
        i += 1
    # Retorna os itens ordenados
    return dict(items)

def ordenar_inventario(inventario, tipo='bubble'):
    # Decifra os preços para preparar os dados para ordenação
    lista_produtos = {
        id_produto: (dados[0], float(''.join(decifrado(c) for c in dados[2])))
        for id_produto, dados in inventario.items()
    }
    
    # Escolha do algoritmo de ordenação
    if len(lista_produtos) > 100:
        merge_sort(lista_produtos, 0, len(lista_produtos) - 1)
        print("\nInventário ordenado por preço (Merge Sort):")
    else:
        if tipo == 'bubble':
            lista_produtos = bubble_sort(lista_produtos)  # Ordena com Bubble Sort
            print("\nInventário ordenado por preço (Bubble Sort):")
        elif tipo == 'selection':
            lista_produtos = selection_sort(lista_produtos)  # Aplica a ordenação por Selection Sort
            print("\nInventário ordenado por preço (Selection Sort):")
    
    # Limpa o inventário original e insere os itens na nova ordem
    inventario.clear()
    for id_produto, (nome, preco) in lista_produtos.items():
        # Converte o preço de volta para o formato cifrado
        preco_cifrado = ''.jo  in(cifrado(c) for c in f"{preco:.2f}")
        inventario[id_produto] = [nome, 0, preco_cifrado, False]
    
    # Exibe o inventário ordenado com os preços cifrados
    for id_produto, dados in inventario.items():
        print(f"ID: {id_produto}, Nome: {dados[0]}, Preço: {dados[2]}")

        
def exibir_inventario(inventario):
    if not inventario:
        print("Inventário vazio.")
    else:
        for id_produto, dados in inventario.items():
            print(f"ID: {id_produto}, Nome: {dados[0]}, Quantidade: {dados[1]}, Preço: {dados[2]}, Importado: {dados[3]}")

# Função para intercalação (Merge Sort)
def intercala(L, inicio, meio, fim):
    T = (fim - inicio + 1) * [0]
    i, j, k = inicio, meio + 1, 0
    while i <= meio and j <= fim:
        if L[i][2] < L[j][2]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = L[j]
            j += 1
        k += 1
    while i <= meio:
        T[k] = L[i]
        i += 1
        k += 1
    while j <= fim:
        T[k] = L[j]
        j += 1
        k += 1
    for i in range(0, len(T)):
        L[inicio + i] = T[i]

# Função para Merge Sort
def merge_sort(L, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        merge_sort(L, inicio, meio)
        merge_sort(L, meio + 1, fim)
        intercala(L, inicio, meio, fim)

# Função para buscar produto por ID
def buscar_produto_id(inventario):
    id_produto = input("Digite o ID do produto a ser buscado: ").strip()
    if id_produto in inventario:
        dados = inventario[id_produto]
        print(f"Produto encontrado: ID: {id_produto}, Nome: {dados[0]}, Quantidade: {dados[1]}, Preço: {dados[2]}, Importado: {dados[3]}")
    else:
        print("Produto não encontrado.")

# Função para buscar produto por nome
def buscar_produto_nome(inventario):
    nome_produto = input("Digite o nome do produto a ser buscado: ").strip().lower()
    encontrados = [(id_produto, dados) for id_produto, dados in inventario.items() if nome_produto in dados[0].lower()]
    if encontrados:
        for produto in encontrados:
            id_produto, dados = produto
            print(f"Produto encontrado: ID: {id_produto}, Nome: {dados[0]}, Quantidade: {dados[1]}, Preço: {dados[2]}, Importado: {dados[3]}")
    else:
        print("Produto não encontrado.")

# Função para atualizar login e senha
def atualizar_login():
    print("\nVocê não pode alterar o login diretamente. Para mudar o login, será necessário criar um novo usuário.")
    print("Você pode alterar a senha, caso deseje.")
    senha = input("Digite a nova senha: ")
    hash_senha = criar_hash_senha(senha)
    with open('login.txt', 'r+') as f:
        conteudo = f.readlines()
        conteudo[1] = hash_senha + '\n'  # Atualiza a senha
        f.seek(0)
        f.writelines(conteudo)
    print("Senha atualizada com sucesso!")

# Função principal
def main():
    usuario, hash_senha_armazenada = verificar_login()
    if usuario is None:
        return  # Se o login falhar, encerra o programa
    inventario = {}
    while True:
        print("\nMenu de opções:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Atualizar produto")
        print("4. Exibir inventário")
        print("5. Ordenar inventário")
        print("6. Buscar produto por ID")
        print("7. Buscar produto por nome")
        print("8. Atualizar senha")
        print("9. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            adicionar_produto(inventario)
        elif opcao == '2':
            remover_produto(inventario)
        elif opcao == '3':
            atualizar_produto(inventario)
        elif opcao == '4':
            exibir_inventario(inventario)
        elif opcao == '5':
            tipo_ordem = input("Escolha o tipo de ordenação (bubble/selection): ").strip()
            ordenar_inventario(inventario, tipo_ordem)
        elif opcao == '6':
            buscar_produto_id(inventario)
        elif opcao == '7':
            buscar_produto_nome(inventario)
        elif opcao == '8':
            atualizar_login()
        elif opcao == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
