import sqlite3

sql = '''
create table if not exists conta(id integer primary key autoincrement,
marca text,modelo text, quantidade integer, preco real, unique(modelo))
'''


def criarTabela():
    conn = sqlite3.connect("Banco.db");
    cursor = conn.cursor()
    cursor.execute(sql);


lista = []
check = []


def cadastrar():
    print('===========================')
    print('||    CADASTRAR PLACAS   ||')
    print('===========================')
    conn = sqlite3.connect("Banco.db");
    cursor = conn.cursor()
    try:
        lista.append(input('MARCA:').strip(' ').upper())
        lista.append((input('MODELO:').strip(' ').upper()))
        lista.append(int(input('QUANTIDADE:')))
        lista.append(float(input('PREÇO:')))
        cursor.executemany("INSERT INTO conta(marca, modelo, quantidade, preco)VALUES(?,?,?,?)" \
                           , [(lista)])
        conn.commit()
        conn.close()
    except ValueError:
        print(ValueError)
        conn.close()


def adicionar():
    print('===========================')
    print('||   ADICIONAR PLACAS     ||')
    print('===========================')
    conn = sqlite3.connect("Banco.db");
    cursor = conn.cursor()
    lista.append(input('MARCA:').strip(' ').upper())
    lista.append((input('MODELO:').strip(' ').upper()))
    lista.append(int(input('QUANTIDADE:')))
    lista.append(float(input('PREÇO:')))
    p = cursor.execute('select * from conta where modelo=?', [(lista[1])])
    if p.fetchone()!=None:
        cursor.execute('UPDATE  conta set quantidade = quantidade +? where modelo =?', (lista[2], lista[1]))
        cursor.execute('UPDATE  conta set preco=? where modelo =?', (lista[3], lista[1]))
        conn.commit()
        print(f'\n{lista[2]} PLACA MARCA {lista[0]}  MODELO {lista[1]} FOI ADICIONADA AO ESTOQUE! ')
        conn.close()
    else:
        print(f'NÃO NEM UMA PLACA MODELO {lista[1]} EM ESTOQUE !!!')
        op = input('GOSTARIA DE CADASTRALA ?\nS)sim\nN)Não\n\n:').upper()
        if op=='S':
            cursor.executemany("INSERT INTO conta(marca, modelo, quantidade, preco)VALUES(?,?,?,?)" \
                               , [(lista)])
            conn.commit()
            print(f'\n{lista[2]} PLACA MARCA {lista[0]}  MODELO {lista[1]} FOI ADICIONADA AO ESTOQUE! ')
            conn.close()
        elif op=='n':
            pass


def vender():
    print('===========================')
    print('||     VENDER PLACA      ||')
    print('===========================')
    conn = sqlite3.connect("Banco.db");
    cursor = conn.cursor()
    lista.append((input('MODELO:').upper()))
    lista.append(int(input('QUANTIDADE:')))
    try:
        cursor.execute('UPDATE  conta set quantidade = quantidade -? where quantidade >0 and modelo =?',
                       (lista[2], lista[1]))
        cursor.execute('UPDATE  conta set preco=? where modelo =?', (lista[3], lista[1]))
        conn.commit()
        cursor.execute('delete from conta where quantidade =0')
        conn.commit()
        conn.close()
    except:
        print(f'\nNÃO TEMOS A PLACA MARCA {lista[0]} E MODELO {lista[1]} EM ESTOQUE! :(')


def pesquisarMod():
    print('===========================')
    print('     PESQUISAR PLACA       ')
    print('===========================')
    conn = sqlite3.connect("Banco.db");
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM conta WHERE modelo=?""", [input('MODELO:')])
    print(' Id   ,MD,   Qt    ,Valor')
    print('=' * 30)
    for i in cursor.fetchall():
        print(i);
    conn.close()
def estoque():
    print("""
=======================================
| LISTA DE TODAS AS PLACAS EM ESTOQUE |
=======================================
    """)
    conn = sqlite3.connect("Banco.db");
    cursor = conn.cursor()
    cursor.execute('select * from conta')
    for i in cursor.fetchall():
        print("-"*50)
        print(i)
    conn.close()

def findMarca():
    print("""
==============================
| BUSCA DE PLACAS POR MARCA  |
==============================\n

    """)
    m=input("DIGITE A MARCA :").strip(' ').upper()
    conn = sqlite3.connect("Banco.db");
    cursor = conn.cursor()
    cursor.execute('select * from conta where marca=?',[m])
    for i in cursor.fetchall():
        print("-" * 50)
        print(i)
    conn.close()
def findMod():
    print("""
==============================
| BUSCA DE PLACAS POR MARCA  |
==============================\n

    """)
    m=input("DIGITE A MODELO :").strip(' ').upper()
    conn = sqlite3.connect("Banco.db");
    cursor = conn.cursor()
    cursor.execute('select * from conta where modelo=?',[m])
    for i in cursor.fetchall():
        print("-" * 50)
        print(i)
    conn.close()
