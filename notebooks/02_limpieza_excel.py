import pandas as pd

hojas = pd.read_excel("data/raw/customer-details.xlsx", sheet_name=None)

df_customers = pd.concat(
    [hoja.assign(sheet_year=int(nombre)) for nombre, hoja in hojas.items()],
    ignore_index=True,
)
df_customers = df_customers.drop(columns="Unnamed: 0")

print(df_customers.shape)
print("IDs duplicados:", df_customers["ID"].duplicated().sum())
print("Filas totalmente duplicadas:", df_customers.duplicated().sum())
print(df_customers.describe())


df_customers.to_csv("data/processed/customers_clean.csv", index=False)
print("Guardado en data/processed/customers_clean.csv")

