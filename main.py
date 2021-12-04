#CSCE 3550 Project 1 - 11279325 - Enock Omweno
#Description: In this project I created a 2-Factor authenctaion login form for a users account
import sys
import random
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QInputDialog
import sqlite3
import hashlib
from twilio.rest import Client
from cryptography.fernet import Fernet
import base64

key= Fernet.generate_key() # this is the randomly generated key for the prpject
fernet = Fernet(key)



class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("WelcomeScreen.ui", self)
        self.login.clicked.connect(self.loginButton)# this connects to the login in button on the welcome screen
        self.createA.clicked.connect(self.createAccount)# this connects to the create account button on the welcome screen

    def loginButton(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def createAccount(self):
        createA = CreateAccount()
        widget.addWidget(createA)
        widget.setCurrentIndex(widget.currentIndex()+1)



#pinNumber = "55443"

#pinNumber = ''.join(random.choice("0123456789") for i in range(5))


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("LoginScreen.ui", self)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password) # this hides the password
        self.login.clicked.connect(self.loginF) # to give the login function functionality
        self.back.clicked.connect(self.backButton)# this is the home button on the Login Screen




    def backButton(self):
        back = WelcomeScreen()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def loginButton(self):
        login = SuccessScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def loginF(self): #this is the login function
        user = self.username.text() # this connects to teh username text edit field
        password = self.Password.text() # this connects to the password text edit field
        password2 = hashlib.sha256(self.Password.text().encode()).hexdigest()


        if user == 0 or len(password) == 0:
            self.errorMessege.setText("Missing input")

        else:
            test=hashlib.sha256((password.encode())).hexdigest()
            print(test)
            conn = sqlite3.connect("Project1_Database.db")
            cur = conn.cursor()
            query = 'SELECT password FROM Login WHERE username =\''+user+"\'"
            cur.execute(query)
            database_password = cur.fetchone()[0]
            if database_password == test:
                print("Success")
                conn = sqlite3.connect("Project1_Database.db")
                cur = conn.cursor()
                query2 = 'SELECT Phone FROM Login WHERE username =\'' + user + "\'"
                cur.execute(query2)
                database_phoneNumber = cur.fetchone()[0]
                print(database_phoneNumber)

                query4 = 'SELECT key FROM Login WHERE username =\'' + user + "\'"
                cur.execute(query4)
                database_key = cur.fetchone()[0]

                fernet2 = Fernet(database_key)

                phone = fernet2.decrypt(database_phoneNumber).decode()
                print("HEYYYYY" + phone)
                pinNumber = ''.join(random.choice("0123456789") for i in range(5))
                account_sid = "AC04adf203e52a81862544c11ab651f2e4"
                auth_token = "6bbf876a2479139ea0d41a8c81b12bc1"
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body='Please verify your account by entering this code: ' + pinNumber,
                    from_='+16822282907',
                    to=phone
                )

                print(message.sid)
                text, ok = QInputDialog.getText(self, 'Sample', 'Enter pin')
                if (text == pinNumber):
                    print("The pins match")
                    login = SuccessScreen()
                    widget.addWidget(login)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                else:
                    text, ok = QInputDialog.getText(self, 'Sample', 'Enter a valid pin')
                    print("The pins you enter do not match")
                    if (text == pinNumber):

                        login = SuccessScreen()
                        widget.addWidget(login)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                 self.errorMessege.setText("Invalid username or password ")

        # conn = sqlite3.connect("Project1_Database.db")
        # cur = conn.cursor()
        # query2 = 'SELECT Phone FROM Login WHERE username =\'' + user + "\'"
        # cur.execute(query2)
        # result_phoneNumber = cur.fetchone()
        # print(result_phoneNumber)
        #
        # query2 = 'SELECT key FROM Login WHERE username =\'' + user + "\'"
        # cur.execute(query2)
        # result_key = cur.fetchmany()[0]
        #
        # fernet2 = Fernet(result_key)
        #
        # phone = fernet2.decrypt(result_phoneNumber).decode()
        # print("HEYYYYY"+phone)
        #
        # account_sid = "AC04adf203e52a81862544c11ab651f2e4"
        # auth_token = "6bbf876a2479139ea0d41a8c81b12bc1"
        # client = Client(account_sid, auth_token)
        #
        #
        # message = client.messages.create(
        #      body='Hey verify your account by entering this code: ' + pinNumber,
        #      from_='+16822282907',
        #      to=phone
        # )
        #
        #
        # print(message.sid)

        # text, ok = QInputDialog.getText(self, 'Sample', 'Enter pin')
        # if(text == pinNumber):
        #     print("The pins match")
        # else:
        #     text, ok = QInputDialog.getText(self, 'Sample', 'Enter pin a valid Pin')
        #     print("The pins you enter do not match")




class CreateAccount(QDialog):
    def __init__(self):
        super(CreateAccount,self).__init__()
        loadUi("CreateAccount.ui", self)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)# this hides the password
        self.confirmPass.setEchoMode(QtWidgets.QLineEdit.Password)# this hides the password when you are confirming ti
        self.Signup.clicked.connect(self.SignupF) # this connects to the sign up button on the create account screen
        self.home.clicked.connect(self.homeButton)# this connects to teh home button on the create account screen

    def homeButton(self):
        home = WelcomeScreen()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def SignupF(self):
        user = self.username.text()
        password = hashlib.sha256(self.Password.text().encode()).hexdigest()
        confirmPassword = hashlib.sha256(self.confirmPass.text().encode()).hexdigest()
        phoneNumber = fernet.encrypt(self.phonenumber.text().encode())

        conn = sqlite3.connect("Project1_Database.db")
        cur = conn.cursor()
        query2 = 'SELECT username FROM Login WHERE username =\''+user+"\'"
        cur.execute(query2)
        database_username = cur.fetchone()
        print("This is a TEST")
        print(database_username)


        if database_username is not None:
            self.errorMessege.setText("Username already exist")

        elif len(user) == 0 or len(password) == 0 or len(confirmPassword) == 0 or len(phoneNumber) == 0:
            self.errorMessege.setText("Missing inputs")
        elif password!=confirmPassword :
            self.errorMessege.setText("Your passwords do not match")

        else:
            conn = sqlite3.connect("Project1_Database.db")
            cur = conn.cursor()
            usersInformation = [user, password,phoneNumber,key]
            cur.execute('INSERT INTO Login(username,password,Phone,key)VALUES (?,?,?,?)',usersInformation)
            conn.commit()
            conn.close()

            login = LoginScreen()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)




class SuccessScreen(QDialog):
    def __init__(self):
        super(SuccessScreen, self).__init__()
        loadUi("SuccessScreen.ui", self)
        self.Logout.clicked.connect(self.logoutButton) # this connects to the logout button on the SuccessScreen


    def logoutButton(self): # this gives the logout  button functionality
        Logout = WelcomeScreen()
        widget.addWidget(Logout)
        widget.setCurrentIndex(widget.currentIndex() + 1)


#main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.show()
try:
     sys.exit(app.exec())
except:
    print("Exiting")