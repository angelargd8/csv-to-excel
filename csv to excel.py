#pip install openpyxl

import pandas as pd

archivo = pd.read_csv('data.csv',encoding='utf-8')
df = pd.DataFrame(archivo)

GFG = pd.ExcelWriter('data.xlsx', engine='openpyxl')
df.to_excel(GFG, index=False)
GFG.close()
