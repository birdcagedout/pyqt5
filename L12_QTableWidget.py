#https://youtu.be/WOegxbnIG0U?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 12. QTableWidget

import sys, pickle

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal, QBasicTimer, QTimerEvent, QDate, QMimeData
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent, QPixmap, QDrag, QDragEnterEvent, QDropEvent, QPainter, QPen, QBrush, QFont, QColor, QPaintEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog, QCheckBox, QProgressBar, QCalendarWidget, QComboBox, QTableWidget, QTableWidgetItem


# 저장 버튼 눌렀을 때
def onClick():
	fp = open("out.txt", "wb")
	for r in range(win.count):
		for c in range(win.count):
			pickle.dump(win.table.item(r, c).text(), fp)		# 테이블의 str 객체를 하나씩 파일로 저장
	fp.close()


class Test12(QWidget):
	def __init__(self):
		super().__init__()
		self.count = 4
		self.initUI()
		self.resize(660, 240)
		self.setWindowTitle("QTableWidget")
		self.show()

	def initUI(self):
		self.createTable()
		self.btn = QPushButton('저장')
		self.btn.clicked.connect(onClick)

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.table)
		self.layout.addWidget(self.btn)

		self.setLayout(self.layout)
		self.show()


	def createTable(self):
		self.table = QTableWidget()
		self.table.setRowCount(self.count)
		self.table.setColumnCount(self.count)
		self.table.setHorizontalHeaderLabels(('이름', '국어', '영어', '수학'))		# 설정하지 않으면 1, 2, 3, 4로 설정됨

		# 만약 저장된 파일이 있다면 ==> 순차적으로 값을 가져와서 테이블 채우기
		try:
			fp = open("out.txt", "rb")
			for r in range(self.count):
				for c in range(self.count):
					self.table.setItem(r, c, QTableWidgetItem(str(pickle.load(fp))))		# pickle로 객체 하나씩 꺼내옴
			fp. close()
		
		# 만약 저장된 파일이 없다면 ==> 빈값으로 테이블 채우기
		except:
			for r in range(self.count):
				for c in range(self.count):
					self.table.setItem(r, c, QTableWidgetItem(""))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Test12()
	sys.exit(app.exec())
