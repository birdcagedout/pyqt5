#https://youtu.be/1C94gdxAeuk?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 06. 이벤트와 시그널

import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPalette, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout


class Test6(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		btn1 = QPushButton("Button1", self)
		btn2 = QPushButton("Button2", self)

		btn1.move(30, 50)
		btn2.move(150, 50)

		btn1.clicked.connect(self.buttonClicked)
		btn2.clicked.connect(self.buttonClicked)

		self.statusBar()

		self.resize(300, 150)
		self.setWindowTitle("Mouse Event")
		self.show()

	# 1. 커스텀 정의된 버튼 이벤트 핸들러
	def buttonClicked(self):
		sender = self.sender()					# 이벤트가 발생한 객체 = self.sender()
		self.statusBar().showMessage(sender.text() + ' was pressed')

	# (비교용) 마우스 이벤트 핸들러
	def mouseMoveEvent(self, event: QMouseEvent) -> None:
		x = event.x()					# 마우스커서의 클라이언트영역 x좌표
		y = event.y()					# 마우스커서의 클라이언트영역 y좌표
		text = f"x: {x}, y: {y}"
		self.label.setText(text)

	# (비교용) 키 이벤트 핸들러
	def keyPressEvent(self, event: QKeyEvent) -> None:
		if event.key() == Qt.Key_Escape:
			self.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	#app.setStyle('Fusion')
	w = Test6()
	sys.exit(app.exec())
