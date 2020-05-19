import sqlite3 

conn = sqlite3.connect("Banco.db");
cursor = conn.cursor()

sql ='''
create table if not exists conta(id integer primary key autoincrement,\
modelo text, quantidade integer, preco real)
'''
def criarTabela():
    cursor.execute(sql);

def cadastrar():
    try:
        cursor.executemany("INSERT INTO conta(modelo, quantidade, preco)VALUES(?,?,?)"\
                           ,[(input('MODELO:'),int(input('QUANTIDADE:')),float(input('PREÇO:')))])

        conn.commit()
    except:
        print('ERROR!!!')

def atualizar():
    ...

def pesquisarMod():
    cursor.execute("""SELECT * FROM conta WHERE modelo=?""",[input('MODELO:')])
    print(' Id   ,MD,   Qt    ,Valor')
    print('='*30)
    for i in cursor.fetchall():
        print(i);



