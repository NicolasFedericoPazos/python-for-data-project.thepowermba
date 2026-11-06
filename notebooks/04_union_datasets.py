import pandas as pd

df_bank = pd.read_csv("data/processed/bank_clean.csv", parse_dates=["date"])
df_customers = pd.read_csv(
    "data/processed/customers_clean.csv", parse_dates=["Dt_Customer"]
)

df = df_bank.merge(
    df_customers,
    how="left",
    left_on="id_",
    right_on="ID",
    validate="one_to_one",
)


df = df.drop(columns=["ID", "sheet_year"])


print("Forma final:", df.shape)
print("Nulos en las columnas del Excel:")
print(df[["Income", "Kidhome", "Teenhome", "Dt_Customer", "NumWebVisitsMonth"]].isna().sum())
print("IDs duplicados:", df["id_"].duplicated().sum())

# 5. Guardar el dataset final
df.to_csv("data/processed/dataset_final.csv", index=False)
print("Guardado en data/processed/dataset_final.csv")