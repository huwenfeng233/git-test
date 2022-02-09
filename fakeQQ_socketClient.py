import concurrent
import socket
import json
from  PyQt5.QtCore import *
class Client(QThread):
    config = {"host": "www.bighu.com.cn", "user": "root", "password": "42357", "port": 9999}
    configTest={"host": "127.0.0.1", "user": "root", "password": "42357", "port": 42357}

    def __init__(self):
        pass
        # clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # clientSocket.connect((self.config['host'], self.config['port']))
        # data="""fakeQQ/1.1
        #
        #                         CONNECT BY{}""".format(clientSocket.getsockname()[0])
        # clientSocket.send("""fakeQQ/1.1
        #
        #                         CONNECT BY{}""".format(clientSocket.getsockname()[0]).encode(),4096 )
        # print(data)
    def run(self):
        pass
        print("启动")
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.clientSocket.connect((self.configTest['host'], self.configTest['port']))
        except ConnectionRefusedError as e:
            print('服务器连接失败！')
            exit(1)
        data =\
"""fakeQQ/1.1

CONNECT BY {}\n""".format(self.clientSocket.getsockname()[0])
        # self.clientSocket.send(data.encode(), 4096)
        # print(data)
        print("连接服务器成功")
    def send(self,jsondata:str):
        print("发送内容：{}\n".format(jsondata))
        # recv=self.clientSocket.send(jsondata.encode())

        recv = self.clientSocket.send(jsondata.encode("UTF-8"),4096)

        return recv
    

    pass

class ClientThread(QThread):
    def __init__(self):
        super(ClientThread, self).__init__()
    def run(self):
        pass
if __name__ == '__main__':
    client=Client()
    client.run()
    pass