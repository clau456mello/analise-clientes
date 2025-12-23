import sqlite3
import pandas as pd
conn= sqlite3.connect("dados.db")
df = pd.read_sql_query("SELECT * FROM clientes" , conn)
conn.close()
print("\n--- DATAFRAME COMPLETO ---")
print(df)
print("\n---MÉDIA DE IDADE POR CIDADE ---")
media_idade = df.groupby("cidade") ["idade"].mean()
print(media_idade)