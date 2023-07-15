import trafilatura
import requests
from nltk import tokenize
###############################esse funciona
base_url = "https://www.biblegateway.com/passage/?"
search_query = "Mateus%201"
version = "ARC"
url = base_url + "search=" + search_query + "&version=" + version

response = requests.get(url)
html_content = response.text

verses = trafilatura.extract(html_content, include_images=False, include_formatting=False)
palavras_tokenize = tokenize.word_tokenize(verses, language='portuguese')

import re


padrao = r"\d+(\D+)"

matches = re.findall(padrao, " ".join(palavras_tokenize))
print(matches)





precisamos remover o inicio e o fim
#padrao = r'\d+\s(.+?)(?=\d+\s|\Z)'

#versiculos = re.findall(padrao, verses, re.DOTALL)

#print(len(versiculos[2:-1]))
#versiculos = versiculos[2:-1]
#print(versiculos[-1])
# A expressão regular encontra o número do versículo seguido por um espaço e captura o texto do versículo até encontrar o próximo número de versículo ou o fim do texto.

#padrao = r'(\d+)\s(.*?)\n'

#resultados = re.findall(padrao, verses, re.DOTALL)

#dicionario_versiculos = {versiculo: texto.strip() for versiculo, texto in resultados}

#print(dicionario_versiculos["18"]) #ainda existem sub versiculos no texto

#input()
