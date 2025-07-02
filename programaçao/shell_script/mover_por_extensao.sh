#!/bin/bash

# Crie um script que solicite ao usuário uma extensão de arquivo e conte quantos arquivos com essa extensão existem no diretório atual.
# Em seguida, peça um nome de diretório, crie esse diretório, e mova todos os arquivos com a extensão informada para ele.
# Após cada movimentação, exiba uma mensagem de sucesso. 

echo -e "Qual extensão deseja contar e copiar a partir do diretório atual: \n"; read EXT
dir=$(pwd)
result=$(ls "$dir"/*."$EXT" | wc -l)
echo -e "Total de linhas com essa extensão: $result\n"
echo -e "Digite um nome de diretório para mover os arquivos: \n"; read nome
mkdir "$dir"/"$nome"
for arquivo in "$dir"/*."$EXT"; do
        mv "$arquivo" "$dir"/"$nome"
        echo -e "Movido com sucesso!\n"
done
