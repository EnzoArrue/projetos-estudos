#!/bin/bash

# Desenvolver um script Bash que conte o número de linhas em um arquivo especificado pelo usuário.
# O script solicitará o caminho absoluto do diretório e o nome do arquivo separadamente.
# Ele fará a validação tanto do diretório quanto do arquivo, garantindo que ambos existam e sejam válidos.
# Após a validação, o script utilizará uma função para realizar a contagem das linhas
# e exibir o resultado ao usuário.

echo -e "\t*Insira o nome de um arquivo que deseja contar as linhas*"
echo -e "\nDigite o caminho absoluto do diretório do arquivo:\n"
read DIR
while [ ! -d "$DIR" ]; do
        echo -e "\nDiretório inválido! Digite:"
        read DIR
        if [ -d "$DIR" ]; then
                echo -e "\nDiretório válido!"
        fi
done
echo -e "\nDigite o nome coreto do arquivo que deseja:\n"
read ARQ
while [ ! -f "$DIR"/"$ARQ" ]; do
        echo -e "\nInválido. Digite outro:"
        read ARQ
        if [ -f "$DIR" ]; then
                echo -e "\nArquivo válido!"
        fi
done
function main() {
        CONT=$(cat "$DIR"/"$ARQ" | wc -l)
        echo "Linhas: $CONT"
}
main
