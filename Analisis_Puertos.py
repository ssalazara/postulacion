
# coding: utf-8

# In[2]:


#Explicitando que no supe elaborar el DF desde data.json, presento el analisis que hubiese realizado(exportando un csv desde API)

#Librerías a utilizar

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[11]:


#carga de datos desde archivo exportado (csv)
filepath = '/home/haze/Documentos/Programa/puertos_chile.csv'
df = pd.read_csv(filepath, sep =',', thousands = '.', header = 0, error_bad_lines = False, encoding = 'ISO-8859-1')


# In[14]:


#Visualización de datos
df.head()


# In[20]:


cols = df.columns.values


# In[16]:


#Los errores de escritura en los titulos se debe al uso de tildes ''' y letra 'ñ'
print(cols)


# In[24]:


#Distribución del tonelaje movilizado por regiones
df.groupby('REGIÃ\x93N')['TONELADAS'].sum().sort_values().plot.barh()


# In[30]:


#Tonelaje movilizado por año
df.groupby('AÃ\x91O')['TONELADAS'].sum().plot.bar()


# In[36]:


#Distribución porcentual de carga movilizada por tipo de carga
df.groupby('TIPO_CARGA')['TONELADAS'].sum().sort_values().plot.pie(autopct = '%.2f')


# In[46]:


#Medidas de tendencia central del tonelaje movilizado
ton = df['TONELADAS'].describe()
print(ton)


# In[57]:


#Correlación estandar coeficiente pearson
df.corr(method = 'pearson')

