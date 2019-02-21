import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Test deneme kontrol başlık")

    button1 = QtWidgets.QPushButton(pencere)
    button1.setText("Kaydet")

    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Merhaba Buttona tıkla")

    etiket1.move(200,30)
    button1.move(190,80)
    
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    app.exec_()

Pencere()