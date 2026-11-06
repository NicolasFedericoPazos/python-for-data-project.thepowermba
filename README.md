# python-for-data-project.thepowermba
# Análisis exploratorio de campañas de marketing bancario

## Objetivo

[Explica en 2 o 3 frases qué analizas y para qué. Por ejemplo: qué quieres
descubrir sobre los clientes que suscriben el depósito a plazo.]

## Datos

- `bank-additional.csv`: 43.000 contactos de campañas de marketing directo
  de un banco portugués, con datos del cliente, de la llamada y del contexto
  económico.
- `customer-details.xlsx`: datos demográficos de los clientes (ingresos,
  hijos, visitas web), en 3 hojas según el año de alta (2012, 2013 y 2014).

## Estructura del repositorio

​```
data/
  raw/          datos originales sin modificar
  processed/    datos limpios y dataset final
notebooks/      scripts de Python, en orden de ejecución
images/         gráficos generados
requirements.txt
README.md
​```

## Cómo ejecutarlo

1. Instalar las dependencias: `pip install -r requirements.txt`
2. Ejecutar desde la raíz del proyecto, en este orden:

​```
python notebooks/02_limpieza_excel.py
python notebooks/03_limpieza_csv.py
python notebooks/04_union_datasets.py
python notebooks/05_analisis_descriptivo.py
python notebooks/06_visualizacion.py
​```

(`01_carga_exploracion.py` es solo la exploración inicial.)

## Pasos seguidos

1. **Exploración inicial:** Ver de que se trataban los datos.
2. **Limpieza del Excel:** se unieron las 3 hojas en una tabla (43.170
   clientes), se eliminó una columna de índice sobrante y se comprobó que no
   había duplicados ni nulos.
3. **Limpieza del CSV:**
   - Se convirtieron a número las columnas con coma decimal.
   - Se unificó el texto a minúsculas.
   - Se convirtió la fecha (texto en español) a fecha real y se crearon
     `contact_month` y `contact_year`.
   - Nulos de texto (`job`, `marital`, `education`): se rellenaron con `unknown`.
   - Nulos de `age`, `default`, `housing` y `loan`: se dejaron sin rellenar
     para no distorsionar las distribuciones y que no afecte a un futuro calculo.
   - `cons.price.idx` y `euribor3m`: se rellenaron con el valor de su grupo
     económico.
   - `pdays = 999`  se pasó a nulo y se creó
     `previously_contacted`.
4. **Unión:** se unió el CSV con el Excel por el identificador del cliente,
   conservando las 43.000 filas del CSV.
5. **Análisis descriptivo:** estadísticos, tasa de suscripción por grupos
   y correlaciones.
6. **Visualización:** 9 gráficos con matplotlib y seaborn.


## Herramientas

Python, pandas, matplotlib, seaborn, Visual Studio Code.