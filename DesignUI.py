# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(392, 330)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(90, 40, 150, 21))
		font = QtGui.QFont()
		font.setFamily("맑은 고딕")
		font.setPointSize(10)
		self.lineEdit.setFont(font)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(90, 80, 150, 21))
		font = QtGui.QFont()
		font.setFamily("맑은 고딕")
		font.setPointSize(10)
		self.lineEdit_2.setFont(font)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_3.setGeometry(QtCore.QRect(90, 130, 150, 21))
		font = QtGui.QFont()
		font.setFamily("맑은 고딕")
		font.setPointSize(10)
		self.lineEdit_3.setFont(font)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_4.setGeometry(QtCore.QRect(90, 170, 150, 21))
		font = QtGui.QFont()
		font.setFamily("맑은 고딕")
		font.setPointSize(10)
		self.lineEdit_4.setFont(font)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(70, 220, 111, 51))
		font = QtGui.QFont()
		font.setFamily("맑은 고딕")
		font.setPointSize(10)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(200, 220, 111, 51))
		font = QtGui.QFont()
		font.setFamily("맑은 고딕")
		font.setPointSize(10)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setObjectName("pushButton_2")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 26))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.pushButton.clicked.connect(MainWindow.start)
		self.pushButton_2.clicked.connect(MainWindow.stop)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "시작"))
		self.pushButton_2.setText(_translate("MainWindow", "중지"))
	
	def start(self):
		print(f"[시작 버튼 눌림] event:")

	def stop(self):
		print(f"[중지 버튼 눌림] Event:")



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

