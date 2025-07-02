#!/bin/bash

# Desenvolver um script Bash que conte o número de linhas de um arquivo.
# O script solicitará o nome do diretório e o nome do arquivo separadamente.
# Ele implementará um loop de validação robusto que continuará pedindo ao usuário
# um diretório e um arquivo válidos até que um caminho de arquivo existente seja fornecido.
# Uma vez que um arquivo válido é identificado, o script exibirá o total de linhas.

function linhas(){
        echo "Escreva o nome do diretório pelo qual contenha o arquivo que deseja trabalhar"
        read DIR
        echo -e "\nEscreva o nome do arquivo:\n"
        read ARQ
        while [ ! -f "$DIR"/"$ARQ" ]; do
                echo -e "\nInválido, digite um diretorio e um arquivo\n"
                echo "Digite um diretório:"
                read DIR
                echo -e "\nDigite um arquivo válido:"
                read ARQ
        done
        for linha in "$DIR"/"$ARQ"; do
                cat "$linha" | wc -l # Corrigido: 'cat' precisa do nome do arquivo
        done
}
linhas
