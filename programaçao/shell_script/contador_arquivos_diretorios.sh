#!/bin/bash

# Desenvolver um script Bash que solicite ao usuário o caminho de um diretório.
# Primeiro, o script deve validar se o diretório informado existe.
# Se for um diretório válido, ele procederá para contar quantos arquivos
# e quantos subdiretórios ele contém.
# Ao final, o script exibirá o total de arquivos e diretórios encontrados dentro do caminho especificado.

echo "Diretório: "; read DIR

if [ -d "$DIR" ]; then
        echo "Válido!"
else
        echo "Inválido!"
fi
arq=0
diret=0
for item in $"$DIR"/*; do
        if [ -f $item ]; then
                arq=$((arq + 1))
        elif [ -d $item ]; then
                diret=$((diret + 1))
        fi
done
echo "Possui $arq arquivos e $diret diretórios..."
Close
