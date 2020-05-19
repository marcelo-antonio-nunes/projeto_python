#--coding:utf-8 
from banco import *
import os, time,platform
def limpar():
    if platform.system()=='Linux':
        os.system('clear')
    else:
        os.system('cls')
criarTabela();

def menuBusca():
    print("""
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||CADASTRO E CONTROLE DE ENTRADA E SAIDA DE PLACAS EM ESTOQUE ||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
-----------------------OPÇÕES---------------------------------
C) -> BUSCA POR MARCA
M) -> BUSCA POR MODELO
    
        """)
    return input("DIGITE O MODO DE BUSCA :").upper()


def menu():
    print("""
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||CADASTRO E CONTROLE DE ENTRADA E SAIDA DE PLACAS EM ESTOQUE ||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
-----------------------OPÇÕES---------------------------------
C) -> CADASTRAR PLACA
A) -> ADICIONAR PLACA CADASTRADA
B) -> DAR BAIXA EM PLACA VENDIDA
F) -> MODO DE BUSCA
L) -> LISTAR TODAS AS PLACAS 
S) -> SAIR DO PROGRAMA
    """)
    return input('DIGITE SUA OPÇÃO :').upper()
op =None
while op!='S':
    limpar()
    op = menu()
    if op == 'C':
        limpar()
        cadastrar()
    elif op == 'A':
        limpar()
        adicionar()
    elif op == 'B':
        limpar()
        vender()
    elif op == 'L':
        limpar()
        estoque()
        input("\n\nENTER PRA RETORNAR AO MENU ")
    elif op == 'F':
        limpar()
        b = menuBusca()
        if b == 'C':
            limpar()
            findMarca()
        elif b == 'M':
            limpar()
            findMod()
        input("\n\nENTER PRA RETORNAR AO MENU ")
    elif op == 'S':
        break


