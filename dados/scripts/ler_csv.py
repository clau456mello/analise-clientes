import pandas as pd

# Ler arquivo CSV
df = pd.read_csv("clientes.csv")

print("\n--- DADOS DO CSV ---")
print(df)

print("\n--- IDADE MÉDIA ---")
print(df["idade"].mean())

print("\n--- QUANTIDADE POR CIDADE ---")
print(df["cidade"].value_counts())
