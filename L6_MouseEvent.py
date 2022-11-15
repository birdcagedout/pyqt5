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
		self.posText = ""

		self.initUI()

	def initUI(self):
		
		grid = QGridLayout()
		grid.setSpacing(10)

		x = 0
		y = 0

		self.posText = f"x: {x}, y: {y}"

		self.label = QLabel(self.posText, self)
		grid.addWidget(self.label, 0, 0, Qt.AlignTop)

		# 1. 마우스이벤트 캡처 시작
		self.setMouseTracking(True)

		self.setLayout(grid)

		self.resize(300, 150)
		self.setWindowTitle("Mouse Event")
		self.show()
	
	# 2. 마우스 이벤트 핸들러
	def mouseMoveEvent(self, event: QMouseEvent) -> None:
		x = event.x()					# 마우스커서의 클라이언트영역 x좌표
		y = event.y()					# 마우스커서의 클라이언트영역 y좌표
		text = f"x: {x}, y: {y}"
		self.label.setText(text)


	# 3. 키 이벤트 핸들러
	def keyPressEvent(self, event: QKeyEvent) -> None:
		if event.key() == Qt.Key_Escape:
			self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test6()
	sys.exit(app.exec_())
