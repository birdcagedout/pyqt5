#https://youtu.be/BmAkbN1jmRk?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 09. 여러가지 위젯

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal, QBasicTimer, QTimerEvent, QDate
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent, QPixmap, QMovie

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog, QCheckBox, QProgressBar, QCalendarWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout



class Test9(QWidget):
	def __init__(self):
		super().__init__()
		

		self.resize(350, 180)
		self.setWindowTitle("QMovie")
		
		self.initUI()
		self.show()

	def initUI(self):
		self.hbox = QHBoxLayout(self)
		self.mov = QMovie('smile.gif')

		self.label = QLabel(self)
		self.label.setMovie(self.mov)

		self.hbox.addWidget(self.label)
		self.hbox.setContentsMargins(0,0,0,0)			# label이 hbox에 붙을 때 label <-> hbox 사이의 마진
		self.setLayout(self.hbox)

		self.mov.start()
		#print(f"framecount={mov.frameCount()}, width={mov.scaledSize().width()}, height={mov.scaledSize().height()}")
		print(f"{self.mov.frameRect().width()} x {self.mov.frameRect().height()}")
		#mov.destroyed.connect(print)
		#self.mov.deleteLater()
		#self.label.deleteLater()
		#print(f"widget: {label} Parent: {label.parentWidget()}")

		self.timer = QBasicTimer()
		self.timer.start(5000, self)
		self.timerCount = 0

		self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)

	def timerEvent(self, event: QTimerEvent) -> None:
		if self.timer.isActive():
			if self.timerCount == 0:
				self.resize(self.mov.frameRect().width(), self.mov.frameRect().height())

			if self.timerCount == 1:
			#	self.mov.deleteLater()
			#	print("mov deleted")
			#else:

				# mov를 delete하고, 나중에 label을 delete하려고 하면
				# label에 붙은 하위 위젯 mov까지도 자동으로 delete하려고 하기 때문에 런타임 에러가 뜬다.
				self.label.deleteLater()
				self.update()
				print("label deleted")
				self.timerCount += 1



if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test9()
	sys.exit(app.exec())
