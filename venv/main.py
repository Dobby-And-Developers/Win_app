# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kokt0\PycharmProjects\untitled\venv\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(960, 540)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.signin = QtWidgets.QPushButton(Main)
        self.signin.setGeometry(QtCore.QRect(780, 90, 81, 31))
        self.signin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.signin.setCheckable(False)
        self.signin.setAutoRepeat(False)
        self.signin.setAutoExclusive(False)
        self.signin.setObjectName("signin")
        self.signup = QtWidgets.QPushButton(Main)
        self.signup.setGeometry(QtCore.QRect(870, 90, 81, 31))
        self.signup.setFocusPolicy(QtCore.Qt.NoFocus)
        self.signup.setAutoDefault(True)
        self.signup.setObjectName("signup")
        self.tabWidget = QtWidgets.QTabWidget(Main)
        self.tabWidget.setGeometry(QtCore.QRect(30, 110, 737, 366))

        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()

        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 721, 331))
        font = QtGui.QFont()
        font.setFamily("한컴 고딕")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()

        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 731, 341))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("한컴 고딕")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("한컴 고딕")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("한컴 고딕")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(0, 0, 1197, 540))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.signin.raise_()
        self.signup.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Main)
        self.tabWidget.setCurrentIndex(1)
        self.signin.clicked.connect(Main.push_button_clicked1)
        self.signup.clicked.connect(Main.push_button_clicked2)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "DSM-Owl"))
        self.signin.setText(_translate("Main", "로그인"))
        self.signup.setText(_translate("Main", "회원가입"))
        self.label_2.setText(_translate("Main", "공지"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Main", "공지사항"))
        self.label_3.setText(_translate("Main", "TextLabel"))
        self.label_4.setText(_translate("Main", "TextLabel"))
        self.label_5.setText(_translate("Main", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Main", "오늘의 급식"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

