# https://www.youtube.com/watch?v=OtqWefBqbxA&list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo&index=1

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMessageBox, QMenu,
                             QPushButton, QWidget)


# QWidget에서 상속 ==> QMainWindow로 변경
class Test2(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		# 버튼
		#btn = QPushButton("입력", self)
		#btn.resize(btn.sizeHint())
		#btn.setToolTip("입력버튼입니다")
		#btn.move(50, 50)
		#btn.clicked.connect(QCoreApplication.instance().quit)		# 이벤트 처리

		# 상태바
		self.statusBar()
		self.statusBar().showMessage("상태바")

		# 메뉴
		menu = self.menuBar()										# 메뉴 생성
		menu_file = menu.addMenu("File")							# 메뉴그룹File
		menu_edit = menu.addMenu("Edit")							# 메뉴그룹Edit

		menu_file_new = QMenu("New", self)							# 메뉴그룹File의 서브메뉴New
		menu_file_new_txt = QAction("텍스트 파일", self)			# 메뉴그룹File의 서브메뉴New의 메뉴액션TXT
		menu_file_new_py = QAction("파이썬 파일", self)				# 메뉴그룹File의 서브메뉴New의 메뉴액션PY
		menu_file_new.addAction(menu_file_new_txt)
		menu_file_new.addAction(menu_file_new_py)

		menu_file_exit = QAction("Exit", self)						# 메뉴그룹File의 서브메뉴New의 메뉴액션EXIT
		menu_file_exit.setShortcut("Ctrl+X")
		menu_file_exit.setStatusTip("누르면 빠이빠이")
		
		menu_file.addMenu(menu_file_new)							# 메뉴그룹File의 서브메뉴New 등록
		menu_file.addAction(menu_file_exit)							# 메뉴그룹File에 메뉴액션Exit 등록



		
		# 윈도창 설정
		#self.setGeometry(1000, 300, 500, 200)						# 위치, 크기
		self.resize(500, 500)										# 인자는 크기, 자동으로 화면 센터에 뜬다
		self.setWindowTitle("PyQT5를 이용한 윈도")
		
		self.show()
	
	# 종료버튼 클릭시 오버라이드
	def closeEvent(self, QCloseEvent) -> None:
		response = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		
		if response == QMessageBox.Yes:
			QCloseEvent.accept()
		else:
			QCloseEvent.ignore()

app = QApplication(sys.argv)
w = Test2()
sys.exit(app.exec_())

