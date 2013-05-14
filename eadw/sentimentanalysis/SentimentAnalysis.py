

stopwords=open("/Users/luiscarvalho/Desktop/EADW-Lab/project/stopwords.txt","r")
stopwordList=[]

for line in stopwords:
    l=line.split(",")
    for word in l:
        stopwordList.append(word)
        
#print stopwordList

class SentimentA():
    
    def __init__(self, stopWordL, vocabPolDict):
        self.stopWList = stopWordL
        self.vocabPolD = vocabPolDict
        
    def sentiment(self, news, personalList):
        valor2=0
        i=0
        j=0
        listaSplit2=[]
        avaliacao = dict()

        titulo = news.split("::")[0]
        summary = news.split("::")[1]
        summary2=summary.split()

        ##Tratamento dos nomes das personalidades, retirar do texto
        for personalidade in personalList:
        
            listaSplit1=personalidade.split()
            for nomeAnome in listaSplit1:
                listaSplit2.append(nomeAnome)
            
        
    
        for summary3 in summary2:
        #print summary3
        
            n1=summary3.split(',')[0]
            n2=n1.split('.')[0]
            n=n2.split('...')[0]
            

            if stopwordList.count(n)<1 and n not in listaSplit2:
                if n=="n\xc3\xa3o" or n=="N\xc3\xa3o":
                    i=1
                else:
                    if i==1 and j<2:
                        if self.vocabPolD.has_key(n):
                            pol=self.vocabPolD.get(n)
                            if int(pol)>0:
                                avaliacao[n]="-1"
                                i=0
                                j=0
                            elif int(pol)<0:
                                avaliacao[n]="1"
                                i=0
                                j=0
                            elif int(pol)==0:
                                j=j+1
                                pol="0"
                                avaliacao[n]=pol
                    else:
                        if i==1 and j>2:
                            j=0
                            i=0
                            avaliacao["Nao"]="-1"
                        elif self.vocabPolD.has_key(n):
                            pol=self.vocabPolD.get(n)
                            #print n
                            avaliacao[n]=pol
                            #print pol
                        else:
                            pol="0"
                            
                            avaliacao[n]=pol
                            #print n
                            #print pol
        #else:
            #print summary3
            #print "palavra rejeitada"
        avaliacaoFinal=avaliacao.values()
        print avaliacaoFinal
        for valor in avaliacaoFinal:
            valor2=valor2+int(valor)
        print valor2
        return valor2
        
        
        

        
        
