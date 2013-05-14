
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import *
from whoosh.query import *

class Searcher:

    def __init__(self, path):
        self.p = path
        
    def search(self, string):
        list=[]
        ix = open_dir(self.p)
        with ix.searcher() as searcher:
            query = QueryParser("content", ix.schema, group=OrGroup).parse(u(string))
            results = searcher.search(query)
            for r in results:
                #list.append(r.get('id'))
                list.append(r['content'])
                #print "content: "+ r['content']
                #print list
            return list

        #lista = search("Troika")

        #print lista

    def allFeeds(self):
        nfeed=0
        #file=open("teste.txt", "a")
        ix = open_dir(self.p)     
        with ix.searcher() as searcher:
            for fields in searcher.all_stored_fields():
                print nfeed
                print "-------------------------------------------------------\n"
                print fields.get('content').encode('utf-8')
                print "\n"
                #file.write(str(fields.get('content')))
                nfeed+=1
        