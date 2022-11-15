#https://youtu.be/FnTFQ_wJSEo?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 07. 다이얼로그

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout



class Test7(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(250, 180)
		self.setWindowTitle("Signal")
		self.show()

	def initUI(self):
		vbox = QVBoxLayout()

		btn = QPushButton('Dialog', self)
		btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		btn.move(20, 20)
		btn.clicked.connect(self.showDialog)

		self.label = QLabel("Knowledge matters", self)
		self.label.move(130, 20)

		vbox.addWidget(btn)
		vbox.addWidget(self.label)

		self.setLayout(vbox)

		
	# 마우스 클릭 이벤트 핸들러
	def showDialog(self):
		font, ok = QFontDialog.getFont()

		if ok:
			self.label.setFont(font)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test7()
	sys.exit(app.exec())
