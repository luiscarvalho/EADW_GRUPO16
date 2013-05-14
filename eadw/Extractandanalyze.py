
import sys
from collectionandstorage import Collection
from extraction import Extractionpersonalities
from search import Search

indexPath = '/Users/luiscarvalho/Desktop/EADW-Lab/project/indexdir/'
persListpath = '/Users/luiscarvalho/Desktop/EADW-Lab/project/personalities.txt'
stopWordspath = '/Users/luiscarvalho/Desktop/EADW-Lab/project/stopwords.txt'
run = True

while(run):
    print "\n\nPortuguese political personalities\n"
    print "1 - News Collection and Storage"
    print "2 - Stored News"
    print "3 - News Search"
    print "4 - Extraction of Named Entities"
    print "5 - Sentiment Analysis"
    print "6 - Exit\n"
    var = raw_input("Select an option: ")
    
    if ("1" in var):
        c = Collection.CollectStores(indexPath)
        c.collectStores()
    elif ("2" in var):
        print "\n"
        search = Search.Searcher(indexPath)
        search.allFeeds()
    elif ("3" in var):
        print "\n"
        query = raw_input("Enter a query to search: ")
        search = Search.Searcher(indexPath)
        searchlist = search.search(query)
        print "\nLIST OF NEWS RANKED BY RELEVANCE\nSTRUCTURE - News title :: News summary\n"
        for line in searchlist:
            print line
            print "\n"
    elif ("4" in var):
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
    elif ("5" in var):
        print "5"
    elif ("6" in var):
        print "\n"
        print "Tank you for your participation"
        run = False
    else:
        print "Insert a valid options"
    
    
    