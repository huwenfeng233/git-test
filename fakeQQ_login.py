import sys

from PyQt5.QtWidgets import *
from  PyQt5.QtCore import *
from  PyQt5.QtGui import *
from fakeQQ_registry import registry
from fakeQQ_DAO import DAO
from fakeQQ_loginWidget import Ui_Form
from fakeQQ_socketClient import Client
from PyQt5.QtCore import pyqtSlot


class Login_Wiget (Ui_Form,QWidget):
    userInputTime=QTime().currentTime()
    passwdInputTime=QTime().currentTime()
    def __init__(self,dao:DAO):
        super(Login_Wiget, self).__init__()
        self.setupUi(self)
        self.dao=dao
        # self.userLineEdit.textChanged.connect(self.on_userLineEdit_textChanged)
        self.userData={}
        self.initSignalSlot()
    def initSignalSlot(self):
        self.userLineEdit.textChanged.connect(self.userLineEdit_textChanged)
        self.passwdLineEdit.textChanged.connect(self.passwdLineEdit_textChanged)
        pass
    @pyqtSlot()
    def on_registerBtn_clicked(self):
        """执行登陆，向服务器发送登陆信息并接受返回值"""
        self.registryWidget=registry(dao)
        self.registryWidget.show()
        print("注册按钮")
        pass

    # @pyqtSlot()
    def passwdLineEdit_textChanged(self):
        print("输入密码")
        self.userData['passwd']= self.passwdLineEdit.text()

        pass
    @pyqtSlot()
    def on_loginBtn_clicked(self):
        """执行注册函数，向服务器发送登陆信息，并接受返回值"""
        self.dao.login(self.userData)
        # print(self.userData)
        print("登陆按钮")

        pass

    # @pyqtSlot()
    def userLineEdit_textChanged(self):

        print("账户输入")
        self.userData['nickname'] = self.userLineEdit.text()
        self.userData['account'] = self.userLineEdit.text()
        # print(self.userData)








if __name__=="__main__":
    app=QApplication(sys.argv)
    socketClient = Client()
    dao = DAO(socketClient)
    main =Login_Wiget(dao)
    main.show()
    sys.exit(app.exec_())