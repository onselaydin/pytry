import sys
from PyQt5 import QtWidgets,QtGui
import os
def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Test deneme kontrol başlık")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("AD SOYAD:")
    etiket1.move(150,40)

    resim1 = QtWidgets.QLabel(pencere)
    resim1.setPixmap(QtGui.QPixmap("/home/onsel/Documents/pytry/pyqt5/python.png"))
    resim1.move(90,100)
    
    pencere.setGeometry(100,100,500,500) #pencere boyutu tespiti
    pencere.show()

    app.exec_()

Pencere()