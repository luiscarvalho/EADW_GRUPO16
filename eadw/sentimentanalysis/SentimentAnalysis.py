

stopwords=open("/Users/luiscarvalho/Desktop/EADW-Lab/project/stopwords.txt","r")
stopwordList=[]

for line in stopwords:
    l=line.split(",")
    for word in l:
        stopwordList.append(word)
        
print stopwordList

class SentimentA():
    
    def __init__(self, stopWordL, persNewsDict, vocabPolDict):
        self.stopWList = stopWordL
        self.persNewsD = persNewsDict
        self.vocabPolD = vocabPolDict
        
    def sentiment(self):
        "asasdasd"
        

        
        
