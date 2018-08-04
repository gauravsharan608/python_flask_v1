import mysql.connector
import sys,logging


class DBConnect():
    'Common class to get connection object to connect with mysql'

    @staticmethod
    def getConnection():
        """Common method to establish DB connection and reuse it
        """
        try:
            conn = mysql.connector.connect(user='sqluser1', password='Mind@1234$',
                              host='mongosql2.eastus2.cloudapp.azure.com',
                              database='banking_mindtree')
            print ("Connection Established\n")
            #logging.info("Connection Established")
            
            return conn
        except Exception as e:
             logging.error("Connection Error ->"+str(e))

#dbconfig = DBConnect()
#conn = DBConnect.getConnection()
#print(conn)
