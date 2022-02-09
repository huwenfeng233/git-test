import pymysql


class Manager:
    def __init__(self):

        pass
    def initSql(self):
        con=pymysql.Connection(host='bighu.com.cn', user='root',password= '42357',database= "fakeQQ")
        cur=con.cursor()

        cur.execute("")
        pass
