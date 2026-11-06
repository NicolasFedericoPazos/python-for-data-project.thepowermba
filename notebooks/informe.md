# Informe de análisis: campañas de marketing de un banco portugués

## 1. Contexto y datos

Se analizaron 43.000 contactos telefónicos de campañas de marketing directo
para la venta de un depósito a plazo, combinando el archivo de la campaña
(`bank-additional.csv`) con datos demográficos de los clientes
(`customer-details.xlsx`). Tras la limpieza, el dataset final tiene
43.000 filas y 31 columnas.

## 2. Hallazgo principal: la suscripción es poco frecuente

Solo suscribe el 11,3 % de los clientes contactados (gráfico 1). La
variable está muy desbalanceada, así que cualquier segmento que supere
con claridad ese 11,3 % merece atención.

## 3. Qué diferencia a quienes suscriben

Los clientes cuya campaña anterior fue un éxito suscriben un 65,3 %,
frente a un 14,2 % de los que tuvieron un fracaso y un 8,8 % de los que
nunca fueron contactados (gráfico 4). Es una señal muy fuerte, pero se
apoya en un grupo pequeño: solo 1.588 clientes (el 3,7 %) tienen contacto
previo.

**El canal importa.**
El contacto por `celular` convierte un 14,7 % y el teléfono
fijo un **5,2 %** (gráfico 5). Además, el móvil ya es el
canal del 64 % de los contactos.

**Hay perfiles más receptivos.**
Por profesión destacan los estudiantes 31,3 % y los jubilados
25,2 %, mientras que los trabajadores manuales `blue-collar` quedan
últimos con un 6,9 % (gráfico 2). Por edad aparece una forma de U
(gráfico 3): suscriben más los menores de 25 años 20,9 % y, sobre todo,
los mayores de 65 46,0 %, mientras que la franja de 36 a 55 años queda en
torno al 8,6 %. Los solteros suscriben más 13,9 % que los casados y
divorciados 10,2 %, y quienes tienen estudios universitarios (13,7 %)
más que quienes llegaron hasta la educación básica (entre 7,8 % y 8,1 %).

**El contexto económico acompaña.**
Las variables macroeconómicas son las que más se relacionan con la
suscripción (gráfico 7): `nr.employed` (-0,36), `euribor3m` (-0,31) y
`emp.var.rate` (-0,30). Quienes suscriben lo hicieron con un euríbor
medio de 2,11 frente a 3,81 de quienes no. Es decir, se suscribe más
cuando los tipos de interés están bajos. Esto describe una asociación y
no prueba causalidad.



## 6. Que recomiendo hacer a continuacion? 

1. Priorizar a los clientes con una campaña anterior exitosa.
2. Contactar por móvil en lugar de teléfono fijo.
3. Diseñar mensajes específicos para jubilados, mayores de 65, estudiantes
   y menores de 25, que son los más receptivos.
4. No insistir con más llamadas a un mismo cliente: no mejora la
   suscripción. (la correlación con el número de contactos es ligeramente
  negativa (-0,07). Quienes suscriben recibieron de media 2,05 contactos,
  frente a 2,63 de quienes no.)


