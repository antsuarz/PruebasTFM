import pandas as pd
from scipy.stats import linregress
 
df = pd.read_csv("dataset-cleaned.txt", sep=";", decimal=",")
 
au_cols = [col for col in df.columns if col.startswith("AU")]
q_cols = [col for col in df.columns if col.startswith("q")]

resultados = []
count = 0
for q in q_cols:
    for au in au_cols:
        datos = df[[q, au]].dropna()
        x = datos[q]
        y = datos[au]

        res = linregress(x, y)

        resultados.append({
            "Pregunta(X)": q,
            "AU(Y)": au,
            "a": round(res.intercept, 4),
            "b": round(res.slope, 4),
            "t": round(res.slope / res.stderr, 4),
            "p": round(res.pvalue, 6),
        }) 
        
tabla_regresiones = pd.DataFrame(resultados)
tabla_regresiones.to_csv("tabla_regresiones_dataset.csv", index=False)