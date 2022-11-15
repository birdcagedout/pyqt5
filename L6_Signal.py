#https://youtu.be/1C94gdxAeuk?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 06. 이벤트와 시그널

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal
from PyQt5.QtGui import QPalette, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout




class Communicate(QObject):
	closeApp = pyqtSignal()			# 신호를 보낼 수 있는 객체 생성



class Test6(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.c = Communicate()
		self.c.closeApp.connect(self.close)		# closeApp이라는 객체에 self.close()라는 slot에 연결함

		self.resize(300, 150)
		self.setWindowTitle("Signal")
		self.show()


	# 마우스 클릭 이벤트 핸들러
	def mousePressEvent(self, event: QMouseEvent) -> None:
		self.c.closeApp.emit()		# closeApp과 연결된 slot에 신호를 내보냄
	

	# (비교용) 키 이벤트 핸들러
	def keyPressEvent(self, event: QKeyEvent) -> None:
		if event.key() == Qt.Key_Escape:
			self.close()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	#app.setStyle('Fusion')
	w = Test6()
	sys.exit(app.exec())
