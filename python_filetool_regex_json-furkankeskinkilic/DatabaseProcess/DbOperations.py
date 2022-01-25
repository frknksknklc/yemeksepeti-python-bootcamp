from datetime import datetime
import sqlite3
from FileProcess.DataParser import DataParser
from Models.user import User
class DbOperations():
    def __init__(self,dbpath: str) -> None:
        self.dbpath=dbpath
        self.tableName=self.createTableName()
        self.dbConnection=self.getConnection(dbpath)

    def getConnection(self,dbName: str) -> sqlite3.Connection:
        conn = sqlite3.connect(dbName)
        return conn
        
    def closeConnection(self,conn: sqlite3.Connection):
        conn.close()
    
    def createTableName(self):
        tableid=datetime.now().strftime('%Y_%m_%d_%H%M%S')
        tableName="user_"+tableid
        return tableName    

    def createTable(self):
        """
        creates a new table with the name of current time
        """                
        tableCreatingQuery = f'''
        CREATE TABLE "{self.tableName}" (
            "user_id"	INTEGER NOT NULL UNIQUE,
            "username"	TEXT,
            "email" TEXT,
            "full_name"	TEXT,
            "emailuserlk"	INTEGER,
            "usernamelk"	INTEGER,
            "birth_year"	INTEGER,
            "birth_month"	INTEGER,
            "birth_day"	INTEGER,
            "country"	TEXT,
            "active_status"	INTEGER,
            PRIMARY KEY("user_id")
        );
        '''
        self.dbConnection.execute(tableCreatingQuery)

    def insertUserList(self, userlist): 
        for user in userlist:
            self.insertUser(user)

    def insertUser(self,user :User) ->str:
        insertingQuery=f"""
        INSERT INTO {self.tableName} 
        (username,email,full_name,emailuserlk,usernamelk,birth_year,
        birth_month,birth_day,country,active_status)
        VALUES (?,?,?,?,?,?,?,?,?,?)"""        
         
        cr=self.dbConnection.cursor()
        cr.execute(insertingQuery,(user.username,user.email,user.fullName,user.emailUsrLk,user.userNameLk,user.yearOfBirth,user.birthMonth,user.birthDay,user.country,user.ap))
        self.dbConnection.commit()