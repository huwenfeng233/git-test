import threading
from  fakeQQ_login import Login_Wiget
from fakeQQ_socketClient import Client
from fakeQQ_DAO import DAO
if __name__ == '__main__':
    socketClient=Client()
    dao=DAO(socketClient)

    loginWiget= Login_Wiget()

    pass