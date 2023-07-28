# %%
#Importar pandas
import pandas as pd

#Operaciones numericas
import numpy as np

#Crear graficos
import matplotlib.pyplot as plt

# %%
estructura = {
    "nombres": ["Juan", "Pedro", "Luis", "Belen", "Mateo", "Andrea"],
    "correlativo": [1, 4, 9, 155, 152, 158],
    "altura": [3.1, 5.2, 4.8, 2.9, 4.3, 4.9]
}

# %%
df = pd.DataFrame(estructura)
df #No poner print para que se muestren como tabla 


# %%
df["nombres"] #acceder a la columna "nombres"

# %%
df.loc[3] #accedo al registro (fila) 3 del df



# %%
