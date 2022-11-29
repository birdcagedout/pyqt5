import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.slider = QSlider(Qt.Horizontal, self)
        # self.slider.move(30, 30)
        # self.slider.setRange(0, 50)
        # self.slider.setSingleStep(2)

        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 9)
        self.dial.setNotchesVisible(True)

        self.lcd = QLCDNumber(self)
        self.lcd.setSegmentStyle(QLCDNumber.Outline)
        self.lcd.move(50, 20)

        self.btn = QPushButton(self)
        # btn.setStyleSheet("border-radius : 10; border-style : outset; background-image : url(setting50.png;")
        self.btn.setStyleSheet("""border-image : url(setting50_original.png);
            background-color : #ccc; border-radius : 10px;
        """)
        # btn.setIcon(btnicon)
        # btn.setIconSize(QSize(50, 50))
        self.btn.move(35, 160)
        self.btn.resize(50+10, 50+10)
        self.btn.clicked.connect(self.mousePressEvent)
        self.btn.released.connect(self.mouseReleaseEvent)
        

        # self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.valueChanged)
        # btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def mousePressEvent(self):
        sender = self.sender()
        if sender == self.btn:
            self.btn.setStyleSheet("border-image : url(setting50_pressed.png)")

    def mouseReleaseEvent(self):
        sender = self.sender()
        if sender == self.btn:
            self.btn.setStyleSheet("border-image : url(setting50_original.png)")
    
    def valueChanged(self):
        sender: QDial = self.sender()
        val = sender.value()
        self.lcd.display(val)
        print(sender.value())
        self.setWindowOpacity((10 - val)/10)

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())