
#Se supone que utilizaré estas librerías para realizar la prueba.

import pandas as pd
import matplotlib.pyplot as plt
import sys
import requests



#Acceso a los datos utilizando la API, el código 200 indica que la respuesta a la solicitud ha sido exitosa
response = requests.get("https://api.datos.observatoriologistico.cl/api/v2/datastreams/TEST-12708/data.json/?auth_key=c93b6780c0f163e2ccf1a947c04656be05d97360&limit=12100")
print(response.status_code)


#Visualización de data.json
response.json()


#Ejercicio para comprender estructura de datos
for key in response.json():
    print(key)


#Datos "interesantes" encontrados
key1 = response.json()["result"]
for key in key1:
    print(key)


#Observaciones
key1["fArray"]


#Observación de la matriz de datos
print(key1["fCols"])
print(key1["fRows"])


