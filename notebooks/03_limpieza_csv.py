import pandas as pd

df = pd.read_csv("data/raw/bank-additional.csv")


# Quitar la columna basura
df = df.drop(columns="Unnamed: 0")


cols_coma = ["cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]
for col in cols_coma:
    df[col] = pd.to_numeric(df[col].str.replace(",", "."), errors="coerce")

# Unificar el formato del texto: "MARRIED" y "married" 
df["marital"] = df["marital"].str.lower()
df["poutcome"] = df["poutcome"].str.lower()


# pandas no entiende los meses en español, traducimos el mes con un diccionario.
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12,
}
partes = df["date"].str.split("-", expand=True)
df["date"] = pd.to_datetime(
    {
        "year": partes[2].astype(float),
        "month": partes[1].map(meses),
        "day": partes[0].astype(float),
    },
    errors="coerce",
)

# creamos contact_month y contact_year para poder agrupar por mes y año 
df["contact_month"] = df["date"].dt.month.astype("Int64")
df["contact_year"] = df["date"].dt.year.astype("Int64")

for col in ["job", "marital", "education"]:
    df[col] = df[col].fillna("unknown")

df["age"] = df["age"].astype("Int64")
for col in ["default", "housing", "loan"]:
    df[col] = df[col].astype("Int64")


claves = ["emp.var.rate", "nr.employed", "cons.conf.idx"]
df["cons.price.idx"] = df["cons.price.idx"].fillna(
    df.groupby(claves)["cons.price.idx"].transform("median")
)
df["euribor3m"] = df["euribor3m"].fillna(
    df.groupby(claves + ["cons.price.idx"])["euribor3m"].transform("median")
)


# cambiamos el 999 para que no se confunda con un valor real. Lo hago nulo
df["previously_contacted"] = (df["pdays"] != 999).astype(int)
df["pdays"] = df["pdays"].where(df["pdays"] != 999)


print("Filas duplicadas:", df.duplicated().sum())
print("IDs duplicados:", df["id_"].duplicated().sum())
print("\nNulos que quedan:")
print(df.isna().sum()[df.isna().sum() > 0])
print("\nRango de fechas:", df["date"].min(), "->", df["date"].max())
df.info()

df.to_csv("data/processed/bank_clean.csv", index=False)
print("\nGuardado en data/processed/bank_clean.csv")

