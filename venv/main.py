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
        Main.resize(960, 542)
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
        self.tabWidget.setGeometry(QtCore.QRect(30, 110, 731, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1199, 542))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView_1 = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.listView_1.setObjectName("listView_1")
        self.horizontalLayout.addWidget(self.listView_1)
        self.listView_2 = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.listView_2.setObjectName("listView_2")
        self.horizontalLayout.addWidget(self.listView_2)
        self.listView_3 = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.listView_3.setObjectName("listView_3")
        self.horizontalLayout.addWidget(self.listView_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(0, 0, 960, 540))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Main", "공지사항"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Main", "오늘의 급식"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

