import sqlite3
conn= sqlite3.connect("dados.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
nome TEXT, 
idade INTEGER,
cidade TEXT
)               
""")
conn.commit()
conn.close()
print("Tabela criada com sucesso")