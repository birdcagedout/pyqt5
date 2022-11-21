#https://youtu.be/uXdC_osU7-c?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 11. QPainter

import sys, random

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal, QBasicTimer, QTimerEvent, QDate, QMimeData
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent, QPixmap, QDrag, QDragEnterEvent, QDropEvent, QPainter, QPen, QBrush, QFont, QColor, QPaintEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog, QCheckBox, QProgressBar, QCalendarWidget, QComboBox




class Test11(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(400, 200)
		self.setWindowTitle("Drawing text")
		self.show()

	def initUI(self):
		pass		

	# paintEvent 오버라이드
	def paintEvent(self, event: QPaintEvent) -> None:
		painter = QPainter()
		painter.begin(self)

		#===== QPainter 객체로 할 수 있는 다섯가지 기능 =====
		#self.myDrawText(event, painter)
		#self.myDrawPoints(painter)
		#self.myDrawRectangles(painter)
		self.myDrawLines(painter)
		#self.myDrawBrushes(painter)		# 흑백무늬 함수는 생략
		
		painter.end()

	# 글자 그리기
	def myDrawText(self, event: QPaintEvent, painter: QPainter):
		painter.setPen(QColor(168, 34, 3))
		painter.setFont(QFont('Malgun Gothic', 15))
		painter.drawText(event.rect(), Qt.AlignCenter, "QPainter로 글씨쓰기")		# event.rect() = 클라이언트 영역 = (0, 0, 400, 200)
		
	# 점 찍기
	def myDrawPoints(self, painter: QPainter):
		painter.setPen(Qt.red)
		size = self.size()

		for i in range(1000):
			x = random.randint(0, size.width())
			y = random.randint(0, size.height())
			painter.drawPoint(x, y)

	# 사각형 그리기
	def myDrawRectangles(self, painter: QPainter):
		# 펜 생성
		col = QColor('#521E8D')
		#col.setNamedColor('#521E8D')
		painter.setPen(col)

		# RGB만으로 Brush 생성
		painter.setBrush(QColor(200, 0, 0))
		painter.drawRect(10, 45, 90, 60)

		# RGBA로 Brush 생성(위아래 Alpha값에 따른 변화)
		painter.setBrush(QColor(255, 80, 0, 50))
		painter.drawRect(130, 45, 90, 60)
		painter.setBrush(QColor(255, 80, 0, 200))
		painter.drawRect(130, 115, 90, 60)

		# RGBA로 Brush 생성(위아래 Alpha값에 따른 변화)
		painter.setBrush(QColor(25, 0, 90, 20))
		painter.drawRect(250, 45, 90, 60)
		painter.setBrush(QColor(25, 0, 90, 200))
		painter.drawRect(250, 115, 90, 60)

	# 선 그리기
	def myDrawLines(self, painter: QPainter):
		pen = QPen(Qt.black, 2, Qt.SolidLine)
		painter.setPen(pen)
		painter.drawLine(20, 10, 250, 10)

		pen.setStyle(Qt.DashLine)
		painter.setPen(pen)
		painter.drawLine(20, 30, 250, 30)

		pen.setStyle(Qt.DashDotLine)
		painter.setPen(pen)
		painter.drawLine(20, 50, 250, 50)

		pen.setStyle(Qt.DotLine)
		painter.setPen(pen)
		painter.drawLine(20, 70, 250, 70)

		pen.setStyle(Qt.DashDotDotLine)
		painter.setPen(pen)
		painter.drawLine(20, 90, 250, 90)

		pen.setStyle(Qt.CustomDashLine)
		pen.setDashPattern([1, 4, 5, 4])
		painter.setPen(pen)
		painter.drawLine(20, 110, 250, 110)


	



if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test11()
	sys.exit(app.exec())
