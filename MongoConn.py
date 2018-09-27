from pymongo import MongoClient

class MongoDB:
    def __init__(self,host,port):
        self.client = MongoClient(host, port)
        self.collections={}

    def create(self,dbname):
        self.db=self.client[dbname]

    def create_collections(self,tables):
        for i in tables:
            self.db.drop_collection(i)
            self.db.create_collection(i)
            self.collections[i]=self.db[i]

    def insert_into(self,tablename,value):
        self.collections[tablename].insert(value)


    def find_all(self, tablename):
       return self.collections[tablename].find()




