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
		self.setWindowTitle("QPixmap")
		self.show()

	def initUI(self):
		hbox = QHBoxLayout(self)
		pixelMap = QPixmap('1.PNG')

		label = QLabel(self)
		label.setPixmap(pixelMap)

		hbox.addWidget(label)
		self.setLayout(hbox)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test9()
	sys.exit(app.exec())
