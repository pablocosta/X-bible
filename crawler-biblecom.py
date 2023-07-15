import trafilatura
import requests
import re
###############################esse funciona
https://www.bible.com/bible/2439/MAT.2.MIM
base_url = "https://www.biblegateway.com/passage/?"
search_query = "Mateus%201"
version = "ARC"
url = base_url + "search=" + search_query + "&version=" + version

response = requests.get(url)
html_content = response.text

verses = trafilatura.extract(html_content, include_images=False, include_formatting=False)






#padrao = r'\d+\s(.+?)(?=\d+\s|\Z)'

#versiculos = re.findall(padrao, verses, re.DOTALL)

#print(len(versiculos[2:-1]))
#versiculos = versiculos[2:-1]
#print(versiculos[-1])
# A expressão regular encontra o número do versículo seguido por um espaço e captura o texto do versículo até encontrar o próximo número de versículo ou o fim do texto.

padrao = r'(\d+)\s(.*?)\n'

resultados = re.findall(padrao, verses, re.DOTALL)

dicionario_versiculos = {versiculo: texto.strip() for versiculo, texto in resultados}

print(dicionario_versiculos["18"]) #ainda existem sub versiculos no texto

input()


