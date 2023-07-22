import utils
import polars
import tqdm
import sys


baseUrl = "https://www.biblegateway.com/passage/?"

#PRECISAMOS FAZER UM FOR PARA CADA ESTILO OU VERSÃO
version      = "OL"

#url = baseUrl + "search=" + "Mateus" + "%20" + "5" + "&version=" + version
#versicles = utils.crawlSite(url, 1)

print("Velho Testamento: ")
#velho testamento
listDf = []
versiculos = []
textos     = []
estilo     = []
capitulo   = []
livro      = []
for k, v in tqdm.tqdm(utils.dictOldBookOL.items()):
    
    for chapter in range(1, v+1):
        url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
        print(url)
        dicionarioUnidade = utils.crawlSite(url)
        versiculos.extend([k for k,_ in dicionarioUnidade.items()])
        textos.extend([v for _,v in dicionarioUnidade.items()])

        estilo.extend([version] * len(versiculos))
        capitulo.extend([chapter] * len(versiculos))
        livro.extend([k] * len(versiculos))
        
        listDf.append(polars.from_dict(utils.toDict(estilo=estilo, livro=livro, capitulo=capitulo, versiculos=versiculos, textos=textos)))
        versiculos = []
        textos     = []
        estilo     = []
        capitulo   = []
        livro      = []
    

polars.concat(listDf).write_parquet("./data/OLOld.parquet")

print("Novo Testamento: ")
#novo testamento
listDf = []
versiculos = []
textos     = []
estilo     = []
capitulo   = []
livro      = []
for k, v in tqdm.tqdm(utils.dicNewBookOL.items()):
    
    for chapter in range(1, v+1):
        url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
        print(url)
        dicionarioUnidade = utils.crawlSite(url)
        versiculos.extend([k for k,_ in dicionarioUnidade.items()])
        textos.extend([v for _,v in dicionarioUnidade.items()])

        estilo.extend([version] * len(versiculos))
        capitulo.extend([chapter] * len(versiculos))
        livro.extend([k] * len(versiculos))
        
        listDf.append(polars.from_dict(utils.toDict(estilo=estilo, livro=livro, capitulo=capitulo, versiculos=versiculos, textos=textos)))
        versiculos = []
        textos     = []
        estilo     = []
        capitulo   = []
        livro      = []

polars.concat(listDf).write_parquet("./data/OLNew.parquet")