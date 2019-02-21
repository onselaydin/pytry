import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Test deneme kontrol başlık")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("AD SOYAD:")
    etiket1.move(150,40)
    pencere.setGeometry(100,100,500,500) #pencere boyutu tespiti
    pencere.show()

    sys.exit(app.exec_())

Pencere()