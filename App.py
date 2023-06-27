# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '218181327Qt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtWidgets import QMessageBox
from twilio.rest import Client 
 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 408)
        MainWindow.setStyleSheet("background rgb(255, 115, 223)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(591, 0))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.textEdit = QtWidgets.QTextEdit(self.about)
        self.textEdit.setGeometry(QtCore.QRect(170, 10, 371, 271))
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"gridline-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.about)
        self.label.setGeometry(QtCore.QRect(20, 140, 151, 21))
        self.label.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.about)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 151, 21))
        self.label_2.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"border-top-color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.about)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 151, 21))
        self.label_3.setStyleSheet("alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(255, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.about)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 141, 81))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/images/WP_20201007_10_05_55_Pro (2).jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.about, "")
        self.Tab = QtWidgets.QWidget()
        self.Tab.setObjectName("Tab")
        self.next = QtWidgets.QPushButton(self.Tab)
        self.next.setGeometry(QtCore.QRect(310, 290, 181, 61))
        self.next.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.next.setObjectName("next")
        self.prev = QtWidgets.QPushButton(self.Tab)
        self.prev.setGeometry(QtCore.QRect(70, 290, 191, 61))
        self.prev.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.prev.setObjectName("prev")
        self.picture = QtWidgets.QLabel(self.Tab)
        self.picture.setGeometry(QtCore.QRect(70, 0, 421, 291))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap(":/images/2020-03-06 (5).png"))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")
        self.tabWidget.addTab(self.Tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.call = QtWidgets.QPushButton(self.tab)
        self.call.setGeometry(QtCore.QRect(210, 210, 151, 41))
        self.call.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
        self.call.setObjectName("call")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 0, 551, 191))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.insta = QtWidgets.QPushButton(self.tab)
        self.insta.setGeometry(QtCore.QRect(320, 10, 75, 23))
        self.insta.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.insta.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/077_twitter-512.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insta.setIcon(icon)
        self.insta.setObjectName("insta")
        self.twitter = QtWidgets.QPushButton(self.tab)
        self.twitter.setGeometry(QtCore.QRect(320, 30, 75, 23))
        self.twitter.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.twitter.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/instagram-icon-suzem-limited-make-known-20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.twitter.setIcon(icon1)
        self.twitter.setObjectName("twitter")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.prev.clicked.connect(self.show_Prev)
        self.next.clicked.connect(self.show_Next)
        self.call.clicked.connect(self.show_popup)
        self.call.clicked.connect(self.show_call_me)

    def show_popup(self):
            msg= QMessageBox()
            msg.setWindowTitle('Confirmation')
            msg.setText('Your Message has been sent Succefully')
            msg.setStandardButtons(QMessageBox.Ok)
            
            msg.exec_()

    def show_call_me(self):
            account_sid = 'AC47c1f834866be49903ef47432080131c' 
            auth_token = 'd10627f2b0ec5e27d65e7d8e7db7e149'
            client = Client(account_sid, auth_token) 
            
            
            call = client.calls.create(
                        from_='+13474915638',        
                        to='+265991071898'
            )
           
            print(call.sid)

    

    def show_Prev(self):
        self.picture.setPixmap(QtGui.QPixmap("Picture prev.png"))

    def show_Next(self):
        self.picture.setPixmap(QtGui.QPixmap("Picture Next.png"))
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project App"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">I am an only child of a family of Two.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Born and Raised in Malawi.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Currently studying B.Sc  Mechanical Engineering.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">At the University of Namibia.</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Name : Tupochele Chatuwa"))
        self.label_2.setText(_translate("MainWindow", "Age   : 20"))
        self.label_3.setText(_translate("MainWindow", "Job   : Student"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("MainWindow", "About Me"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.prev.setText(_translate("MainWindow", "Previous"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab), _translate("MainWindow", "My Photos"))
        self.call.setText(_translate("MainWindow", "CALL ME"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffaaff;\"><span style=\" font-size:16pt; background-color:#ffaaff;\">Soicial Media:     abiti_chatuwa</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffaaff;\"><span style=\" font-size:16pt; background-color:#ffaaff;\">        abiti_chatuwa</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffaaff;\"><span style=\" font-size:16pt; background-color:#ffaaff;\">Email : tupochelechatuwa@gmail.com</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffaaff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffaaff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffaaff;\"><span style=\" font-size:16pt; background-color:#ffaaff;\">To Text and call me use the call button below.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffaaff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffaaff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffaaff;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffaaff;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Contact Information"))
        



import Images

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

