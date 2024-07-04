# Importando sqlite
import sqlite3 as lite

# criando conexao
con = lite.connect('dados.db')


def inserir_form(i):
    # Inserir dados
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventory(name, location, description, brand, purchase_date, prize, serie, image) VALUES(?,?,?, ?,?,?,?,?)"
        # execute precisa de onde/como vai ser inserido os dados e a lista que contenha os dados a serem inseridos
        cur.execute(query, i)


def update_form(i):
    # Atualizar dados
    with con:
        cur = con.cursor()
        query = ("Update inventory SET name=?, location=?, description=?, brand=?, purchase_date=?, prize=?, serie=?, image=? "
                 "WHERE id=?")
        cur.execute(query, i)


def delete_form(i):
    # Deletar dados
    with con:
        cur = con.cursor()
        query = "DELETE FROM INVENTORY WHERE id=?"
        cur.execute(query, i)


# View data
def view_form():
    view_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventory"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            view_dados.append(row)

    return view_dados


# View Individual data
def view_individual_form(id):
    view_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventory WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            view_dados_individual.append(row)