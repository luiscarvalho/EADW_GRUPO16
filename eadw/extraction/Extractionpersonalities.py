
from search import Search
import nltk
import re

class Extraction:
    
    def __init__(self, ipath, ppath ):
        self.indexpath = ipath
        self.perslistpath = ppath

        

#s.allFeeds()

    

    def addPersonalities(self, persona, t, persl):
        dic= eval(open(self.perslistpath).read())
        personaList = persona.split()
        for pers in dic['listPersonalities']:
            #pattern1 = re.compile(persona)
            if (persona == pers and pers not in persl):
                #print "persona==pers"
                #print persona
                #print pers
                persl.append(pers)
            elif (len(personaList) == 2):
                if (personaList[0] in pers and personaList[1] in pers and pers not in persl):
                    persl.append(pers)
            elif (len(personaList) == 1):
                if (personaList[0] in pers.split() and pers not in persl):
                    persl.append(pers)
 
                    
    def seachPersonalities(self, query):
        s = Search.Searcher(self.indexpath)
        newslist = s.search(query)
                  
        #print newslist

        persDict = {}

        for l in newslist:
            titulo = l.split("::")[0]
            summary = l.split("::")[1]
            #wordList=nltk.word_tokenize(l)
            wordList=summary.split()
            #print wordList
            #print len(wordList)
            persList=[]
            i=0
            nome = ""
            xnome = ""
            while i < len(wordList):
                x=wordList[i]
                #print x  
                if x[0].isupper() and len(x) > 2:
                    if ',' in x:
                        n=x.split(',')
                        if nome == "":
                            nome = n[0]
                            #print nome
                            self.addPersonalities(nome, titulo, persList)
                            nome=""
                        elif nome != "" and xnome != "":
                            nome = nome +" "+ xnome +" "+ n[0]
                            self.addPersonalities(nome, titulo, persList)
                            nome=""
                            xnome="" 
                        else: 
                            nome = nome +" " + n[0]
                            #print nome
                            self.addPersonalities(nome, titulo, persList)
                            nome=""
                            xnome=""      
                    elif '\"' in x:
                        n=x.split('\"')
                        if nome == "":
                            nome = n[0]
                            #print nome
                            self.addPersonalities(nome, titulo, persList)
                            nome=""
                        elif nome != "" and xnome != "":
                            nome = nome +" "+ xnome +" "+ n[0]
                            self.addPersonalities(nome, titulo, persList)
                            nome=""
                            xnome="" 
                        else: 
                            nome = nome +" " + n[0]
                            #print nome
                            self.addPersonalities(nome, titulo, persList)
                            nome=""
                            xnome=""   
                    elif nome != "" and xnome != "":
                        nome = nome +" "+ xnome +" "+ x
                    elif nome != "":
                        nome = nome + " " + x
                    else:
                        nome = x
                elif x[0] == '\"' and len(x) > 3:
                    a=x.split('\"')
                    if a[1].isupper():
                        nome = a[1] 
                else:
                    if x == "de" or x == "da":
                        if nome != "":
                            xnome = x
                    else:
                        if nome!="":
                            #print nome
                            self.addPersonalities(nome, titulo, persList)
                            nome=""
                            xnome=""
                i=i+1
                persDict[l]=persList
        return persDict
     

        

    
    