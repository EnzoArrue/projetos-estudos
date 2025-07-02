
Enzo Arrue
Início
Sobre
Projetos
Certificados
Contato
Enzo Arrue
Portfólio de Enzo Arrue
Segurança da Informação | Ethical Hacking

Segurança da Informação
Ethical Hacking
Power BI
Programação
Excel
Laboratórios
SIEM
Estudos Teóricos
Ver Projetos
Entrar em Contato
Sobre Mim
Formação
Desde cedo, a tecnologia despertou em mim mais do que interesse, despertou um propósito. Atualmente curso Segurança da Informação pela FATEC (conclusão em 2026), uma área que escolhi por refletir meus valores e meu compromisso com a ética, especialmente no cuidado e responsabilidade ao lidar com dados sensíveis.

Propósito
Este portfólio foi criado como um espaço profissional, refletindo minha jornada contínua de aprendizado. Aqui registro projetos, experimentos e descobertas que marcaram minha trajetória em busca de conhecimento, sempre com o propósito de desenvolver soluções tecnológicas para os desafios do mundo real.

Áreas de Interesse
Segurança da Informação
Análise de vulnerabilidades, ethical hacking e proteção de sistemas

Programação
Python, Shell Script e desenvolvimento de automações

Inteligência Artificial
Machine Learning, IBM Watson e desenvolvimento de chatbots

Business Intelligence
Power BI, análise de dados e criação de dashboards

Análise de Dados
Excel avançado, SQL e visualização de informações

Estudos Teóricos
Pesquisa, relatórios técnicos e documentação

Ferramentas & Tecnologias
Python
GNU Bash
VS Code
MetaMask
Linux
IBM Watson Studio
Kali Linux
IBM Watson Assistant
Excel
Word
PowerPoint
Power BI
SQL
Cisco Packet Tracer
IDLE
Nmap
Canva
MacOS
Windows
Projetos
Explore meus projetos organizados por área de especialização. Cada pasta contém trabalhos práticos e estudos aplicados.

Projeto Estudos - Repositório GitHub


Segurança da Informação
Projetos relacionados à segurança cibernética e análise de vulnerabilidades


Criptografia

Programação - Cybersecurity
Criptografia
Projeto de Gerenciamento
Sistema de Prevenção de Intrusão - SSH
Teste de Conectividade Automatizado

Laboratório Adm. de Sistemas Operacionais de Redes

Protocolo, Roteamento e Endereçamento em Redes

Programação
Scripts, aplicações e automações desenvolvidas


Python

Shell Script
Verificador de Arquivo
Mover por Extensão
Contar e Mover Extensão
Verifica Idade
Contador Progressivo
Contador de Usuários e Grupo - Linux
Calculadora Bash
Verificar e Listar Diretório
Listar /BIN
Teste de Conectividade Automatizado
Contador de Arquivos e Diretórios
Menu de Informações do Sistema
Contador de Linhas de Arquivos
Contador de Linhas com Validação Reforçada
Organizador de Arquivos em Diretórios
Listagem Simples
Relação de Números
Contador De Users e Grupos - Simplificado - Linux
Ambiente Teste

Excel
Planilhas avançadas e análises de dados


Power BI
Dashboards e relatórios interativos


IA / Prompts
Projetos de inteligência artificial e prompt engineering


Relatórios de Estudo
Documentação e relatórios de pesquisa com laboratórios práticos


Ver no GitHub
Certificados
Minha jornada de aprendizado documentada através de certificações e cursos especializados

Segurança da Informação
Em andamento - Conclusão 2026
Segurança da Informação
FATEC

Graduação em Segurança da Informação com foco em proteção de sistemas e análise de vulnerabilidades.


Ver Certificado
AI Fundamentals
Concluído
AI Fundamentals
IBM

Fundamentos de Inteligência Artificial, Machine Learning e aplicações práticas.


Ver Certificado
AI with Capstone Project
Concluído
AI with Capstone Project
IBM

Projeto prático aplicando conceitos de IA em soluções reais de negócio.


Ver Certificado
Ciência da Computação Python
Concluído
Ciência da Computação Python
USP-IME

Programação em Python com foco em algoritmos e estruturas de dados.


Ver Certificado
Networking Basics
Concluído
Networking Basics
CISCO

Fundamentos de redes de computadores e protocolos de comunicação.


Ver Certificado
Introdução à Cibersegurança
Concluído
Introdução à Cibersegurança
CISCO

Conceitos básicos de segurança cibernética e proteção de dados.


Ver Certificado
Endereçamento IPv4
Concluído
Endereçamento IPv4
Curso em Vídeo

Configuração e gerenciamento de endereços IP versão 4.


Ver Certificado
Networking Devices and Initial Configuration
Concluído
Networking Devices and Initial Configuration
CISCO

Configuração inicial de dispositivos de rede e troubleshooting.


Ver Certificado
Excel Básico
Concluído
Excel Básico
SENAI-SP

Fundamentos do Microsoft Excel para análise e organização de dados.


Ver Certificado
Vamos Conversar
Estou sempre aberto a discussões sobre segurança da informação, colaborações em projetos e oportunidades de aprendizado.

Informações de Contato
Email

enzoarruejuanfuso@gmail.com

Telefone

(11) 94576-2844

Redes Sociais
LinkedIn

Enzo Arrue

GitHub

EnzoArrue

Instagram

@ez.arrue_

Interessado em colaborar?
Seja para discutir projetos, compartilhar conhecimento ou explorar oportunidades, estou sempre disponível para uma conversa produtiva.

Enviar Email
Conectar no LinkedIn
© Enzo Arrue Juan Fuso

Portfólio em constante evolução - Última atualização: Junho 2025

Contador de Arquivos e Diretórios - Script Shell Script
Visualização do código fonte do script selecionado

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
