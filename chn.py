import utils
import polars
import tqdm

#TO-DO olhar cada um dos capitulos e remover aqui dentro

baseUrl = "https://www.biblegateway.com/passage/?"


#PRECISAMOS FAZER UM FOR PARA CADA ESTILO OU VERSÃO "LBLA", "JBS" "DHH", "NBLA", "NBV", "NTV", "NVI", "CST", "PDT", "BLP", "BLPH", "RVA-2015", "RVC", "RVR1690", "RVR1995",

for version in ["CCB", "CCBT", "ERV-ZH", "CNVS", "CNVT", "CSBS", "CSBT", "CUVS", "CUV", "CUVMPS", "CUVMPT", "RCU17SS", "RCU17TS"]:

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
    for k, v in tqdm.tqdm(utils.dictChineseOld.items()):
        
        for chapter in range(1, v+1):
            url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
            print(url)
            dicionarioUnidade = utils.crawlSiteChn(url)
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
        

    polars.concat(listDf).write_csv("./data/CHN/"+version+"Old.tsv", separator="\t")

    print("Novo Testamento: ")
    #novo testamento
    listDf = []
    versiculos = []
    textos     = []
    estilo     = []
    capitulo   = []
    livro      = []
    for k, v in tqdm.tqdm(utils.dicChineseNew.items()):
        
        for chapter in range(1, v+1):
            url = baseUrl + "search=" + k + "%20" + str(chapter) + "&version=" + version
            print(url)
            dicionarioUnidade = utils.crawlSiteChn(url)
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

    polars.concat(listDf).write_csv("./data/CHN/"+version+"New.tsv", separator="\t")