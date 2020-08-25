import sys
import smtplib
import pymysql
import random as r
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SignInDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        self.id = None
        self.password = None

    def setup_ui(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("로그인")
        self.setWindowIcon(QIcon('icon.jpg'))
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("login.jpg")))
        self.setPalette(palette)

        label1 = QLabel("아이디 : ")
        label2 = QLabel("비밀번호 : ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setEchoMode(QLineEdit.Password)
        self.pushButton1= QPushButton("로그인")
        self.pushButton1.clicked.connect(self.push_button_clicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        self.setLayout(layout)

    def push_button_clicked(self):
        self.id = self.lineEdit1.text()
        self.password = self.lineEdit2.text()
        self.close()


class SignUpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        self.name = None
        self.email = None
        self.id = None
        self.password = None
        self.number = None
        self._number = None

    def setup_ui(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("회원가입")
        self.setWindowIcon(QIcon('icon.jpg'))
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("login.jpg")))
        self.setPalette(palette)

        label1 = QLabel("이  름 : ")
        label2 = QLabel("이메일 : ")
        label3 = QLabel("인증번호 :")
        label4 = QLabel("아이디 : ")
        label5 = QLabel("비밀번호 : ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit5.setEchoMode(QLineEdit.Password)

        self.pushButton1 = QPushButton("중복확인")
        self.pushButton2 = QPushButton("회원가입")
        self.pushButton3 = QPushButton("메일인증")
        self.pushButton4 = QPushButton("확인")

        self.pushButton1.clicked.connect(self.checking_id)
        self.pushButton2.clicked.connect(self.push_button_clicked)
        self.pushButton3.clicked.connect(self.checking_mail)
        self.pushButton4.clicked.connect(self.checked_num)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(self.pushButton3, 1, 2)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.lineEdit3, 2, 1)
        layout.addWidget(self.pushButton4, 2, 2)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.lineEdit4, 3, 1)
        layout.addWidget(self.pushButton1, 3, 2)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.lineEdit5, 4, 1)
        layout.addWidget(self.pushButton2, 5, 2)

        self.setLayout(layout)

    def checked_num(self):
        self.number = self.lineEdit3.text()
        if self.number == self._number:
            print(self.number)

        else:
            print('Wrong Num')

    def checking_mail(self):
        self.email = self.lineEdit2.text()
        print(self.email)
        TO = self.email
        SUBJECT = 'DSM Owl Email Check number.'
        TEXT = str(r.randint(100000, 999999))
        self._number = TEXT

        gmail_sender = 'manitto719@gmail.com'
        gmail_passwd = ''

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)
        BODY = '\r\n'.join([f'To: {TO}',
                            f'From: {gmail_sender}',
                            f'Subject: {SUBJECT}',
                            '' + TEXT])

        try:
            server.sendmail(gmail_sender, [TO], BODY)
            print('email sent')

        except:
            print('error sending mail')

        server.quit()

    def checking_id(self):
        self.id = self.lineEdit4.text()
        print(self.id)
        # self.close()
        # self.id = self.lineEdit1.text()

    def push_button_clicked(self):

        self.name = self.lineEdit1.text()
        self.email = self.lineEdit2.text()
        self.id = self.lineEdit4.text()
        self.password = self.lineEdit5.text()
        conn = pymysql.connect(host='localhost', user='root', password='',
                               db='user_info', charset='utf8')

        curs = conn.cursor()
        sql = """insert into user(name, email, id, pw) values (%s, %s, %s, %s)"""
        curs.execute(sql, (f'{self.name}', f'{self.email}', f'{self.id}', f'{self.password}'))
        conn.commit()

        conn.close()

        self.close()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.date = QDate.currentDate()
        self.setup_ui()

    def setup_ui(self):
        self.setGeometry(800, 200, 960, 540)
        self.setWindowTitle("Our Weed Life")
        self.setWindowIcon(QIcon('icon.jpg'))
        # self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        # test background
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("background.jpg")))
        self.setPalette(palette)
        self.pushButton1 = QPushButton("Sign In")
        self.pushButton2 = QPushButton("Sign Up")
        self.pushButton1.clicked.connect(self.push_button_clicked1)
        self.pushButton2.clicked.connect(self.push_button_clicked2)

        layout = QHBoxLayout()
        layout.addStretch(11)
        layout.addWidget(self.pushButton1)
        layout.addWidget(self.pushButton2)

        _layout = QVBoxLayout()
        _layout.addStretch(1)
        _layout.addLayout(layout)
        _layout.addStretch(4)

        self.setLayout(_layout)

    def push_button_clicked1(self):
        dlg1 = SignInDialog()
        dlg1.exec_()
        _id = dlg1.id
        _pw = dlg1.password
        print(f"id : {_id} pw : {_pw}")

    def push_button_clicked2(self):
        dlg2 = SignUpDialog()
        dlg2.exec_()
        _name = dlg2.name
        _email = dlg2.email
        _id = dlg2.id
        _pw = dlg2.password
        print(f"name : {_name} email : {_email} id : {_id} pw : {_pw}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
