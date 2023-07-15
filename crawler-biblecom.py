import trafilatura
import requests
import re
import nltk
from nltk import tokenize

###############################esse funciona
bible = "200/"
base_url = "https://www.bible.com/bible/"
search_query = "MAT.2"
version = ".VFL"
url = base_url + bible + search_query + version

response = requests.get(url)
html_content = response.text

verses = trafilatura.extract(html_content, include_images=False, include_formatting=False)


palavras_tokenize = tokenize.word_tokenize(verses, language='portuguese')
print(palavras_tokenize)


#padrao = r'\d+\s(.+?)(?=\d+\s|\Z)'

#versiculos = re.findall(padrao, verses, re.DOTALL)

#print(len(versiculos[2:-1]))
#versiculos = versiculos[2:-1]
#print(versiculos[-1])
# A expressão regular encontra o número do versículo seguido por um espaço e captura o texto do versículo até encontrar o próximo número de versículo ou o fim do texto.



