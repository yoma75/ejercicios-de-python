import pandas as pd
import webbrowser  # modulo para paginas web

website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'  # ruta
webbrowser.open(website)  # .open, abre la pagina

# leer desde el porta papeles, seleccionar y copiar
dataFrame_nba = pd.read_clipboard()

