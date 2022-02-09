import socket
import socketserver

import pymysql
import json
import random
import threading


class FakeQQServer:
    def __init__(self):
        self.serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.serverSocket.bind(("",42357))
        self.serverSocket.listen(512)
        print("开始监听")
        self.start()
    def start(self):
        while True:
            newTcpClient,ip_port =self.serverSocket.accept()
            print("新的客户端已经登陆，IP：{}，端口：{}".format(ip_port[0], ip_port[1]))
            subThread= threading.Thread(target=self.run,args=(newTcpClient,ip_port))
            # subThread.setDaemon(True)用法过时
            subThread.daemon = True
            subThread.start()
        self.serverSocket.close()
    def parse_data(self):
        pass
    def run(self,newTcpClient:socket.socket,ip_port):
        while True:
            print("接收数据")
            data=newTcpClient.recv(4096)

            print(len(data))
            print(data.decode("unicode_escape"))
            if len(data) == 0:
                newTcpClient.close()
                break



        pass


        pass


def main():
    server= FakeQQServer()
    pass
if __name__ == '__main__':
    main()
    pass

