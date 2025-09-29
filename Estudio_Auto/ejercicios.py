import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('spotify-2023.csv', encoding='latin-1')
print(df.info())

# A
categoricas = df.select_dtypes(include=['object']).shape[1]
numericas = df.select_dtypes(include=['number']).shape[1]

print(f"Variables categóricas: {categoricas}")
print(f"Variables numéricas: {numericas}")

# B
contador = 0

datos1 = df[['artist(s)_name', 'track_name']]
for i in range(len(datos1)):
    artista = datos1['artist(s)_name'][i]
    
    
    if 'Coldplay' in str(artista):
        contador = contador + 1

print(f"Hay {contador} canciones de Coldplay")

# C
    
# D
columnas_numericas = ['artist_count', 'released_year', 'released_month', 'released_day', 'in_spotify_playlists']

for columna in columnas_numericas:
    maximo = df[columna].max()
    minimo = df[columna].min()
    
    print(f"{columna}:")
    print(f"MÁXIMO = {maximo}")
    print(f"MÍNIMO = {minimo}")
        