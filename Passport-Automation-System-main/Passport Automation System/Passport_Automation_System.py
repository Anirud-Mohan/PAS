import random
import smtplib
import sys
import os
import icons_rc
from PyQt5 import Qt, QtWidgets, QtCore, QtGui 
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import  QDialog, QApplication, QMessageBox, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip,QFileDialog
from PyQt5.uic import loadUi

import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(
    user='TfX135h0Id', 
    password='Rjr5w2G9hx',
    host='remotemysql.com',
    database='TfX135h0Id')
cursor = conn.cursor()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("mainwindowui.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        title = "PASSPORT AUTOMATION UI"
        self.setWindowTitle(title)
        QSizeGrip(self.size_grip)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.centralwidget.setGraphicsEffect(self.shadow)
        self.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.close_window_button.clicked.connect(lambda: self.close())
        #self.exit_button.clicked.connect(lambda: self.close())
        self.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
        self.user_btn.clicked.connect(self.gotocreate_login)
        #self.registerbtn.clicked.connect(self.gotocreate_register)
        #self.paymentbtn.clicked.connect(self.gotocreate_payment)
        self.loginbtn.clicked.connect(self.gotocreate_login)
        self.signupbtn.clicked.connect(self.gotocreate)
        self.forgotpasswordbtn.clicked.connect(self.gotocreate_forgotpwd)
        self.show()
        


        def moveWindow(e):  
            if self.isMaximized() == False: 
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.header_frame.mouseMoveEvent = moveWindow
        self.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())


        self.show()

    def slideLeftMenu(self):
        
        width = self.slide_menu_container.width()

        
        if width == 0:
            
            newWidth = 350
            self.open_close_side_bar_btn.setIcon(QtGui.QIcon(r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python39\My Programs\Passport Automation System\icons\chevron-left.svg"))
        
        else:
            
            newWidth = 0
            self.open_close_side_bar_btn.setIcon(QtGui.QIcon(r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python39\My Programs\Passport Automation System\icons\align-left.svg"))

        
        self.animation = QPropertyAnimation(self.slide_menu_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def restore_or_maximize_window(self):
        
        if self.isMaximized():
            self.showNormal()
            self.restore_window_button.setIcon(QtGui.QIcon(r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python39\My Programs\Passport Automation System\icons\maximize-2.svg"))
        else:
            self.showMaximized()
            self.restore_window_button.setIcon(QtGui.QIcon(r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python39\My Programs\Passport Automation System\icons\minimize-2.svg"))

    def gotocreate_login(self):
         login=Login()
         widget.addWidget(login)
         widget.setCurrentIndex(widget.currentIndex()+1)
 

    def gotocreate_forgotpwd(self):
         forgotpwd=Otp()
         widget.addWidget(forgotpwd)
         widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        signup=Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)


    

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.loginbutton.clicked.connect(self.loginfunction)
        self.signup.clicked.connect(self.gotocreate)
        self.forgotpwdbutton.clicked.connect(self.gotocreate_otp)
        self.homebtn.clicked.connect(self.gotocreate_main)
    
        
    
    def loginfunction(self):
        username= self.username.text()
        password= self.password.text()
        cursor.execute("SELECT username,password from user where username like '"+username + "'and password like '"+password+"'")
        result = cursor.fetchone()
        if result == None:
            QMessageBox.critical(self,"","wrong username or password,Please try again !!")
            print("username not in database or username and password does not match")
            print("Please sign up first")
        else:
            QMessageBox.information(self," ","Successfully logged-in ")
            print(self," ","Successfully logged in as: ",username,"and password: ",password)
            #self.loginbutton.pressed.connect(self.gotocreate_user)
            self.gotocreate_user()
            
    def gotocreate(self):
        signup=Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_otp(self):
        forgotpwdbutton=Otp()
        widget.addWidget(forgotpwdbutton)
        widget.setCurrentIndex(widget.currentIndex()+1) 

    def gotocreate_user(self):
        userwindow=UserWindow()
        widget.addWidget(userwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_main(self):
        mainwindow=MainWindow() 
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_register(self):
         register=Register()
         widget.addWidget(register)
         widget.setCurrentIndex(widget.currentIndex()+1)

class Signup(QDialog):
    def __init__(self):
        super(Signup,self).__init__()
        loadUi("signup.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.signupbutton.clicked.connect(self.signupfunction)
        self.login.clicked.connect(self.gotocreate_login)
        self.homebtn.clicked.connect(self.gotocreate_main)

    def signupfunction(self):
        email=self.email.text()
        mobileno=self.mobileno.text()
        username_3=self.username_3.text()
        password=self.password.text()
        confirmpass=self.confirmpass.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            sql = """INSERT INTO user(email, mobileno, username, password, confirm_password)VALUES (%s, %s, %s, %s, %s)"""
            data=(email,mobileno,username_3,password,confirmpass)
            try:
                cursor.execute(sql,data)
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close()

            QMessageBox.information(self," ","Account created successfully")
            print(self," ","Successfully created account with email: ",email,"and password: ", password)
            
               
        else:
            QMessageBox.critical(self," ","Password does not match")

    def gotocreate_login(self):
         login=Login()
         widget.addWidget(login)
         widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_main(self):
        mainwindow=MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Otp(QDialog):
    def __init__(self):
        super(Otp,self).__init__()
        loadUi("otp.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.sendotp.clicked.connect(self.sendfunction)
        self.verifyotp.clicked.connect(self.verifyfunction)
        self.cancelotp.clicked.connect(self.gotocreate_login)
        self.homebtn.clicked.connect(self.gotocreate_login)
  
   
    def sendfunction(self):
     global otp
     try:    
         emailid=self.emailid.text()
         s = smtplib.SMTP("smtp.gmail.com",587)
         s.starttls()
         s.login("projecti2001work@gmail.com" , "ProjectWork2001")
         otp = random.randint(1000,9999)
         otp = str(otp)
         s.sendmail("projecti2001work@gmail.com" ,emailid , otp)
         if len(emailid) and len(otp) > 0:
             QMessageBox.information(self,"OTP","OTP sent successfully")
             print(self,"OTP","OTP sent successfully to ",emailid)
             s.quit()
         else:
             QMessageBox.critical(self," ","Fields cant be empty")
     except Exception as e:
         QMessageBox.critical(self,"OTP","Please enter vaild mail address or check the internet connection")
         print(e)

    def verifyfunction(self):
        otpno=self.otpno.text()
        if otp == otpno:
            QMessageBox.information(self,"OTP","Success")
            #self.verifyotp.pressed.connect(self.gotocreate_forgotpwd)
            self.gotocreate_forgotpwd()
        else:
            QMessageBox.critical(self,"OTP","Failed")
    
    def gotocreate_login(self):
         login=MainWindow()
         widget.addWidget(login)
         widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_forgotpwd(self):
         forgotpwd=Forgotpassword()
         widget.addWidget(forgotpwd)
         widget.setCurrentIndex(widget.currentIndex()+1)

class Forgotpassword(QDialog):
    def __init__(self):
        super(Forgotpassword,self).__init__()
        loadUi("forgotpassword.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.cancelpwd.clicked.connect(self.gotocreate_login)
        self.signpwd.clicked.connect(self.forgotpwdfunction)
        self.homebtn.clicked.connect(self.gotocreate_login)
    

    def forgotpwdfunction(self): 
        password=self.newpwd.text()
        confirm_password=self.confirmnewpwd.text()
        email=self.email.text()
        if len(password) and len(confirm_password) and len(email)> 0:
            if password == confirm_password:
                try:
                    sql = "UPDATE  user SET password =%s , confirm_password= %s WHERE email=%s "
                    data=(password,confirm_password,email)
                    cursor.execute(sql,data)
                    conn.commit()
                    QMessageBox.information(self," ","Successfully changed password")
                    #self.signpwd.clicked.connect(self.gotocreate_login)
                except Exception as e:
                    print(e)
                    conn.rollback()
                    conn.close()
                    QMessageBox.critical(self," ","Failed changed password")

                
            else:
                QMessageBox.critical(self," ","Password does not match")
        else:
            QMessageBox.critical(self," ","Fields cant be empty")


    def gotocreate_login(self):
         login=Login()
         widget.addWidget(login)
         widget.setCurrentIndex(widget.currentIndex()+1)
class Register(QDialog):
    def __init__(self):
        super(Register,self).__init__()
        loadUi("register.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.register_2.clicked.connect(self.registerfunction)
        self.cancelregi.clicked.connect(self.gotocreate_user)
        self.homebtn.clicked.connect(self.gotocreate_user)

    def registerfunction(self):
        fname=self.fname.text()
        lname=self.lname.text()
        username=self.username.text()
        dob=self.dob.text()
        gender=self.gender.text()
        mobileno=self.mobileno.text()
        email=self.email.text()
        nationality=self.nationality.text()
        martialstatus=self.martialstatus.text() 
        aadhar=self.aadhar.text()
        pan=self.pan.text()
        driving=self.driving.text()
        _10mark=self._10mark.text()
        _12mark=self._12mark.text()
        if len(fname) and len(lname) and len(mobileno) and len(username) and len(email) and len(nationality) and len(martialstatus) and len(aadhar) and len(pan) and len(driving) and len(_10mark) and len(_12mark) > 0 :
            sql = """INSERT INTO user_register(fname,lname,username,dob,gender,mobileno,email,nationality,martialstatus,aadhar,pan,driving,_10mark,_12mark,checkstatus)VALUES (%s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s, %s, %s, %s,%s)"""
            data=(fname,lname,username,dob,gender,mobileno,email,nationality,martialstatus,aadhar,pan,driving,_10mark,_12mark,'Not Verified')
            try:
                cursor.execute(sql,data)
                conn.commit()
                QMessageBox.information(self," ","Registered successfully")
                #self.register_2.pressed.connect(self.gotocreate_payment)
                self.gotocreate_payment()
            except Exception as e:
                print(e)
                QMessageBox.critical(self," ","Registered Failed")
                conn.rollback()
                conn.close()
        else:
            QMessageBox.critical(self," ","Fields cant be empty")

    def gotocreate_payment(self):
         payment=Payment()
         widget.addWidget(payment)
         widget.setCurrentIndex(widget.currentIndex()+1)


    def gotocreate_user(self):
        userwindow=UserWindow()
        widget.addWidget(userwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Payment(QDialog):
    def __init__(self):
        super(Payment,self).__init__()
        loadUi("payment.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.card.clicked.connect(self.gotocreate_card)
        self.upi.clicked.connect(self.gotocreate_upi)
        self.homebtn.clicked.connect(self.gotocreate_user)

    def gotocreate_user(self):
        userwindow=UserWindow()
        widget.addWidget(userwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_card(self):
        cardpayment=CardPayment()
        widget.addWidget(cardpayment)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_upi(self):
        upipayment=UpiPayment()
        widget.addWidget(upipayment)
        widget.setCurrentIndex(widget.currentIndex()+1)


class CardPayment(QDialog):
    def __init__(self):
        super(CardPayment,self).__init__()
        loadUi("cardpayment.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.verifybtn.clicked.connect(self.gotocreate_payment)
        

    def gotocreate_payment(self):
        fname=self.fname.text()
        email=self.email.text()
        dob=self.dob.text()
        gender=self.gender.text()
        card_num=self.card_num.text()
        card_cvc=self.card_cvc.text()
        expdate=self.expdate.text()

        if len(fname) and len(email) and len(dob) and len(gender) and len(card_num) and len(card_cvc) and len(expdate) > 0:
            QMessageBox.information(self," ","Payment Successfull")
            #self.verifybtn.pressed.connect(self.gotocreate_user)
            self.gotocreate_user()
            
        else:
            QMessageBox.critical(self," ","Fields Cannot Be Empty")  

    def gotocreate_user(self):
        userwindow=UserWindow()
        widget.addWidget(userwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class UpiPayment(QDialog):
    def __init__(self):
        super(UpiPayment,self).__init__()
        loadUi("upipayment.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.verifybtn.clicked.connect(self.gotocreate_payment)
        

    def gotocreate_payment(self):
        fname=self.fname.text()
        email=self.email.text()
        dob=self.dob.text()
        gender=self.gender.text()
        upi_id=self.upi_id.text()

        if len(fname) and len(email) and len(dob) and len(gender) and len(upi_id) > 0:
            QMessageBox.information(self," ","Payment Successfull")
            #self.verifybtn.pressed.connect(self.gotocreate_user)
            self.gotocreate_user()
        else:
            QMessageBox.critical(self," ","Fields Cannot Be Empty")

    def gotocreate_user(self):
        userwindow=UserWindow()
        widget.addWidget(userwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Status(QDialog):
    def __init__(self):
        super(Status,self).__init__()
        loadUi("status.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.homebtn.clicked.connect(self.gotocreate_user)
        self.checkbtn.clicked.connect(self.statusfunction)


    def statusfunction(self):
        username=self.username.text()
        email=self.email.text()
        sql="""SELECT checkstatus from user_register WHERE username= %s and email= %s"""
        data=(username,email)
        cursor.execute(sql,data)
        result = cursor.fetchone()
        if result == None:
            QMessageBox.critical(self,"","wrong username or email,Please try again !!")
            print("username not in database or username and email does not match")
        else:
            print(result)
            self.status_label.setText(result[0])

    def gotocreate_user(self):
        userwindow=UserWindow()
        widget.addWidget(userwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class UserWindow(QMainWindow):
    def __init__(self):
        super(UserWindow,self).__init__()
        loadUi("userwindowui.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        title = "PASSPORT AUTOMATION UI"
        self.setWindowTitle(title)
        QSizeGrip(self.size_grip)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.centralwidget.setGraphicsEffect(self.shadow)
        self.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.close_window_button.clicked.connect(lambda: self.close())
        #self.exit_button.clicked.connect(lambda: self.close())
        self.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
        self.user_btn.clicked.connect(self.gotocreate_login)
        self.registerbtn.clicked.connect(self.gotocreate_register)
        self.paymentbtn.clicked.connect(self.gotocreate_payment)
        self.checkstatusbtn.clicked.connect(self.gotocreate_status)
        self.show()
        


        def moveWindow(e):  
            if self.isMaximized() == False: 
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.header_frame.mouseMoveEvent = moveWindow
        self.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())


        self.show()

    def slideLeftMenu(self):
        
        width = self.slide_menu_container.width()

        
        if width == 0:
            
            newWidth = 350
            self.open_close_side_bar_btn.setIcon(QtGui.QIcon(r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python39\My Programs\Passport Automation System\icons\chevron-left.svg"))
        
        else:
            
            newWidth = 0
            self.open_close_side_bar_btn.setIcon(QtGui.QIcon(r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python39\My Programs\Passport Automation System\icons\align-left.svg"))

        
        self.animation = QPropertyAnimation(self.slide_menu_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def restore_or_maximize_window(self):
        
        if self.isMaximized():
            self.showNormal()
            self.restore_window_button.setIcon(QtGui.QIcon(r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python39\My Programs\Passport Automation System\icons\maximize-2.svg"))
        else:
            self.showMaximized()
            self.restore_window_button.setIcon(QtGui.QIcon(r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python39\My Programs\Passport Automation System\icons\minimize-2.svg"))

    def gotocreate_login(self):
         login=Login()
         widget.addWidget(login)
         widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate_register(self):
         register=Register()
         widget.addWidget(register)
         widget.setCurrentIndex(widget.currentIndex()+1) 

    def gotocreate_payment(self):
         payment=Payment()
         widget.addWidget(payment)
         widget.setCurrentIndex(widget.currentIndex()+1) 

    def gotocreate_status(self):
         status=Status()
         widget.addWidget(status)
         widget.setCurrentIndex(widget.currentIndex()+1)
        

   


  
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(800)
widget.setFixedWidth(1000)
widget.show()
app.exec_() 