import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import fakeQQ_sessionWidet
from fakeQQ_registry import registry
from fakeQQ_DAO import DAO
from fakeQQ_loginWidget import Ui_Form
from fakeQQ_socketClient import Client
from PyQt5.QtCore import pyqtSlot
from fakeQQ_mainWidget import Ui_MainWindow
from fakeQQ_user import UserWidget


class MainWindow(Ui_MainWindow, QMainWindow):
    friendData = {}
    currentUser={}
    def __init__(self,dao:DAO):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.dao=dao



        self.initListWidget()
        self.initBtn()

    def initBtn(self):
        self.listWidget.itemDoubleClicked.connect(self.itemDoubleClick)


    def getUser(self) -> list:
        userData = self.dao.getFriend(self.currentUser)
        pass

    def initListWidget(self):
        self.userData = self.getUser()
        self.listWidget.addItem("1212")
        self.listWidget.addItem("1232")
        if not self.userData:
            return
        for user in self.userData:
            self.listWidget.addItem(QListWidgetItem(user['nickname']))
            print(user)
            pass
        pass

    def itemDoubleClick(self):
        print('双击' + '用户:{}'.format(self.listWidget.currentItem().text()))
        



    @pyqtSlot()
    def on_searchBtn_clicked(self):
        print("搜索按钮被点击")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    socketClient = Client()
    dao = DAO(socketClient)
    main = MainWindow(dao)
    main.show()
    sys.exit(app.exec_())
