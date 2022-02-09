import json
import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, date


from PyQt5.QtCore import QTime, Qt

import fakeQQ_socketClient
from fakeQQ_socketClient import Client
import threading

class ComplexEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj,QTime):
            return obj.toString(Qt.DefaultLocaleLongDate)
            pass
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

class DAO:
    def __init__(self, client_Socket: fakeQQ_socketClient.Client):
        self.clientSocket = client_Socket
        self.clientSocket.run()
        pass

    def check(self, check_data: dict):
        """测试是否与服务器处于连接"""
        # threading.Thread(target=self.clientSocket.send, args=(check_data,))
        data = json.dumps(check_data, cls=ComplexEncoder)
        data = "fakeQQ/1.0\n\ncheck\n" + data
        self.clientSocket.run()
        with ThreadPoolExecutor(max_workers=1) as t:
            res=t.submit(self.clientSocket.send,data)
            return res
    def registry(self, registry_data: dict):
        """ 注册用户"""
        data=json.dumps(registry_data,cls=ComplexEncoder)
        data="fakeQQ/1.0\n\nregistry\n"+data
        self.clientSocket.run()
        with ThreadPoolExecutor(max_workers=1) as t:
            res=t.submit(self.clientSocket.send,data)
            return res
    def login(self, login_data: dict):
        """ 登陆检查"""
        data = json.dumps(login_data, cls=ComplexEncoder)
        data = "fakeQQ/1.0\n\nlogin\n" + data
        self.clientSocket.run()
        with ThreadPoolExecutor(max_workers=1) as t:
            res=t.submit(self.clientSocket.send,data)
            return res
    def add(self, add_data: dict):
        """添加用户"""
        data = json.dumps(add_data, cls=ComplexEncoder)
        data = "fakeQQ/1.0\n\nadd\n" + data
        self.clientSocket.run()
        with ThreadPoolExecutor(max_workers=1) as t:
            res=t.submit(self.clientSocket.send,data)
            return res
    def search(self, search_data: dict):
        """搜索用户"""
        data = json.dumps(search_data, cls=ComplexEncoder)
        data = "fakeQQ/1.0\n\nsearch\n" + data
        self.clientSocket.run()
        with ThreadPoolExecutor(max_workers=1) as t:
            res=t.submit(self.clientSocket.send,search_data)
            return res
    def delete(self, delete_data: dict):
        """删除用户"""
        data = json.dumps(delete_data, cls=ComplexEncoder)
        data = "fakeQQ/1.0\n\ndelete\n" + data
        self.clientSocket.run()
        with ThreadPoolExecutor(max_workers=1) as t:
            res=t.submit(self.clientSocket.send,delete_data)
            return res

    def message(self,message_data:dict):
        """发送消息"""
        data = json.dumps(message_data, cls=ComplexEncoder)
        data = "fakeQQ/1.0\n\nmessage\n" + data
        self.clientSocket.run()
        with ThreadPoolExecutor(max_workers=1) as t:
            res=t.submit(self.clientSocket.send,message_data)
            return res
    def getFriend(self,friend_data:dict):
        """获取联系人列表"""
        data = json.dumps(friend_data, cls=ComplexEncoder)
        data = "fakeQQ/1.0\n\nmessage\n" + data
        self.clientSocket.run()
        with ThreadPoolExecutor(max_workers=1) as t:
            res = t.submit(self.clientSocket.send, data)
            return res
        pass


login="""
    登陆
"""
registry="""
    注册
"""
add="""
    添加
"""
search="""
    搜索
"""
delete="""
    删除 
"""
message="""
    消息
"""
check="""
    心跳
"""

if __name__ == '__main__':
    dao=DAO(client_Socket=fakeQQ_socketClient.Client())
    dao.login(login)
    dao.search(search)
    dao.registry(registry)
