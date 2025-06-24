#Usamos dicionario quando queremos falar que tal coisa esta ligado a outra; em uma agenda por exemplo.
#Estrutura -> agenda = {chave : valor}; mais de um valor coloca em lista

def exibe(agenda):
    for contato in agenda.items():
        print(f"Nome: {contato[1][0]}")
        print(f"Telefone: {contato[1][1]}")
        print(f"Endereço: {contato[1][2]}")
        print('-' * 20)
          
agenda = {"ana" : [190,111,"Rua da ana"],
          "bia" : [191,222, "Rua da Bia"],
          "clara" : [192,333, "Rua da Clara"]}

exibe(agenda)

def exibe(agenda):
    for x in agenda.items():
        chave, valor = x
        print(f"Nome:", chave)
        fone, endereco = valor
        print(f"Telefone: {fone}")
        print(f"Endereço: {endereco}")
        print('-' * 20)
          

