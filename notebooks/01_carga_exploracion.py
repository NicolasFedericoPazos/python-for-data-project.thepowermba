import pandas as pd

# Para que pandas muestre todas las columnas al imprimir
pd.set_option("display.max_columns", None)

# Carga del CSV
df_bank = pd.read_csv("data/raw/bank-additional.csv")

# Carga del Excel
hojas = pd.read_excel("data/raw/customer-details.xlsx", sheet_name=None)

# Para ver el csv
print("=== CSV ===")
print(df_bank.shape)
print(df_bank.head())
df_bank.info()

# Primer vistazo a cada hoja del Excel
print("\n=== EXCEL ===")
print(hojas.keys())
for nombre, hoja in hojas.items():
    print(f"\nHoja {nombre}: {hoja.shape}")
    print(hoja.head())