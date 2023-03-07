import numpy as np
from enum import auto
import sys
from this import d
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt5.QtWidgets import QMessageBox, QFormLayout, QAction
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import pyqtSlot

def Crout(A):
    n = len(A)
    U = np.zeros((n,n))
    L = np.zeros((n,n))
    for i in range(n):
        U[i, i] = 1
        for j in range(i+1):
            sum1 = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = A[i][j] - sum1
        for j in range(i,n):
            sum2 = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = (A[i][j] - sum2) / L[i][i]
    return L, U

def LTRIS(L,b):
    n = len(L)
    y = np.zeros((n,1))
    y = b
    for r in range(0,n):
        suml = sum(L[r][c] * y[c] for c in range(0,r))
        y[r] = (b[r] - suml) / L[r][r]
    return y

def UTRIS(U,y):
    n = len(U)
    x = np.zeros((n,1))
    x = y
    x[n-1] = y[n-1] / U[n-1][n-1]
    for r in range(n-2,-1,-1):
        sumu = sum(x[c] * U[r][c] for c in range(n-1,r,-1))
        x[r] = (y[r] - sumu) / U[r][r]
    return x

class TreiDoi(QMainWindow):
    def __init__(self, parent=None):
        super(TreiDoi, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setFixedWidth(700)
        self.setFixedHeight(470)
        self.setWindowTitle('SIMULATOR')
        self.setWindowIcon(QIcon("python.jpg"))

        self.label01 = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('propus2.jpg')
        self.label01.setPixmap(self.pixmap)
        self.label01.move(30, 30)
        self.label01.resize(self.pixmap.width(), self.pixmap.height())
        
        self.label02 = QtWidgets.QLabel(self)
        self.label02.setText('Circuit propus')
        self.label02.setAlignment(QtCore.Qt.AlignCenter)
        self.label02.setStyleSheet('font: 20px solid black;')
        self.label02.move(-60, 320)
        self.label02.resize(500, 100)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('V1 = ')
        self.label1.move(470, 30)
        self.textBox1 = QtWidgets.QLineEdit(self)
        self.textBox1.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox1.move(500, 30)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText('V2 = ')
        self.label2.move(470, 70)
        self.textBox2 = QtWidgets.QLineEdit(self)
        self.textBox2.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox2.move(500, 70)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText('V3 = ')
        self.label3.move(470, 110)
        self.textBox3 = QtWidgets.QLineEdit(self)
        self.textBox3.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox3.move(500, 110)

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText('R1 = ')
        self.label4.move(470, 150)
        self.textBox4 = QtWidgets.QLineEdit(self)
        self.textBox4.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox4.move(500, 150)

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText('R2 = ')
        self.label5.move(470, 190)
        self.textBox5 = QtWidgets.QLineEdit(self)
        self.textBox5.move(500, 190)

        self.label6 = QtWidgets.QLabel(self)
        self.label6.setText('R3 = ')
        self.label6.move(470, 230)
        self.textBox6 = QtWidgets.QLineEdit(self)
        self.textBox6.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox6.move(500, 230)

        self.label7 = QtWidgets.QLabel(self)
        self.label7.setText('R4 = ')
        self.label7.move(470, 270)
        self.textBox7 = QtWidgets.QLineEdit(self)
        self.textBox7.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox7.move(500, 270)

        self.label8 = QtWidgets.QLabel(self)
        self.label8.setText('R5 = ')
        self.label8.move(470, 310)
        self.textBox8 = QtWidgets.QLineEdit(self)
        self.textBox8.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox8.move(500, 310)

        self.labelx = QtWidgets.QLabel(self)
        self.labelx.setStyleSheet('font: 20px solid black;')
        self.labelx.move(30, 370)
        self.labelx.resize(100, 100)

        self.labely = QtWidgets.QLabel(self)
        self.labely.setStyleSheet('font: 20px solid black;')
        self.labely.move(140, 370)
        self.labely.resize(100, 100)

        self.labelz = QtWidgets.QLabel(self)
        self.labelz.setStyleSheet('font: 20px solid black;')
        self.labelz.move(240, 370)
        self.labelz.resize(100, 100)

        self.labelw = QtWidgets.QLabel(self)
        self.labelw.setStyleSheet('font: 20px solid black;')
        self.labelw.move(340, 370)
        self.labelw.resize(100, 100)

        self.action1 = QtWidgets.QAction('Rezolvare', self)

        self.toolbar = QtWidgets.QToolBar(self)
        self.toolbar.setStyleSheet('font: 20px solid black;')
        self.toolbar.move(475, 370)
        self.toolbar.resize(140, 40)
        self.toolbar.addAction(self.action1)

        self.action1.triggered.connect(self.on_pushButton_clicked)
 
    def on_pushButton_clicked(self):
        x1 = float(self.textBox1.text())
        x2 = float(self.textBox2.text())
        x3 = float(self.textBox3.text())
        x4 = float(self.textBox4.text())
        x5 = float(self.textBox5.text())
        x6 = float(self.textBox6.text())
        x7 = float(self.textBox7.text())
        x8 = float(self.textBox8.text())
        
        AA = np.array([[1, -1, -1, 1], [x4, x5, 0, 0], [0, -x5, x6+x7, 0], [0, 0, x6+x7, x8]])
        AA = np.triu(AA, -1)
        AA = AA.astype('float')
        bb =  np.array([[0, x1-x2, x2, x3]]).T
        bb = bb.astype('float')

        [L, U] = Crout(AA)

        y = LTRIS(L,bb)
        xx = UTRIS(U,y)

        self.labelx.setText('I1 = ' + str(round(xx[0][0], 2)))
        self.labely.setText('I2 = ' + str(round(xx[1][0], 2)))
        self.labelz.setText('I3 = ' + str(round(xx[2][0], 2)))
        self.labelw.setText('I4 = ' + str(round(xx[3][0], 2)))

class TreiUnu(QMainWindow):
    def __init__(self, parent=None):
        super(TreiUnu, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setFixedWidth(700)
        self.setFixedHeight(470)
        self.setWindowTitle('SIMULATOR')
        self.setWindowIcon(QIcon("python.jpg"))

        self.label01 = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('wheatstone2.jpg')
        self.label01.setPixmap(self.pixmap)
        self.label01.move(30, 30)
        self.label01.resize(self.pixmap.width(), self.pixmap.height())
        
        self.label02 = QtWidgets.QLabel(self)
        self.label02.setText('Punte Wheatstone')
        self.label02.setAlignment(QtCore.Qt.AlignCenter)
        self.label02.setStyleSheet('font: 20px solid black;')
        self.label02.move(-40, 310)
        self.label02.resize(500, 100)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('V = ')
        self.label1.move(460, 80)
        self.textBox1 = QtWidgets.QLineEdit(self)
        self.textBox1.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox1.move(490, 80)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText('R = ')
        self.label2.move(460, 120)
        self.textBox2 = QtWidgets.QLineEdit(self)
        self.textBox2.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox2.move(490, 120)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText('R1 = ')
        self.label3.move(460, 160)
        self.textBox3 = QtWidgets.QLineEdit(self)
        self.textBox3.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox3.move(490, 160)

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setText('R2 = ')
        self.label4.move(460, 200)
        self.textBox4 = QtWidgets.QLineEdit(self)
        self.textBox4.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox4.move(490, 200)

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setText('R3 = ')
        self.label5.move(460, 240)
        self.textBox5 = QtWidgets.QLineEdit(self)
        self.textBox5.move(490, 240)

        self.label6 = QtWidgets.QLabel(self)
        self.label6.setText('Rx = ')
        self.label6.move(460, 280)
        self.textBox6 = QtWidgets.QLineEdit(self)
        self.textBox6.setValidator(QDoubleValidator(0.99,99.99,2))
        self.textBox6.move(490, 280)

        self.labelx = QtWidgets.QLabel(self)
        self.labelx.setStyleSheet('font: 20px solid black;')
        self.labelx.move(60, 370)
        self.labelx.resize(100, 100)

        self.labely = QtWidgets.QLabel(self)
        self.labely.setStyleSheet('font: 20px solid black;')
        self.labely.move(180, 370)
        self.labely.resize(100, 100)

        self.labelz = QtWidgets.QLabel(self)
        self.labelz.setStyleSheet('font: 20px solid black;')
        self.labelz.move(300, 370)
        self.labelz.resize(100, 100)

        self.action1 = QtWidgets.QAction('Rezolvare', self)

        self.toolbar = QtWidgets.QToolBar(self)
        self.toolbar.setStyleSheet('font: 20px solid black;')
        self.toolbar.move(460, 350)
        self.toolbar.resize(140, 40)
        self.toolbar.addAction(self.action1)

        self.action1.triggered.connect(self.on_pushButton_clicked)
 
    def on_pushButton_clicked(self):
        x1 = float(self.textBox1.text())
        x2 = float(self.textBox2.text())
        x3 = float(self.textBox3.text())
        x4 = float(self.textBox4.text())
        x5 = float(self.textBox5.text())
        x6 = float(self.textBox6.text())
        
        if x3*x6 == x4*x5:
            AA = np.array([[1, -1, -1], [x2, x3+x4, 0], [0, -x3-x4, x5+x6]])
            AA = AA.astype('float')
            bb =  np.array([[0, x1, 0]]).T
            bb = bb.astype('float')

            [L, U] = Crout(AA)

            y = LTRIS(L,bb)
            xx = UTRIS(U,y)

            self.labelx.setText('I1 = ' + str(round(xx[0][0], 2)))
            self.labely.setText('I2 = ' + str(round(xx[1][0], 2)))
            self.labelz.setText('I3 = ' + str(round(xx[2][0], 2)))

class Doi(QMainWindow):
    def __init__(self, parent=None):
        super(Doi, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setFixedWidth(600)
        self.setFixedHeight(350)
        self.setWindowTitle('SIMULATOR')
        self.setWindowIcon(QIcon("python.jpg"))

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('Alegeti tipul circuitului pe care doriti\n' +
            'sa il analizati apasand unul din butoanele urmatoare')
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setStyleSheet('font: 20px solid black;')
        self.label1.move(50, 50)
        self.label1.resize(500, 100)

        self.button1 = QtWidgets.QPushButton('Punte Wheatstone', self)
        self.button1.setToolTip('Punte Wheatstone')
        self.button1.move(70, 220)
        self.button1.resize(200, 40)
        self.button1.setStyleSheet('font: 20px solid black;')
        self.button1.clicked.connect(self.on_pushButton1_clicked)
        self.dialog1 = TreiUnu(self)

        self.button2 = QtWidgets.QPushButton('Circuit Propus', self)
        self.button2.setToolTip('Circuit Propus')
        self.button2.move(320, 220)
        self.button2.resize(200, 40)
        self.button2.setStyleSheet('font: 20px solid black;')
        self.button2.clicked.connect(self.on_pushButton2_clicked)
        self.dialog2 = TreiDoi(self)
 
    def on_pushButton1_clicked(self):
        self.dialog1.show()

    def on_pushButton2_clicked(self):
        self.dialog2.show()
 
class Unu(QMainWindow):
    def __init__(self, parent=None):
        super(Unu, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setFixedWidth(600)
        self.setFixedHeight(350)
        self.setWindowTitle('SIMULATOR')
        self.setWindowIcon(QIcon("python.jpg"))

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('Rezolvarea unui circuit electric simplu')
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setStyleSheet('font: 20px solid black;')
        self.label1.move(50, 50)
        self.label1.resize(500, 100)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText('Rezolvarea unui circuit electric simplu propus\n' + 
            'cu ajutorul algoritmilor de rezolvare a sistemelor de ecuatii liniare')
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setStyleSheet('font: 16px solid black;')
        self.label2.move(50, 100)
        self.label2.resize(500, 100)

        self.button1 = QtWidgets.QPushButton('Continuare', self)
        self.button1.setToolTip('Continuare')
        self.button1.move(200, 240)
        self.button1.resize(200, 40)
        self.button1.setStyleSheet('font: 20px solid black;')
 
        self.button1.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Doi(self)
 
    def on_pushButton_clicked(self):
        self.dialog.show()
 
def main():
    app = QApplication(sys.argv)
    main = Unu()
    main.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()