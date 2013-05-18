
import sys
from collectionandstorage import Collection
from extraction import Extractionpersonalities
from search import Search
from sentimentanalysis import SentimentAnalysis
import pickle
import string
import re

#------- Carrega o vocabulario com a polaridade -----------

arq = open('SemA.txt','rb') 
dicA = pickle.load(arq)
arq.close()
arq = open('SemB.txt','rb')
dicB = pickle.load(arq)
arq.close()
arq = open('SemC.txt','rb')
dicC = pickle.load(arq)
arq.close()
arq = open('SemD.txt','rb') 
dicD = pickle.load(arq)
arq.close()
arq = open('SemE.txt','rb') 
dicE = pickle.load(arq)
arq.close()
arq = open('SemF.txt','rb')
dicF = pickle.load(arq)
arq.close()

vocabPolDict=dict()

vocabPolDict.update(dicF)
vocabPolDict.update(dicA)
vocabPolDict.update(dicB)
vocabPolDict.update(dicC)
vocabPolDict.update(dicD)
vocabPolDict.update(dicE)

#print vocabPolDict

indexPath = 'indexdir/'
persListpath = 'personalities.txt'
run = True

#---------- carrega a lista de stopWord ---------
stopwords=open("stopwords.txt","r")
stopwordList=[]

for line in stopwords:
    l=line.split(",")
    for word in l:
        stopwordList.append(word)

while(run):
    print "\n\nPortuguese political personalities\n"
    print "1 - News Collection and Storage"
    print "2 - Stored News"
    print "3 - News Search"
    print "4 - Extraction of Named Entities"
    print "5 - Sentiment Analysis for news"
    print "6 - Sentiment Analysis for query"
    print "7 - Exit\n"
    var = raw_input("Select an option: ")
    
    if "1" in var:
        c = Collection.CollectStores(indexPath)
        c.collectStores()
    elif "2" in var:
        print "\n"
        search = Search.Searcher(indexPath)
        search.allFeeds()
    elif "3" in var:
        print "\n"
        query = raw_input("Enter a query to search: ")
        search = Search.Searcher(indexPath)
        searchlist = search.search(query)
        print "\nLIST OF NEWS RANKED BY RELEVANCE\nSTRUCTURE - News title :: News summary\n"
        for line in searchlist:
            print line
            print "\n"
    elif "4" in var:
        print "\n"
        query = raw_input("Enter a query to search: ")
        extraction = Extractionpersonalities.Extraction(indexPath, persListpath)
        persDict = extraction.seachPersonalities(query)
        #print persDict
        for news in persDict:
            print "\nNEWS:\n"
            n=news.split("::")
            print "Title: " + n[0]
            print "Summary:" + n[1]
            print "\nMENTIONED PERSONALITIES:\n"
            for persona in persDict[news]:
                print persona
    elif "5" in var:
        print "\n"
        query = raw_input("Enter a query to search: ")
        extraction = Extractionpersonalities.Extraction(indexPath, persListpath)
        persDict = extraction.seachPersonalities(query)
        sentiment = SentimentAnalysis.SentimentA(stopwordList, vocabPolDict)
        for news in persDict:
            print "\nNEWS:\n"
            n=news.split("::")
            print "Title: " + n[0]
            print "Summary:" + n[1]
            print "\nMENTIONED PERSONALITIES:\n"
            for persona in persDict[news]:
                print persona
            print '\nANALISE DE SENTIMENTOS:\n'
            sentim = sentiment.sentiment(news, persDict[news])
            if sentim==0:
                print "neutro"
            elif sentim>0:
                print "positivo"
            else:
                print "negativo" 
    elif "6" in var:
        print "\n"
        persSentDict = dict()
        query = raw_input("Enter a query to search: ")
        extraction = Extractionpersonalities.Extraction(indexPath, persListpath)
        persDict = extraction.seachPersonalities(query)
        sentiment = SentimentAnalysis.SentimentA(stopwordList, vocabPolDict)
        for news in persDict:
            sentim = sentiment.sentiment(news, persDict[news])
            for pers in persDict[news]:
                if pers in persSentDict:
                    persSentDict[pers][0]+=1
                    if sentim==0:
                        persSentDict[pers][3]+=1    
                    elif sentim>0:
                        persSentDict[pers][1]+=1 
                    else:
                        persSentDict[pers][2]+=1
                else:
                    if sentim==0:
                        persSentDict[pers]=[1,0,0,1]    
                    elif sentim>0:
                        persSentDict[pers]=[1,1,0,0] 
                    else:
                        persSentDict[pers]=[1,0,1,0]
        for persona in persSentDict:
            print "\nPERSONALITY: " + persona
            print "NUMBER OF OCCURRENCES: " + str(persSentDict[persona][0])
            print "NUMBER OF POSITIVE SENTIMENT ANALYSIS: " + str(persSentDict[persona][1]) 
            print "NUMBER OF NEGATIVE SENTIMENT ANALYSIS: " + str(persSentDict[persona][2])
            print "NUMBER OF NEUTRAL SENTIMENT ANALYSIS: " + str(persSentDict[persona][3]) 
    elif "7" in var:
        print "\n"
        print "Thank you for your participation"
        run = False
    else:
        print "Insert a valid options"
    
    
    