# https://www.youtube.com/watch?v=OtqWefBqbxA&list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo&index=1

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication


class Test1(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		# 버튼
		btn = QPushButton("입력", self)
		btn.resize(btn.sizeHint())
		btn.setToolTip("입력버튼입니다")
		btn.move(50, 50)
		btn.clicked.connect(QCoreApplication.instance().quit)		# 이벤트 처리

		
		# 윈도창 설정
		#self.setGeometry(1000, 300, 500, 200)						# 위치, 크기
		self.resize(500, 500)										# 인자는 크기, 자동으로 화면 센터에 뜬다
		self.setWindowTitle("PyQT5를 이용한 윈도")
		
		self.show()
	
	def closeEvent(self, QCloseEvent) -> None:
		response = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		
		if response == QMessageBox.Yes:
			QCloseEvent.accept()
		else:
			QCloseEvent.ignore()

app = QApplication(sys.argv)
w = Test1()
sys.exit(app.exec_())

