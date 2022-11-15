#https://youtu.be/1C94gdxAeuk?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 06. 이벤트와 시그널

import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout


class Test6(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		
		# 1. LCD 7-segment display, Slider
		lcd = QLCDNumber(self)
		slider = QSlider(Qt.Horizontal, self)
		slider.valueChanged.connect(lcd.display)		# 이벤트 연결

		vbox = QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(slider)
		
		self.setLayout(vbox)
		
		self.resize(300, 150)
		self.setWindowTitle("signal and slot")
		self.show()

	# 2. 키 이벤트 핸들러
	def keyPressEvent(self, event: QKeyEvent) -> None:
		if event.key() == Qt.Key_Escape:
			self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test6()
	sys.exit(app.exec_())

