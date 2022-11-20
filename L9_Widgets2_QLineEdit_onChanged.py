#https://youtu.be/BmAkbN1jmRk?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 09. 여러가지 위젯

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal, QBasicTimer, QTimerEvent, QDate
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent, QPixmap

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog, QCheckBox, QProgressBar, QCalendarWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout



class Test9(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(350, 180)
		self.setWindowTitle("OnChanged")
		self.show()

	def initUI(self):
		self.label = QLabel(self)
		self.edit = QLineEdit(self)

		self.edit.move(60, 100)
		self.label.move(60, 40)
		self.edit.textChanged[str].connect(self.onChanged)

	def onChanged(self, text):
		print(text)						# QLineEdit에 있는 내용 전부가 text로 들어온다
		self.label.setText(text)
		self.label.adjustSize()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test9()
	sys.exit(app.exec())
