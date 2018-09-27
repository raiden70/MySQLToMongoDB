import sys
from PyQt5.QtWidgets import (QWidget,QLineEdit,QFormLayout,QLabel,QGroupBox,QMessageBox,QPushButton, QApplication)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont,QIcon,QColor,QLinearGradient,QBrush,QPalette
from main import mainFunction

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet('''
        QLineEdit
        {border-radius: 20px; height:30px;border:1 solid grey; padding:2px;font-size:16px;}
        QLabel
        {font-size:18px;}
        QGroupBox
        {font-size:20px;} 
        ''')
    def initUI(self):
        layout=QFormLayout(self)
        layout2=QFormLayout(self)
        layout3=QFormLayout(self)

        groupe1=QGroupBox("Mysql:",self)
        groupe2 = QGroupBox("MongoDB:", self)

        layout.addRow(groupe1)
        layout.addRow(groupe2)

        l_host=QLabel("Host:",groupe1)
        self.e_host=QLineEdit(groupe1)
        self.e_host.setText("localhost")

        l_username=QLabel("Username:",groupe1)
        self.e_username=QLineEdit(groupe1)

        l_password=QLabel("Password:",groupe1)
        self.e_password=QLineEdit(groupe1)

        l_dbname = QLabel("DB Name:", groupe1)
        self.e_dbname = QLineEdit(groupe1)

        l_mhost=QLabel("Host:",groupe2)
        self.e_mhost=QLineEdit(groupe2)
        self.e_mhost.setText("localhost")

        l_port=QLabel("Port:",groupe2)
        self.e_port=QLineEdit(groupe2)
        self.e_port.setText("27017")

        btn = QPushButton('Transform', self)
        btn.setStyleSheet('''QPushButton
        {color: #FFF; background-color: gray;height:45px;font-size:18px;border-radius:20px;}
        QPushButton:hover
        {color: #000; background-color: white;}''')

        layout2.addRow(btn)
        groupe1.setLayout(layout2)
        groupe2.setLayout(layout3)

        layout2.addRow(l_host,self.e_host)
        layout2.addRow(l_username,self.e_username)
        layout2.addRow(l_password,self.e_password)
        layout2.addRow(l_dbname,self.e_dbname)

        layout3.addRow(l_mhost,self.e_mhost)
        layout3.addRow(l_port,self.e_port)
        layout.addRow(btn)

        btn.clicked.connect(self.trigger)
        self.setGeometry(400,300,500,300)
        self.setWindowTitle('Mysql To MongoDB')
        self.show()

    @pyqtSlot()
    def trigger(self):
        mo=mainFunction(self.e_host.text(),self.e_dbname.text(),self.e_username.text(),self.e_password.text(),self.e_mhost.text(),int(self.e_port.text()))
        msg=QMessageBox(self)
        msg.setWindowTitle("Opération Réussi")
        mo=', '.join(mo)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Importation terminée avec succées !")
        msg.setInformativeText("Toutes les tables sont bien importer:")
        msg.setDetailedText("Tables:\n"+mo)
        msg.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("logo.ico"))
    p = QPalette()

    gradient = QLinearGradient(0, 0, 0, 400)
    gradient.setColorAt(0.0, QColor(240, 240, 240))
    gradient.setColorAt(1.0, QColor(20, 20, 230))
    p.setBrush(QPalette.Window, QBrush(gradient))

    app.setPalette(p)
    ex = Example()
    sys.exit(app.exec_())