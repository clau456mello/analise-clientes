import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar ao banco SQLite
conn = sqlite3.connect("dados.db")

# Ler dados para o pandas
df = pd.read_sql_query("SELECT * FROM clientes", conn)
conn.close()

# Mostrar DataFrame
print(df)

# Estilo do seaborn
sns.set(style="whitegrid")

# Gráfico de barras - idade por pessoa
plt.figure(figsize=(6,4))
sns.barplot(x="nome", y="idade", data=df)
plt.title("Idade por Cliente")
plt.xlabel("Cliente")
plt.ylabel("Idade")

plt.show()
