#https://youtu.be/1fdGUSmcdv0?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 10. 드래그 앤 드롭

import sys

from PyQt5.QtCore import Qt, QCoreApplication, QObject, pyqtSignal, QBasicTimer, QTimerEvent, QDate, QMimeData
from PyQt5.QtGui import QPalette, QColor, QContextMenuEvent, QCloseEvent, QKeyEvent, QMouseEvent, QPixmap, QDrag, QDragEnterEvent, QDropEvent

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QSizePolicy
from PyQt5.QtWidgets import	QMessageBox, QLabel, QPushButton, QLineEdit, QTextEdit, QLCDNumber, QSlider, QInputDialog, QColorDialog, QFrame, QFontDialog, QCheckBox, QProgressBar, QCalendarWidget, QComboBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout


# 마우스 우클릭으로 버튼 위치 옮길 수 있는 버튼
class Button1(QPushButton):
	def __init__(self, title, parent):
		super().__init__(title, parent)

	def mouseMoveEvent(self, event: QMouseEvent) -> None:
		if event.buttons() != Qt.RightButton:
			return
		
		mimeData = QMimeData()
		drag = QDrag(self)
		drag.setMimeData(mimeData)
		drag.exec(Qt.MoveAction)

	def mousePressEvent(self, event: QMouseEvent) -> None:
		super().mousePressEvent(event)			# 버튼이 눌리는 효과를 보여주기 위해

		if event.button() == Qt.LeftButton:
			print('pressed')


class Button2(QPushButton):
	def __init__(self, title, parent):
		super().__init__(title, parent)
		self.setAcceptDrops(True)

	# text를 드래그한 것이 버튼 영역 위로 들어올 때 발생
	def dragEnterEvent(self, event: QDragEnterEvent) -> None:
		print("drageEnterEvent 발생")
		if event.mimeData().hasFormat('text/plain'):
			event.accept()
		else:
			event.ignore()

	# 뭔가가 Button2 위로 드랍할 때
	def dropEvent(self, event: QDropEvent) -> None:
		self.setText(event.mimeData().text())


class Test10(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

		self.resize(400, 200)
		self.setWindowTitle("Drag and Drop")
		self.show()

	def initUI(self):
		# 버튼1을 위한 코드
		self.setAcceptDrops(True)
		self.button1 = Button1('드래그앤드랍 버튼', self)
		self.button1.move(50, 50)

		# 버튼2를 위한 코드
		self.edit = QLineEdit('', self)
		self.edit.setDragEnabled(True)
		self.edit.move(50, 100)

		self.button2 = Button2("제목바꾸는 버튼", self)
		self.button2.move(250, 100)
		

	# 드래그가 시작될 때
	def dragEnterEvent(self, event: QDragEnterEvent) -> None:
		print("[QWidget] dragEnterEvent 발생")
		event.accept()

	# (앱의 아무곳이나) 드랍할 때
	def dropEvent(self, event: QDropEvent) -> None:
		
		# 이벤트 발생시킨 객체가 Button1인지 확인
		if event.source() == self.button1:
			position = event.pos()
			self.button1.move(position)
			event.accept()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test10()
	sys.exit(app.exec())
