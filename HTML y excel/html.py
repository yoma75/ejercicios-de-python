# Html con python, recuperar datos de una pagina web

import pandas as pd

url = 'https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'

dataframe = pd.io.html.read_html(url)
print(dataframe)

# CONTINUACIÓN EN GOOGLE DRIVE  yomacolor42


