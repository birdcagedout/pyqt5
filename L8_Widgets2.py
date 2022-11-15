#https://youtu.be/eAUXdxWiRUQ?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 08. 여러가지 위젯

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog, QCheckBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout



class Test8(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(350, 180)
		self.setWindowTitle("Toggle Button")
		self.show()

	def initUI(self):
		self.color = QColor(0, 0, 0)

		btnRed = QPushButton('Red', self)
		btnRed.setCheckable(True)
		btnRed.move(10, 10)
		btnRed.clicked.connect(self.setColor)

		btnGreen = QPushButton('Green', self)
		btnGreen.setCheckable(True)
		btnGreen.move(10, 60)
		btnGreen.clicked.connect(self.setColor)

		btnBlue = QPushButton('Blue', self)
		btnBlue.setCheckable(True)
		btnBlue.move(10, 110)
		btnBlue.clicked.connect(self.setColor)

		self.frame = QFrame(self)
		self.frame.setGeometry(150, 20, 100, 100)
		self.frame.setStyleSheet('QWidget {background-color: %s }' % self.color.name())

		
	# 마우스 클릭 이벤트 핸들러
	def setColor(self, pressed):
		sender = self.sender()

		if pressed:
			val = 255
		else:
			val = 0
		
		if sender.text() == "Red":
			self.color.setRed(val)
		elif sender.text() == "Green":
			self.color.setGreen(val)
		elif sender.text() == "Blue":
			self.color.setBlue(val)
		
		self.frame.setStyleSheet("QFrame { background-color: %s }" % self.color.name())


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test8()
	sys.exit(app.exec())
