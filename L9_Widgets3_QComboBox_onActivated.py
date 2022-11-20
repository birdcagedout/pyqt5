#https://youtu.be/BmAkbN1jmRk?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 09. 여러가지 위젯

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal, QBasicTimer, QTimerEvent, QDate
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent, QPixmap

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog, QCheckBox, QProgressBar, QCalendarWidget, QComboBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout



class Test9(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(300, 200)
		self.setWindowTitle("OnActivated")
		self.show()

	def initUI(self):
		self.label = QLabel('Ubuntu', self)

		self.combo = QComboBox(self)
		self.combo.addItem("Ubuntu")
		self.combo.addItem("Mandriva")
		self.combo.addItem("Fedora")
		self.combo.addItem("Arch")
		self.combo.addItem("Gentoo")
		self.combo.activated[str].connect(self.onActivated)

		self.combo.move(50, 50)
		self.label.move(50, 150)


	def onActivated(self, text):
		self.label.setText(text)
		self.label.adjustSize()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test9()
	sys.exit(app.exec())
