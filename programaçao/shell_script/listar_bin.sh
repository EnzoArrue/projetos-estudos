#!/bin/bash

# Desenvolver um script Bash que liste, um por um, todos os arquivos e diretórios
# contidos dentro do diretório padrão /bin do sistema.
# O script deve pausar e aguardar a interação do usuário no início e no fim de sua execução.
# Cada elemento do diretório /bin será exibido com uma mensagem indicando sua exibição.

echo "Pressione <ENTER> para continuar..."
read
for ELEMENTO in $(ls /bin); do
        echo -e "Seguinte diretório/arquivo do \n$ELEMENTO\n"
done
echo "Pressione <ENTER> para finalizar..."
read
