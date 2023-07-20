import utils
import pandas

#TODO - do comtando, precisamos ajustar esse caso: — Felizes as pessoas que choram,
#pois Deus as consolará.  DICA É POR CONTA SPLIT NO INICIO DO CÓDIGO \N




baseUrl = "https://www.biblegateway.com/passage/?"

#PRECISAMOS FAZER UM FOR PARA CADA ESTILO OU VERSÃO
version      = "VFL"


#velho testamento
for k, v in utils.dictOldBooksVFL.items():

    for chapter in range(v):
        url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
        print(k, v)

input()
#novo testamento
for k, v in utils.dicNewBookVFL.items():

    for chapter in range(v):
        url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
        print(k, v)




versicles = utils.crawlSite(url, chapter)

print(versicles)



"""
for book in utils.velhoTestamento:

    for chapter in montar uma sublista para cada livro https://www.respostas.com.br/capitulos-da-biblia/

"""





#padrao = r'\d+\s(.+?)(?=\d+\s|\Z)'

#versiculos = re.findall(padrao, verses, re.DOTALL)
#print(versiculos)

#input()
#print(len(versiculos[2:-1]))
#versiculos = versiculos[2:-1]
#print(versiculos)




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

