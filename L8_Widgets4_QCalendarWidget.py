#https://youtu.be/eAUXdxWiRUQ?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 08. 여러가지 위젯

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal, QBasicTimer, QTimerEvent, QDate
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog, QCheckBox, QProgressBar, QCalendarWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout



class Test8(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(350, 180)
		self.setWindowTitle("Calendar")
		self.show()

	def initUI(self):
		vbox = QVBoxLayout(self)

		cal = QCalendarWidget(self)
		cal.setGridVisible(True)						# 격자선 보이게
		cal.clicked[QDate].connect(self.showDate)
		

		date = cal.selectedDate()
		dateString = f"{date.year()}-{date.month()}-{date.day()} ({date.shortDayName(date.dayOfWeek())})"

		vbox.addWidget(cal)

		self.label = QLabel(self)
		self.label.setText(dateString)

		vbox.addWidget(self.label)
		self.setLayout(vbox)

	def showDate(self, date):
		dateString = f"{date.year()}-{date.month()}-{date.day()} ({date.shortDayName(date.dayOfWeek())})"
		self.label.setText(dateString)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test8()
	sys.exit(app.exec())
