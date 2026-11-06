import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_theme(style="whitegrid")
Path("images").mkdir(exist_ok=True)

df = pd.read_csv("data/processed/dataset_final.csv", parse_dates=["date", "Dt_Customer"])
df["y_bin"] = (df["y"] == "yes").astype(int)


def guardar(nombre):
    plt.tight_layout()
    plt.savefig(f"images/{nombre}.png", dpi=150)
    plt.close()

#Cuántos clientes suscriben? (desbalance de la variable objetivo)
fig, ax = plt.subplots(figsize=(5, 4))
sns.countplot(data=df, x="y", ax=ax, hue="y", legend=False)
ax.set_title("Clientes que suscriben el depósito")
ax.set_xlabel("¿Suscribe?")
ax.set_ylabel("Clientes")
guardar("01_distribucion_y")

#Qué profesiones suscriben más?
tasa_job = (df.groupby("job")["y_bin"].mean() * 100).sort_values()
fig, ax = plt.subplots(figsize=(8, 5))
tasa_job.plot(kind="barh", ax=ax)
ax.axvline(df["y_bin"].mean() * 100, color="red", linestyle="--", label="Media global")
ax.set_title("Tasa de suscripción por profesión")
ax.set_xlabel("% que suscribe")
ax.legend()
guardar("02_tasa_por_profesion")

#Y por edad?
df["tramo_edad"] = pd.cut(
    df["age"].astype(float),
    bins=[0, 25, 35, 45, 55, 65, 100],
    labels=["≤25", "26-35", "36-45", "46-55", "56-65", ">65"],
)
tasa_edad = df.groupby("tramo_edad", observed=True)["y_bin"].mean() * 100
fig, ax = plt.subplots(figsize=(7, 4))
tasa_edad.plot(kind="bar", ax=ax, rot=0)
ax.set_title("Tasa de suscripción por tramo de edad")
ax.set_xlabel("Edad")
ax.set_ylabel("% que suscribe")
guardar("03_tasa_por_edad")

#Influye el resultado de la campaña anterior?
tasa_pout = df.groupby("poutcome")["y_bin"].mean() * 100
fig, ax = plt.subplots(figsize=(6, 4))
tasa_pout.plot(kind="bar", ax=ax, rot=0)
ax.set_title("Tasa de suscripción según la campaña anterior")
ax.set_xlabel("Resultado de la campaña anterior")
ax.set_ylabel("% que suscribe")
guardar("04_tasa_por_campana_anterior")

#Qué canal de contacto funciona mejor?
tasa_contact = df.groupby("contact")["y_bin"].mean() * 100
fig, ax = plt.subplots(figsize=(5, 4))
tasa_contact.plot(kind="bar", ax=ax, rot=0)
ax.set_title("Tasa de suscripción por canal de contacto")
ax.set_xlabel("Canal")
ax.set_ylabel("% que suscribe")
guardar("05_tasa_por_canal")

#Las llamadas largas terminan más en suscripción?
#Se excluyen las llamadas de más de 1500 s para que los extremos no aplasten el gráfico.
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(data=df[df["duration"] < 1500], x="y", y="duration", ax=ax, hue="y", legend=False)
ax.set_title("Duración de la llamada según suscripción")
ax.set_xlabel("¿Suscribe?")
ax.set_ylabel("Duración (segundos)")
guardar("06_duracion_por_y")

#Matriz de correlaciones
cols_corr = ["age", "duration", "campaign", "previous", "emp.var.rate",
             "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed",
             "Income", "NumWebVisitsMonth", "y_bin"]
fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(df[cols_corr].astype(float).corr(), annot=True, fmt=".2f",
            cmap="coolwarm", center=0, ax=ax)
ax.set_title("Matriz de correlaciones")
guardar("07_correlaciones")

#Cómo se distribuyen las edades?
fig, ax = plt.subplots(figsize=(7, 4))
sns.histplot(data=df, x="age", bins=30, ax=ax)
ax.set_title("Distribución de la edad (clientes con edad conocida)")
ax.set_xlabel("Edad")
ax.set_ylabel("Clientes")
guardar("08_distribucion_edad")

#Hay estacionalidad por mes?
fig, ax = plt.subplots(figsize=(7, 4))
sns.barplot(data=df, x="contact_month", y="y_bin", ax=ax, errorbar=None)
ax.set_title("Tasa de suscripción por mes de contacto")
ax.set_xlabel("Mes")
ax.set_ylabel("Proporción que suscribe")
guardar("09_tasa_por_mes")

print("Gráficos guardados en la carpeta images/")