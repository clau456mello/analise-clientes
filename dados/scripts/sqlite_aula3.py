import sqlite3
conn = sqlite3.connect("dados.db")
cursor = conn.cursor()
print("\n--- TODOS OS CLIENTES --")
cursor.execute ("SELECT * FROM clientes")
for linha in cursor.fetchall():
    print(linha)
print("\n--- CLIENTES COM IDADE>= 30 ---") 
cursor.execute("SELECT nome, idade FROM clientes WHERE idade >=30")
for linha in cursor.fetchall():
    print(linha) 
print("\n--- QUANTIDADE DE CLIENTES POR CIDADE ---") 
cursor.execute("""
SELECT cidade, COUNT(*)
FROM clientes
GROUP BY cidade
""")
for linha in cursor.fetchall():
    print(linha) 
conn.close()               