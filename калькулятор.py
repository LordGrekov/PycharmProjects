# Form implementation generated from reading ui file 'калькулятор.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 50))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(163, 163, 163);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 120, 120);")
        self.label.setObjectName("label")
        self.btn_rezult = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rezult.setGeometry(QtCore.QRect(200, 329, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_rezult.setFont(font)
        self.btn_rezult.setStyleSheet("")
        self.btn_rezult.setObjectName("btn_rezult")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(100, 330, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("")
        self.btn_0.setObjectName("btn_0")
        self.btn_C = QtWidgets.QPushButton(self.centralwidget)
        self.btn_C.setGeometry(QtCore.QRect(0, 330, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_C.setFont(font)
        self.btn_C.setStyleSheet("")
        self.btn_C.setObjectName("btn_C")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 260, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("")
        self.btn_3.setObjectName("btn_3")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 120, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("")
        self.btn_7.setObjectName("btn_7")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 190, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("")
        self.btn_4.setObjectName("btn_4")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 190, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("")
        self.btn_6.setObjectName("btn_6")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 120, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("")
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 120, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("")
        self.btn_8.setObjectName("btn_8")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 190, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("")
        self.btn_5.setObjectName("btn_5")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 260, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("")
        self.btn_2.setObjectName("btn_2")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 260, 100, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("")
        self.btn_1.setObjectName("btn_1")
        self.btn_oper_summa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_oper_summa.setGeometry(QtCore.QRect(0, 50, 61, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_oper_summa.setFont(font)
        self.btn_oper_summa.setStyleSheet("")
        self.btn_oper_summa.setObjectName("btn_oper_summa")
        self.btn_oper_ymnogit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_oper_ymnogit.setGeometry(QtCore.QRect(120, 50, 61, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_oper_ymnogit.setFont(font)
        self.btn_oper_ymnogit.setStyleSheet("")
        self.btn_oper_ymnogit.setObjectName("btn_oper_ymnogit")
        self.btn_oper_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_oper_minus.setGeometry(QtCore.QRect(60, 50, 61, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_oper_minus.setFont(font)
        self.btn_oper_minus.setStyleSheet("")
        self.btn_oper_minus.setObjectName("btn_oper_minus")
        self.btn_oper_delit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_oper_delit.setGeometry(QtCore.QRect(180, 50, 61, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_oper_delit.setFont(font)
        self.btn_oper_delit.setStyleSheet("")
        self.btn_oper_delit.setObjectName("btn_oper_delit")
        self.btn_oper_stepen = QtWidgets.QPushButton(self.centralwidget)
        self.btn_oper_stepen.setGeometry(QtCore.QRect(240, 50, 61, 70))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.btn_oper_stepen.setFont(font)
        self.btn_oper_stepen.setStyleSheet("")
        self.btn_oper_stepen.setObjectName("btn_oper_stepen")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_rezult.setText(_translate("MainWindow", "="))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_C.setText(_translate("MainWindow", "C"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_oper_summa.setText(_translate("MainWindow", "+"))
        self.btn_oper_ymnogit.setText(_translate("MainWindow", "*"))
        self.btn_oper_minus.setText(_translate("MainWindow", "-"))
        self.btn_oper_delit.setText(_translate("MainWindow", "/"))
        self.btn_oper_stepen.setText(_translate("MainWindow", "^"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
