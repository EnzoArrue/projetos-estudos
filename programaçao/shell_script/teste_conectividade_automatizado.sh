#!/bin/bash

# Desenvolver um script Bash que realize um teste de conectividade (ping) em um intervalo de endereços IP.
# O script definirá uma sub-rede padrão (192.168.15) e solicitará ao usuário o primeiro e o último octeto
# do intervalo de IPs a serem testados.
# Para cada IP no intervalo, o script tentará um ping rápido (um pacote, tempo limite de 1 segundo).
# Os resultados detalhados do ping serão salvos em um arquivo de log chamado 'arquivoLog.txt'.
# Além disso, o script exibirá no terminal se cada máquina (IP) respondeu ('OK') ou não ('NÃO OK').
# Ao final do processo, uma mensagem de "FIM" será exibida.

echo -e "Insira um intervalo de IPs para ser testado...\n"
REDE="192.168.15"
echo -ne "\n\tDigite IP1: "; read IP1
echo -ne "\n\tDigite IP2: "; read IP2
touch arquivoLog.txt
while [ $IP1 -le $IP2 ]; do
        ping $REDE.$IP1 -w 1 -c 1 >> arquivoLog.txt #-w 1 espera 1seg e -c 1 apenas um pacote
        if [ $? -eq 0 ]; then #$? retorna o valor do último comando, 0 = sucesso
                echo -ne "\n\tMaq-$IP1 - OK"
        else
                echo -ne "\n\tMaq-$IP1 - NÃO OK"
        fi
        IP1=$((IP1 + 1))
done
echo -ne "\n\t F I M\n"
