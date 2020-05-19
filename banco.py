import sqlite3 

conn = sqlite3.connect("Banco.db");
cursor = conn.cursor()

sql ='''
create table if not exists conta(id integer primary key autoincrement,\
modelo text, quantidade integer, preco real, unique(modelo))
'''
def criarTabela():
    cursor.execute(sql);
lista=[]
check=[]
def cadastrar():
    try:
        lista.append((input('MODELO:').upper()))
        lista.append(int(input('QUANTIDADE:')))
        lista.append(float(input('PREÇO:')))
        cursor.executemany("INSERT INTO conta(modelo, quantidade, preco)VALUES(?,?,?)" \
                               , [(lista)])
        conn.commit()
    except:
        print('ERROR!!!')

def adicionar():
    lista.append((input('MODELO:').upper()))
    lista.append(int(input('QUANTIDADE:')))
    lista.append(float(input('PREÇO:')))
    cursor.execute('UPDATE  conta set quantidade = quantidade +? where modelo =?', (lista[1], lista[0]))
    cursor.execute('UPDATE  conta set preco=? where modelo =?', (lista[2], lista[0]))
    conn.commit()
def vender():
    lista.append((input('MODELO:').upper()))
    lista.append(int(input('QUANTIDADE:')))
    cursor.execute('UPDATE  conta set quantidade = quantidade -? where quantidade >0 and modelo =?', (lista[1], lista[0]))
    cursor.execute('UPDATE  conta set preco=? where modelo =?', (lista[2], lista[0]))
    conn.commit()
    cursor.execute('delete from conta where quantidade =0')
    conn.commit()

def pesquisarMod():
    cursor.execute("""SELECT * FROM conta WHERE modelo=?""",[input('MODELO:')])
    print(' Id   ,MD,   Qt    ,Valor')
    print('='*30)
    for i in cursor.fetchall():
        print(i);



