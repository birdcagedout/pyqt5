#https://youtu.be/OIe77wIGZXY
# 04. 체크 메뉴, 컨텍스트 메뉴

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMessageBox, QMenu, qApp,
                             QPushButton, QWidget)
from PyQt5.QtGui import QContextMenuEvent, QCloseEvent

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
		menu_view = menu.addMenu("View")							# 메뉴그룹View

		menu_file_new = QMenu("New", self)							# 메뉴그룹File의 서브메뉴New
		menu_file_new_txt = QAction("텍스트 파일", self)			# 메뉴그룹File의 서브메뉴New의 메뉴액션txt
		menu_file_new_py = QAction("파이썬 파일", self)				# 메뉴그룹File의 서브메뉴New의 메뉴액션py

		menu_file_new.addAction(menu_file_new_txt)
		menu_file_new.addAction(menu_file_new_py)

		menu_file_exit = QAction("Exit", self)						# 메뉴그룹File의 서브메뉴New의 메뉴액션Exit
		menu_file_exit.setShortcut("Ctrl+X")
		menu_file_exit.setStatusTip("누르면 빠이빠이")
		menu_file_exit.triggered.connect(QCoreApplication.instance().quit)

		menu_view_status = QAction("상태표시줄", self, checkable=True)
		menu_view_status.setChecked(True)
		menu_view_status.triggered.connect(self.toggleStatus)		# 클릭했을 때 실행할 이벤트핸들러 등록
		
		menu_file.addMenu(menu_file_new)							# 메뉴그룹File의 서브메뉴New 등록
		menu_file.addAction(menu_file_exit)							# 메뉴그룹File에 메뉴액션Exit 등록
		menu_view.addAction(menu_view_status)						# 메뉴그룹View에 메뉴액션Status 등록


		
		# 윈도창 설정
		#self.setGeometry(1000, 300, 500, 200)						# 위치, 크기
		self.resize(500, 500)										# 인자는 크기. 자동으로 화면 센터에 뜬다
		self.setWindowTitle("PyQT5를 이용한 윈도")
		
		self.show()
	
	# 상태표시줄 체크박스 클릭시 이벤트 핸들러
	def toggleStatus(self, state):
		if state:
			self.statusBar().show()
		else:
			self.statusBar().hide()
	
	
	# 마우스우클릭시 컨텍스트 메뉴
	def contextMenuEvent(self, event: QContextMenuEvent) -> None:
		contextMenu = QMenu(self)
		quit = contextMenu.addAction("Quit")
		action = contextMenu.exec_(self.mapToGlobal(event.pos()))

		if action == quit:
			#qApp.quit()
			QCoreApplication.instance().quit()

	
	# 종료버튼 클릭시 오버라이드
	def closeEvent(self, event: QCloseEvent) -> None:
		response = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		
		if response == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()


app = QApplication(sys.argv)
w = Test2()
sys.exit(app.exec_())

