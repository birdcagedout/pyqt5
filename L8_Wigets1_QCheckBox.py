#https://youtu.be/eAUXdxWiRUQ?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 08. 여러가지 위젯

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog, QCheckBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout



class Test8(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(350, 180)
		self.setWindowTitle("Widgets")
		self.show()

	def initUI(self):
		checkbox = QCheckBox('Show Title', self)
		checkbox.move(20, 20)
		checkbox.toggle()		# checked 상태로 변경
		checkbox.stateChanged.connect(self.changeTitle)

		
	# 마우스 클릭 이벤트 핸들러
	def changeTitle(self, state):
		if state == Qt.Checked:
			self.setWindowTitle('QCheckBox')
		else:
			self.setWindowTitle(' ')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test8()
	sys.exit(app.exec())
