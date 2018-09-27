import mysql.connector

class Mysqlcon():

    def __init__(self,host,db,username,password):
        self.host=host
        self.db=db
        self.username=username
        self.password=password
        self.columns=[]
        self.tables=[]

    def connection(self):
        return mysql.connector.connect(database=self.db, user=self.username, password=self.password, host=self.host)

    def query_fetch_rows(self,query):
        db=self.connection()
        self.cursor = db.cursor(dictionary=True)
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def column_name(self):
        del self.columns[:]
        for c in self.cursor.column_names:
            self.columns.append(c)
        return self.columns

    def get_tables(self):
        del self.tables[:]
        db = self.connection()
        self.cursor = db.cursor()
        self.cursor.execute("show tables")
        for i in self.cursor.fetchall():
            self.tables.append(i[0])
        return self.tables


