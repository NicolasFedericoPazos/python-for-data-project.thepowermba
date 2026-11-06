import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

df = pd.read_csv("data/processed/dataset_final.csv", parse_dates=["date", "Dt_Customer"])


df["y_bin"] = (df["y"] == "yes").astype(int)

cols_num = ["age", "duration", "campaign", "pdays", "previous",
            "Income", "NumWebVisitsMonth", "euribor3m"]
print("=== Resumen de variables numéricas ===")
print(df[cols_num].describe().round(2))

print("\n=== ¿Cuántos clientes suscriben? ===")
print(df["y"].value_counts(normalize=True).round(3))


def tasa(col):
    t = df.groupby(col)["y_bin"].agg(clientes="count", tasa_suscripcion="mean")
    t["tasa_suscripcion"] = (t["tasa_suscripcion"] * 100).round(1)
    return t.sort_values("tasa_suscripcion", ascending=False)

categorias = ["job", "education", "marital", "contact", "poutcome",
              "previously_contacted", "contact_month", "contact_year",
              "housing", "loan", "Kidhome", "Teenhome"]
for col in categorias:
    print(f"\n=== Tasa de suscripción por {col} ===")
    print(tasa(col))


df["tramo_edad"] = pd.cut(df["age"].astype(float), bins=[0, 25, 35, 45, 55, 65, 100])
df["tramo_income"] = pd.qcut(df["Income"], 4)
for col in ["tramo_edad", "tramo_income"]:
    print(f"\n=== Tasa de suscripción por {col} ===")
    print(tasa(col).sort_index())

print("\n=== Promedios: no vs. sí ===")
print(df.groupby("y")[cols_num].mean().round(2))


cols_corr = ["age", "duration", "campaign", "pdays", "previous",
             "emp.var.rate", "cons.price.idx", "cons.conf.idx",
             "euribor3m", "nr.employed", "Income", "Kidhome",
             "Teenhome", "NumWebVisitsMonth", "y_bin"]
print("\n=== Correlación con y_bin ===")
print(df[cols_corr].astype(float).corr()["y_bin"].drop("y_bin").round(3).sort_values())