

# importar la librería Requests que sirve para enviar consultas HTTP
import requests
import pandas as pd
# api-endpoint
endpoint = "https://api.openaq.org/v1/locations"
parameters = "?country=CL"
URL = endpoint+parameters

r = requests.get(url = URL)

# extracting data in json format
data = r.json()
chile_df = pd.DataFrame(data['results'])
#Mostramos los 10 primeros resultados
chile_df[0:10] #equivalente a: valdivia_df.head(10)

print(chile_df[0:10])
