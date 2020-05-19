import sqlite3

sql = '''
create table if not exists conta(id integer primary key autoincrement,\
modelo text, quantidade integer, preco real,marca text unique(modelo))
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
        lista.append((input('MODELO:').upper()))
        lista.append(int(input('QUANTIDADE:')))
        lista.append(float(input('PREÇO:')))
        cursor.executemany("INSERT INTO conta(modelo, quantidade, preco)VALUES(?,?,?)" \
                           , [(lista)])
        conn.commit()
        conn.close()
    except:
        print('ERROR!!!')
        conn.close()


def adicionar():
    print('===========================')
    print('||   ADICIONAR PLACAS     ||')
    print('===========================')
    conn = sqlite3.connect("Banco.db");
    cursor = conn.cursor()
    lista.append((input('MODELO:').upper()))
    lista.append(int(input('QUANTIDADE:')))
    lista.append(float(input('PREÇO:')))
    p = cursor.execute('select * from conta where modelo=?', [(lista[0])])
    if p.fetchone()!=None:
        cursor.execute('UPDATE  conta set quantidade = quantidade +? where modelo =?', (lista[1], lista[0]))
        cursor.execute('UPDATE  conta set preco=? where modelo =?', (lista[2], lista[0]))
        conn.commit()
        print(f'\n{lista[1]} PLACA MODELO {lista[0]} FOI ADICIONADA AO ESTOQUE! ')
        conn.close()
    else:
        print(f'NÃO NEM UMA PLACA MODELO {lista[0]} EM ESTOQUE !!!')
        op = input('GOSTARIA DE CADASTRALA ?\nS)sim\nN)Não\n\n:').upper()
        if op=='S':
            cursor.executemany("INSERT INTO conta(modelo, quantidade, preco)VALUES(?,?,?)" \
                               , [(lista)])
            conn.commit()
            print(f'\n{lista[1]} PLACA MODELO {lista[0]} FOI ADICIONADA AO ESTOQUE! ')
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
                       (lista[1], lista[0]))
        cursor.execute('UPDATE  conta set preco=? where modelo =?', (lista[2], lista[0]))
        conn.commit()
        cursor.execute('delete from conta where quantidade =0')
        conn.commit()
        conn.close()
    except:
        print(f'\nNÃO TEMOS A PLACA {lista[0]} EM ESTOQUE! :(')


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
    conn = sqlite3.connect("Banco.db");
    cursor = conn.cursor()
    cursor.execute('select * from conta')
    for i in cursor.fetchall():
        print("-"*30)
        print(i)
    conn.close()
