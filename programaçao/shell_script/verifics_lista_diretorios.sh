#!/bin/bash

# Desenvolver um script Bash que solicite ao usuário o caminho absoluto de um diretório.
# O script deve então verificar se o diretório existe e não está vazio.
# Se o diretório for válido, ele exibirá uma mensagem de confirmação e aguardará a interação do usuário
# antes de listar detalhadamente o conteúdo do diretório.
# Caso o diretório não seja encontrado, uma mensagem de erro será exibida.

clear
echo "Digite um caminho absoluto de um diretório:"
read DIR
if [ -d "$DIR" ]; then
        echo -e "\nO diretório realmente existe e não está vázio! Clique em <ENTER> para listar os arquivos do diretório...\n"
        read
        ls -l "$DIR"
        echo -e "\nConcluído com sucesso!"
else
        echo "Diretório não encontrado. Pressione <ENTER>"
        read
fi
