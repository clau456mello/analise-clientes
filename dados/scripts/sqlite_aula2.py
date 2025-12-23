import sqlite3
conn = sqlite3.connect("dados.db")
cursor = conn.cursor()
cursor.execute(""" 
INSERT INTO clientes (nome, idade, cidade)
VALUES ('Ana', 28, 'Lisboa')   
""")
cursor.execute("""
INSERT INTO clientes (nome, idade, cidade)
VALUES ('João', 35, 'Porto')
""")
cursor.execute("""
INSERT INTO clientes (nome, idade, cidade)
VALUES ('Maria', 22, 'Coimbra')                             
""")
conn.commit()
conn.close()
print ("Dados inseridos com sucesso")                              