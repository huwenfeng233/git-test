import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from fakeQQ_UserWidget import  Ui_Form

class UserWidget(Ui_Form,QtWidgets.QWidget):
    def __init__(self,*args):
        super(UserWidget, self).__init__()
        self.setupUi(self)
        if len(args)==0:
            self.headerLabel.setText("默认头像")
            self.nameLaybel.setText("默认用户名")
            pass

        if len(args)==2:
            self.headerLabel.setText(args[0])
            self.nameLaybel.setText(args[1])

            pass
        pass

    pass

if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=UserWidget()
    main.show()
    sys.exit(app.exec_())