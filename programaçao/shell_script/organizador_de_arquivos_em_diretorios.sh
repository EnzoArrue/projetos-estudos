#!/bin/bash

# Desenvolver um script Bash que organize arquivos de um diretório especificado pelo usuário.
# O script primeiro verifica a existência do diretório informado. Se o diretório não existir,
# o script será encerrado. Se for válido, ele criará um subdiretório chamado 'exercicio' dentro dele.
# Em seguida, o script percorrerá todos os itens no diretório original e copiará apenas os arquivos
# (ignorando subdiretórios existentes) para a nova pasta 'exercicio', exibindo mensagens
# sobre o processo de criação da pasta e o movimento de cada arquivo. Ao final, uma mensagem
# de conclusão será exibida.

echo "DIR: "; read DIR

function verificadir() {
        if [ -d "$DIR" ]; then
                echo "Existe!"
        else
                echo "Inexistente!"
                exit
        fi
}

function pasta() {
        echo "Criando pasta"
}

function arquivo() {
        echo "Movendo o arquivo: $arq"
}

function mover_criardiret() {
        contador=1
        for arq in "$DIR"/*; do
                if [ -f "$arq" ]; then
                        pasta
                        mkdir -p "$DIR/exercicio"
                        arquivo "$contador"
                        cp "$arq" "$DIR/exercicio"
                        contador=$((contador + 1))
                fi
        done
        echo "Organização concluída!"
}

verificadir
mover_criardiret
