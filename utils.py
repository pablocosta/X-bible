import trafilatura
import requests
import re
from nltk import tokenize


dictOldBooksVFL = {"Gênesis": 50,
"Êxodo": 40,
"Levítico": 27,
"Números": 36,
"Deuteronômio": 34,
"Josué": 24,
"Juízes": 21,
"Rute": 4,
"1%20Samuel": 31,
"2%20Samuel": 24,
"1%20Reis": 22,
"2%20Reis": 25,
"1%20Crônicas": 29,
"2%20Crônicas": 36,
"Esdras": 10,
"Neemias": 13,
"Ester": 10,
"Jó": 42,
"Salmos": 150,
"Provérbios": 31,
"Eclesiastes": 12,
"Cânticos": 8,
"Isaías": 66,
"Jeremias": 52,
"Lamentações": 5,
"Ezequiel": 48,
"Daniel": 12,
"Oseias": 14,
"Joel": 3,
"Amós": 9,
"Obadias": 1,
"Jonas": 4,
"Miqueias": 7,
"Naum": 3,
"Habacuque": 3,
"Sofonias": 3,
"Ageu": 2,
"Zacarias":14,
"Malaquias": 4}


dicNewBookVFL = {"Mateus": 28,
"Marcos": 16,
"Lucas": 24,
"João": 21,
"Atos": 26,
"Romanos": 16,
"1%20Coríntios": 16,
"2%20Coríntios": 13,
"Gálatas": 6,
"Efésios": 6,
"Filipenses": 4,
"Colossenses": 4,
"1%20Tessalonicenses": 5,
"2%20Tessalonicenses": 3,
"1%20Timóteo": 6,
"2%20Timóteo": 4,
"Tito": 3,
"Filemom": 1,
"Hebreus": 13,
"Tiago": 5,
"1%20Pedro": 5,
"2%20Pedro": 3,
"1%20João": 5,
"2%20João": 1,
"3%20João": 1,
"Judas": 1,
"Apocalipse": 22}


def crawlSite(url: str, chapter: str):
    versiculos = {}
    response = requests.get(url)
    htmlContent = response.text
    verses = trafilatura.extract(htmlContent, include_images=False, include_formatting=False)
    #print(getAllSentencesBetweenHifen(verses))
    text = verses.split("\n")
    
    

    # pega os principais versículos
     
    check = 0
    # procura por versículos que estejam dentro de versículos
    for s in text:
        str0 = s.split(" ")[0]
        if str0.isnumeric():
            #True    
            #is first time
            if check == 0:
                check = 1
                #tem sub versiculos?
                #faszer quebra por numeros
                
                #contains other versicles at the same string?
                if len(re.findall('[0-9]+', s)) > 1:
                    print("aqui")
                    print(getAllSubVersicles(s))
                    for subVersicle in getAllSubVersicles(s):
                        subVersicle = tokenize.word_tokenize(subVersicle, language='portuguese')
                        tail = subVersicle[1:]
                        head = subVersicle[0]
                        if head == chapter:
                            versiculos["1"] = " ".join(tail)
                        else:
                            versiculos[head] = " ".join(tail)
                    input(versiculos)

            else:
                #is not first time
                #tem sub versiculos?
                #contains other versicles at the same string?
                if len(re.findall('[0-9]+', s)) > 1:
                    for subVersicle in getAllSubVersicles(s):
                        subVersicle = tokenize.word_tokenize(subVersicle, language='portuguese')
                        tail = subVersicle[1:]
                        head = subVersicle[0]
                        versiculos[head] = " ".join(tail)
                else:
                    versiculos[str0] = " ".join(s.split(" ")[1:])
    
    return versiculos

def getAllSubVersicles(text):
    sents = []
    sent = []
    isprimeiro = 0
    wholeString = tokenize.word_tokenize(text, language='portuguese')
    sizeString = len(wholeString)
    for word in range(sizeString):
        
        if wholeString[word].isnumeric() and isprimeiro==0:
            isprimeiro = 1
            sent.append(wholeString[word])
        elif wholeString[word].isnumeric() and isprimeiro==1:
            sents.append(" ".join(sent))
            sent = []
            sent.append(wholeString[word])
        elif word == len(wholeString)-1:
            sents.append(" ".join(sent))
            sent = []
        else:
            sent.append(wholeString[word])
    return sents





def getAllSentencesBetweenHifen(texts: str):
   
    
   for sent in tokenize.sent_tokenize(texts, language='portuguese'):
        str0 = sent.split(" ")[0]
        if str0.isnumeric():
            print("é numérico:  ", sent)
        else: 
            print("não é numérico:  ", sent)
        input()
   return "matches"

def processContent(content: list):
    padrao = r"\d+(\D+)"
    matchesVersiculos = re.findall(padrao, content)
    versos = matchesVersiculos[2:-1]
    print(len(versos))
    #secoes = re.findall('\d+', " ".join(content))[2:-1]
    return versos
