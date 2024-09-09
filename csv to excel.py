import pandas as pd

archivo = pd.read_csv('data.csv')
df = pd.DataFrame(archivo)

GFG = pd.ExcelWriter('data.xlsx')
df.to_excel(GFG, index=False)
GFG.save()
