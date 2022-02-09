import sys

from PyQt5.QtWidgets import QWidget, QApplication

from fakeQQ_DAO import DAO
from fakeQQ_sessionWidet import Ui_sessionWidget

class SessionWidget(Ui_sessionWidget,QWidget):
    def __init__(self):
        super(SessionWidget, self).__init__()
        self.setupUi(self)

    def keyPressEvent(self, keyevent):
        print(f"键盘按键: {keyevent.text()},0X{keyevent.key():X} 被按下")
        if keyevent.key() ==0X1000004:
            print('发送按钮')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=SessionWidget()
    main.show()
    sys.exit(app.exec_())



