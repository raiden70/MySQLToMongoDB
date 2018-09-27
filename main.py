from MysqlConn import Mysqlcon
from MongoConn import MongoDB


def mainFunction(msqlHost,dbname,username,password,moHost,moPort):
    msql=Mysqlcon(msqlHost,dbname,username,password)
    mongo=MongoDB(moHost,moPort) # 27017 default
    mongo.create(dbname)
    mongo.create_collections(msql.get_tables())
    for i in mongo.db.collection_names():
        pass
    for j in msql.get_tables():
        c=msql.query_fetch_rows("select * from "+j)
        for p in c:
            mongo.insert_into(j,p)
    return mongo.db.collection_names()
#print(mongo.find_all("administrateur")[0])
