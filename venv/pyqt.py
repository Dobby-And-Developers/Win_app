import sys
import smtplib
import pymysql
import random as r
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
main_class = uic.loadUiType('main.ui')[0]
login_class = uic.loadUiType('login.ui')[0]
signup_class = uic.loadUiType('signup.ui')[0]


class SignInDialog(QDialog, login_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.id = None
        self.password = None

    def push_button_clicked(self):
        self.id = self.lineEdit_2.text()
        self.password = self.lineEdit_3.text()
        self.close()


class SignUpDialog(QDialog, signup_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def checking_mail(self):
        self.email = self.lineEdit_2.text()
        print(self.email)
        TO = self.email
        SUBJECT = 'DSM Owl Email Check number.'
        TEXT = str(r.randint(100000, 999999))
        # TEXT = str(123456)
        self._number = TEXT

        gmail_sender = ''
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
            self.label.setText('이메일주소를 확인해주세요.')

        else:
            self.lineEdit.setDisabled(True)
            self.lineEdit_2.setDisabled(True)
            self.pushButton.setDisabled(True)
            self.lineEdit_3.setDisabled(False)
            self.pushButton_2.setDisabled(False)

        server.quit()

    def checking_num(self):
        self.number = self.lineEdit_3.text()
        if self.number == self._number:
            print(self.number)
            self.lineEdit_3.setDisabled(True)
            self.pushButton_2.setDisabled(True)
            self.lineEdit_4.setDisabled(False)
            self.pushButton_3.setDisabled(False)

        else:
            print('Wrong Num')
            self.label.setText('인증번호가 잘못되었습니다.')


    def checking_id(self):
        self.id = self.lineEdit_4.text()
        print(self.id)
        self.lineEdit_4.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.lineEdit_5.setDisabled(False)
        self.lineEdit_6.setDisabled(False)
        self.pushButton_4.setDisabled(False)
        self.pushButton_5.setDisabled(False)

    def checking_pw(self):
        self.password = self.lineEdit_5.text()
        self._password = self.lineEdit_6.text()
        if self.password == self._password:
            self.lineEdit_5.setDisabled(True)
            self.lineEdit_6.setDisabled(True)
            self.pushButton_4.setDisabled(True)

        else:
            print('check your pw')

    def signup(self):
        self.pushButton_5.setDisabled(True)
        print('회원가입성공')

        self.name = self.lineEdit.text()
        self.email = self.lineEdit_2.text()
        self.id = self.lineEdit_4.text()
        self.password = self.lineEdit_5.text()
        self.close()


class MyWindow(QWidget, main_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def push_button_clicked1(self):
        self.hide()
        dlg1 = SignInDialog()
        dlg1.exec_()
        self.show()
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
    import sys
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
