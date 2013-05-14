

from collectionandstorage import feedparser

import re
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import *
from whoosh.query import *
import os, os.path
from whoosh import index

class CollectStores:
    
    def __init__(self, path):
        self.p = path
    
    #--------------------------------  STORES FEEDS  ---------------------------------
    
    def index_creation(self, feedsDN, feedsJN):
        schema = Schema(id = TEXT(stored=True), content=TEXT(stored=True))
        ix = index.create_in(self.p, schema)
        writer = ix.writer()
        print "NEWS FROM DIARIO DE NOTICIAS:\n"
        for feeddn in feedsDN.entries:
            print feeddn.title
            print feeddn.summary.split('<img')[0]
            print "\n" 
            writer.add_document(id=feeddn.title, content=feeddn.title+" :: "+feeddn.summary.split('<img')[0])
        
        print "NEWS FROM JORNAL DE NOTICIAS:\n"
        for feedjn in feedsJN.entries:
            print feedjn.title
            print feedjn.summary.split('<img')[0]
            print "\n" 
            writer.add_document(id=feedjn.title, content=feedjn.title+" :: "+feedjn.summary.split('<img')[0])
        writer.commit()
    
    def incremental_index(self, feedsDN, feedsJN):
        indx = open_dir(self.p)
        idList=[]
        with indx.searcher() as searcher:
            writer = indx.writer()
        
            for fields in searcher.all_stored_fields():
                feed_id=fields['id']
                idList.append(feed_id)
            
            print "NEWS FROM DIARIO DE NOTICIAS:\n"
            for fddn in feedsDN.entries:
                if fddn.title not in idList:
                    print fddn.title.encode('utf-8')
                    print fddn.summary.split('<img')[0].encode('utf-8')
                    print "\n" 
                    writer.add_document(id=fddn.title, content=fddn.title+" :: "+fddn.summary.split('<img')[0])
            
            print "NEWS FROM JORNAL DE NOTICIAS:\n"    
            for fdjn in feedsJN.entries:
                if fdjn.title not in idList:
                    print fdjn.title.encode('utf-8')
                    print fdjn.summary.split('<img')[0].encode('utf-8')
                    print "\n" 
                    writer.add_document(id=fdjn.title, content=fdjn.title+" :: "+fdjn.summary.split('<img')[0]) 
            writer.commit()            

    
    def collectStores(self):
        #-------------------------  GET FEEDS  --------------------------
        fDN = feedparser.parse("http://feeds.dn.pt/DN-Politica")
        fJN = feedparser.parse("http://feeds.jn.pt/JN-Politica")

        #print feedsDN.entries[1]
        #print feedsJN.entries[1]
                
        if not os.path.exists(self.p):
            #print "indexdir nao existe!\n" 
            os.mkdir(self.p)
            self.index_creation(fDN, fJN)
        else:
            #print "indexdir ja existe!\n"
            self.incremental_index(fDN, fJN)
    
          
          
          
      
      
      
      
      
      
      
    

