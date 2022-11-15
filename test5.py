#https://youtu.be/O1PnaVwuZiA?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo
# 05. 레이아웃

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QTextEdit, QAction, QMessageBox, QMenu
from PyQt5.QtGui import QContextMenuEvent, QCloseEvent

# QWidget에서 상속 ==> QMainWindow로 변경
class Test5(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		# 1. Label 레이아웃
		#label1 = QLabel('ZetCode', self)
		#label1.move(15, 10)
		#label2 = QLabel('tutorial', self)
		#label2.move(35, 40)
		#label3 = QLabel('for programmers', self)
		#label3.move(55, 70)

		
		# 2. 버튼과 QHBoxLayout, QVBoxLayout + stretch
		#okButton = QPushButton("OK")
		#cancelButton = QPushButton("CANCEL")

		#hBox = QHBoxLayout()
		#hBox.addStretch(1)
		#hBox.addWidget(okButton)
		#hBox.addWidget(cancelButton)

		#vBox = QVBoxLayout()
		#vBox.addStretch(1)
		#vBox.addLayout(hBox)

		#self.setLayout(vBox)


		# 3. 그리드
		#grid = QGridLayout()
		#self.setLayout(grid)

		#names = [ 'Cls', 'Bck', '', 'Close',
		#			'7', '8', '9', '/',
		#			'4', '5', '6', '*',
		#			'1', '2', '3', '-',
		#			'0', '.', '=', '+'
		#		]
		#positions = [(i, j) for i in range(5) for j in range(4)]

		#for position, name in zip(positions, names):

		#	if name == '':
		#		continue

		#	button = QPushButton(name)
		#	grid.addWidget(button, *position)		# position이 (0, 1)인 경우: grid.addWidget(button, 0, 1)이 됨


		# 4. 레이아웃 총정리
		title = QLabel("Title")
		author = QLabel("Author")
		review = QLabel("Review")

		titleEdit = QLineEdit()
		authorEdit = QLineEdit()
		reviewEdit = QTextEdit()				# review만 multiline(높이 3배)

		grid = QGridLayout()
		grid.setSpacing(10)						# Label과 LineEdit 사이, Label과 Label 사이 둘다 10

		grid.addWidget(title, 1, 0)
		grid.addWidget(titleEdit, 1, 1)

		grid.addWidget(author, 2, 0)
		grid.addWidget(authorEdit, 2, 1)

		grid.addWidget(review, 3, 0)
		grid.addWidget(reviewEdit, 3, 1, 5, 1)

		self.setLayout(grid)

		self.resize(300, 150)
		self.setWindowTitle("Absolute")
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Test5()
	sys.exit(app.exec_())

