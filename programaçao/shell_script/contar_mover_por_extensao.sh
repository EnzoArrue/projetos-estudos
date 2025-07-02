#!/bin/bash

# Desenvolver um script Bash que permite ao usuário especificar uma extensão de arquivo.
# O script deve então contar quantos arquivos com essa extensão existem no diretório atual.
# Após a contagem, o script deve perguntar ao usuário um diretório de destino e mover
# todos os arquivos com a extensão especificada para esse novo diretório, informando
# cada arquivo que foi movido.

echo -e "Qual extensão deseja contar e copiar a partir do diretório atual: \n"; read EXT
dir=$(pwd)
result=$(ls "$dir"/*."$EXT" | wc -l)
echo -e "Total de linhas com essa extensão: $result\n"
echo -e "Digite a pasta que quer repassar os arquivos: \n"; read diret
for arquivo in "$dir"/*."$EXT"; do
        mv "$arquivo" "$diret"
        echo -e "\nArquivo "$arquivo" movido para a pasta de antes!\n"
done
