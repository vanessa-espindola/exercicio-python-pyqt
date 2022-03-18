# -*- coding: utf-8 -*-

def abrir_exibir_arquivo(nome_arq):
    '''
        abertura do arquivo txt e 
        exibição do seu conteúdo.
    '''
    with open(nome_arq, encoding="utf-8") as f:
        dados = list(f)
    return dados
# abrir_exibir_arquivo("meu_arquivo.txt")

def salvar_inserir_dados_em_arquivo(nome_arq, todos_os_dados_lista):
    '''
        uma função para salvamento dos dados 
        inseridos em um arquivo.txt
    '''
    arquivo = open(nome_arq, 'w+', encoding="utf-8")  
    for dado_da_vez in todos_os_dados_lista:
        arquivo.write(dado_da_vez)
        arquivo.write("\n")
# salvar_inserir_dados_em_arquivo('meu_arquivo.txt', lista)
