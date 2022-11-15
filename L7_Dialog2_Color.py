#https://youtu.be/FnTFQ_wJSEo?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 07. 다이얼로그

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout



class Test7(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(250, 180)
		self.setWindowTitle("Signal")
		self.show()

	def initUI(self):
		color = QColor(0, 0, 0)

		self.btn = QPushButton('Dialog', self)
		self.btn.move(20, 20)
		self.btn.clicked.connect(self.showDialog)

		self.frame = QFrame(self)
		self.frame.setStyleSheet('QWidget {background-color: %s }' % color.name())			# "#000000"
		self.frame.setGeometry(130, 22, 100, 100)

		
	# 마우스 클릭 이벤트 핸들러
	def showDialog(self):
		color = QColorDialog.getColor()

		# OK이면 isValid() == True, Cancel이면 False
		if color.isValid():
			self.frame.setStyleSheet("QWidget { background-color: %s }" % color.name())		# '#456dff'


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test7()
	sys.exit(app.exec())
