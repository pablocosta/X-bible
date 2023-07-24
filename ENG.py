import utils
import polars
import tqdm

#TO-DO olhar cada um dos capitulos e remover aqui dentro

baseUrl = "https://www.biblegateway.com/passage/?"


"""
    #PRECISAMOS FAZER UM FOR PARA CADA ESTILO OU VERSÃO
    version      = "KJ21"

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
    for k, v in tqdm.tqdm(utils.dictEnglishOld.items()):
        
        for chapter in range(1, v+1):
            url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
            print(url)
            dicionarioUnidade = utils.crawlSiteEng(url)
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
        

    polars.concat(listDf).write_csv("./data/ENG/KJ21Old.tsv", separator="\t")

    print("Novo Testamento: ")
    #novo testamento
    listDf = []
    versiculos = []
    textos     = []
    estilo     = []
    capitulo   = []
    livro      = []
    for k, v in tqdm.tqdm(utils.dicEnglishNew.items()):
        
        for chapter in range(1, v+1):
            url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
            print(url)
            dicionarioUnidade = utils.crawlSiteEng(url)
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

    polars.concat(listDf).write_csv("./data/ENG/KJ21New.tsv", separator="\t")



    #PRECISAMOS FAZER UM FOR PARA CADA ESTILO OU VERSÃO
    version      = "ASV"

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
    for k, v in tqdm.tqdm(utils.dictEnglishOld.items()):
        
        for chapter in range(1, v+1):
            url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
            print(url)
            dicionarioUnidade = utils.crawlSiteEng(url)
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
        

    polars.concat(listDf).write_csv("./data/ENG/ASVOld.tsv", separator="\t")

    print("Novo Testamento: ")
    #novo testamento
    listDf = []
    versiculos = []
    textos     = []
    estilo     = []
    capitulo   = []
    livro      = []
    for k, v in tqdm.tqdm(utils.dicEnglishNew.items()):
        
        for chapter in range(1, v+1):
            url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
            print(url)
            dicionarioUnidade = utils.crawlSiteEng(url)
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

    polars.concat(listDf).write_csv("./data/ENG/ASVNew.tsv", separator="\t")
"""


#PRECISAMOS FAZER UM FOR PARA CADA ESTILO OU VERSÃO "AMP", "AMPC", "BRG", "CSB", "CEB", "CJB", "CEV", "DARBY", 
# "DLNT", "DRA", "ERV", "EHV", "ESV", "ESVUK", "EXB", "GNV", "KJV", "AKJV", "LSB", "LEB", "TLB", "MOUNCE", "NABRE", "NASB", "NASB1995", "NCB", "NCV", "NIRV", "NIVUK", "NKJV", "YLT"

for version in ["YLT"]:

    #version      = "ASV"

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
    for k, v in tqdm.tqdm(utils.dictEnglishOld.items()):
        
        for chapter in range(1, v+1):
            url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
            print(url)
            dicionarioUnidade = utils.crawlSiteEng(url)
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
        

    polars.concat(listDf).write_csv("./data/ENG/"+version+"Old.tsv", separator="\t")

    print("Novo Testamento: ")
    #novo testamento
    listDf = []
    versiculos = []
    textos     = []
    estilo     = []
    capitulo   = []
    livro      = []
    for k, v in tqdm.tqdm(utils.dicEnglishNew.items()):
        
        for chapter in range(1, v+1):
            url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
            print(url)
            dicionarioUnidade = utils.crawlSiteEng(url)
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

    polars.concat(listDf).write_csv("./data/ENG/"+version+"New.tsv", separator="\t")