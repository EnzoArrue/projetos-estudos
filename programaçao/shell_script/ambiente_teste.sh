#!/bin/bash

# Desenvolver um script Bash que prepare um ambiente de teste no diretório home do usuário 'kali'.
# O script criará um novo diretório chamado 'teste_simbolos' dentro de 'scripts_shell'.
# Em seguida, ele navegará para este novo diretório e criará quatro arquivos de texto vazios:
# 'arq1.txt', 'arq2.txt', 'arq3.txt' e 'arq4.txt'.
# Após a criação, o script listará esses arquivos de duas maneiras diferentes para demonstrar padrões de nomes.
# Finalmente, ele adicionará uma mensagem inicial ao 'arq1.txt' e, em seguida, uma segunda linha
# com outra mensagem, mostrando como concatenar texto em um arquivo.

mkdir /home/kali/scripts_shell/teste_simbolos
cd /home/kali/scripts_shell/teste_simbolos
touch arq1.txt arq2.txt arq3.txt arq4.txt
ls -l *.txt
ls -l arq?.txt
mensagem="Shell Script teste"
echo "Mensagem: $mensagem" > /home/kali/scripts_shell/teste_simbolos/arq1.txt
echo "Olá mundo!!!" >> /home/kali/scripts_shell/teste_simbolos/arq1.txt
