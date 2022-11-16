#https://youtu.be/eAUXdxWiRUQ?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 08. 여러가지 위젯

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal, QBasicTimer, QTimerEvent
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog, QCheckBox, QProgressBar
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout



class Test8(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(350, 180)
		self.setWindowTitle("ProgressBar")
		self.show()

	def initUI(self):
		self.progressBar = QProgressBar(self)
		self.progressBar.setGeometry(30, 40, 200, 25)

		self.btn = QPushButton('Start', self)
		self.btn.move(40, 80)
		self.btn.clicked.connect(self.doAction)

		self.timer = QBasicTimer()
		self.step = 0

	def doAction(self):
		if self.btn.text() == "Finished":
			return
		
		if self.timer.isActive():
			self.timer.stop()
			self.btn.setText('Start')
		else:
			self.timer.start(100, self)					# 100ms마다 TimerEvent 발생
			self.btn.setText('Stop')

	def timerEvent(self, event: QTimerEvent) -> None:
		if self.step >= 100:
			self.timer.stop()
			self.btn.setText("Finished")
			return
		else:
			self.step += 1
			self.progressBar.setValue(self.step)
		


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test8()
	sys.exit(app.exec())
