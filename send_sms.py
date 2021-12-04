# class LoginScreen(QDialog):
#     def __init__(self):
#         super(LoginScreen, self).__init__()
#         loadUi("LoginScreen.ui", self)
#         self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.login.clicked.connect(self.loginF) # to give the login function functionality
#         self.back.clicked.connect(self.backButton)
#         self.login.clicked.connect(self.loginButton)
#
#
#     def backButton(self):
#         back = WelcomeScreen()
#         widget.addWidget(back)
#         widget.setCurrentIndex(widget.currentIndex() + 1)
#
#     def loginButton(self):
#         login = SuccessScreen()
#         widget.addWidget(login)
#         widget.setCurrentIndex(widget.currentIndex() + 1)
#
#
#     def loginF(self): #this is the login function
#         user = self.username.text()
#         password = hashlib.sha256(self.Password.text().encode()).hexdigest()
#
#
#         if user == 0 or len(password) == 0:
#             self.errorMessege.setText("Missing input")
#
#         else:
#             conn = sqlite3.connect("Project1_Database.db")
#             cur = conn.cursor()
#             query = 'SELECT password FROM Login WHERE username =\''+user+"\'"
#             cur.execute(query)
#             result_password = cur.fetchone()[0]
#             if result_password == password:
#                 print("Success")
#                 text, ok = QInputDialog.getText(self, 'Sample', 'Enter pin')
#                 if (text == pinNumber):
#                     print("The pins match")
#                 else:
#                     text, ok = QInputDialog.getText(self, 'Sample', 'Enter pin a valid Pin')
#                     print("The pins you enter do not match")
#             else:
#                self.errorMessege.setText("Invalid username or password ")
#
#         conn = sqlite3.connect("Project1_Database.db")
#         cur = conn.cursor()
#         query2 = 'SELECT Phone FROM Login WHERE username =\'' + user + "\'"
#         cur.execute(query2)
#         result_phoneNumber = cur.fetchone()[0]
#         print(result_phoneNumber)
#
#         query4 = 'SELECT key FROM Login WHERE username =\'' + user + "\'"
#         cur.execute(query4)
#         result_key = cur.fetchone()[0]
#
#         fernet2 = Fernet(result_key)
#
#         phone = fernet2.decrypt(result_phoneNumber).decode()
#         print("HEYYYYY"+phone)
#
#         account_sid = "AC04adf203e52a81862544c11ab651f2e4"
#         auth_token = "6bbf876a2479139ea0d41a8c81b12bc1"
#         client = Client(account_sid, auth_token)
#         # print(text,number)
#         message = client.messages.create(
#             body='Hey verify your account by entering this code: ' + pinNumber,
#             from_='+16822282907',
#             to=phone
#         )
#
#
#         print(message.sid)
