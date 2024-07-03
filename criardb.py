# Importando sqlite

import sqlite3 as lite

# criando conexao

con = lite.connect('dados.db')

# criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE inventory(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, location TEXT, description TEXT, "
                "brand TEXT, purchase_date DATE, prize DECIMAL, serie TEXT, image TEXT)")
