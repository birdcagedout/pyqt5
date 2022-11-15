#https://youtu.be/FnTFQ_wJSEo?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 07. 다이얼로그

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal
from PyQt5.QtGui import QPalette, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout



class Test7(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(350, 150)
		self.setWindowTitle("Signal")
		self.show()

	def initUI(self):
		self.btn = QPushButton("Dialog", self)
		self.btn.move(20, 20)
		self.btn.clicked.connect(self.showDialog)

		self.edit = QLineEdit(self)
		self.edit.move(130, 22)
		
	# 마우스 클릭 이벤트 핸들러
	def showDialog(self):
		text, ok = QInputDialog.getText(self, 'Input Dialog', "Enter your name: ")

		if ok:
			self.edit.setText(text)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test7()
	sys.exit(app.exec())
