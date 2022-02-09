import json
import sys

from PyQt5.QtWidgets import *
from  PyQt5.QtCore import *
from  PyQt5.QtGui import *

from fakeQQ_DAO import DAO
from fakeQQ_registryWidget import Ui_registryWidget

class registry(Ui_registryWidget,QWidget):


    def __init__(self,dao:DAO):
        self.dao=dao
        super(registry, self).__init__()
        self.setupUi(self)
        self.setData()
        self.registryData={}
    @pyqtSlot()
    def on_registryBtn_clicked(self):
        if not self.checkData():
            return
        else:
            self.registryData['nickname']=self.nicknameLEt.text()
            self.registryData['motto']=self.mottoLEt.text()
            self.registryData['birthday']=self.birthDEt.time()
            self.registryData['location']=self.locationLEt.text()
            self.registryData['passwd']=self.passwdLEt.text()
            self.registryData['gender']=self.genderComboBox.currentText()
            self.registryData['job']=self.jobLEt.text()
            # jsonData=json.dumps(self.registryData)
            print(type(self.registryData))
            self.dao.registry(self.registryData)
        print("按钮被按下")
    def setData(self):
        # self.nicknameLEt.setText("我心飞翔")
        self.nicknameLEt.setPlaceholderText("我心飞翔")
        self.mottoLEt.setPlaceholderText("这个人很懒，什么也没留下")
        self.genderComboBox.setCurrentIndex(2)
        self.passwdLEt.setEchoMode(QLineEdit.PasswordEchoOnEdit)


    def checkData(self)->bool:
        if len(self.nicknameLEt.text())==0:
            QMessageBox.information(self,'错误','昵称不能为空',QMessageBox.Ok)
            return False

        if len(self.passwdLEt.text())==0:
            QMessageBox.information(self, '错误', '密码不能为空', QMessageBox.Ok)
            return False
        return True





        pass


        pass
if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=registry()
    main.show()
    sys.exit(app.exec_())

