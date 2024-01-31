import sys
from requests import get
from json import loads
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QPalette, QColor,QFont
from PyQt6.QtCore import QSize,Qt


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.label= QLabel('')
        self.label2 = QLabel("")
        self.label3 = QLabel('')
        self.label4 = QLabel('')
        self.label5 = QLabel('')
        self.label6 = QLabel('')
        font = self.label.font()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        font = self.label2.font()
        font.setPointSize(15)
        self.label2.setFont(font)

        font = self.label3.font()
        font.setPointSize(15)
        self.label3.setFont(font)

        font = self.label4.font()
        font.setPointSize(15)
        self.label4.setFont(font)

        font = self.label5.font()
        font.setPointSize(15)
        self.label5.setFont(font)

        font = self.label6.font()
        font.setPointSize(15)
        self.label6.setFont(font)







        self.setWindowTitle("Aplikacja pogodowa")
        self.text= QLineEdit()
        self.text.setMaxLength(128)
        self.text.setPlaceholderText("Wprowadź miasto")
        self.text.textChanged.connect(self.text_changed)
        self.text.setFixedSize(500,80)

        self.text.setFixedSize(300,35)

        self.text.setStyleSheet("QLineEdit{border-radius:10px; font-size:20px}")





        self.button = QPushButton("Wyszukaj")
        self.button.setStyleSheet("""
        QPushButton {
         background-color: black; 
         font-size: 20px; 
         color: white; 
         border-radius: 25px;
         
        }
        QPushButton:hover{
        
        box-shadow: 0px 0px 15px 5px rgba(0,0,0,0.75);
        }
        
        """)

        self.button.setFixedSize(100,50)

        font = self.button.font()
        font.setPointSize(10)
        self.button.setFont(font)



        self.button.released.connect(self.the_button_was_released)


        layout2 = QHBoxLayout()
        layout1 = QVBoxLayout()
        layout3 = QHBoxLayout()




        layout1.addLayout(layout3)
        layout1.addLayout(layout2)
        layout2.addStretch()
        layout2.addWidget(self.button)
        layout2.addStretch()
        layout3.addWidget(self.text)
        layout2.setContentsMargins(0, 10, 0, 0)


        self.label.setStyleSheet("QLabel{color:aliceblue;}")
        self.label2.setStyleSheet("QLabel{color:aliceblue;}")
        self.label3.setStyleSheet("QLabel{color:aliceblue;}")
        self.label4.setStyleSheet("QLabel{color:aliceblue;}")
        self.label5.setStyleSheet("QLabel{color:aliceblue;}")
        self.label6.setStyleSheet("QLabel{color:aliceblue;}")




        layout1.addWidget(self.label)
        layout1.addWidget(self.label2)
        layout1.addWidget(self.label3)
        layout1.addWidget(self.label4)
        layout1.addWidget(self.label5)
        layout1.addWidget(self.label6)
        self.setMinimumSize(QSize(500, 500))
        self.setMaximumSize(QSize(500, 500))

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def the_button_was_released(self):



        url = 'https://danepubliczne.imgw.pl/api/data/synop'

        resposne = get(url).text

        miasto = self.text_changed(self)
        for i in loads(resposne):

            if miasto == i['stacja']:

                self.label.setText(f"----------------Miasto: {i['stacja']}----------------")
                self.label2.setText(f"Godzina pomiaru: {i['godzina_pomiaru']}:00")
                self.label3.setText(f"Temperatura: {i['temperatura']}C")
                self.label4.setText(f"Prędkość wiatru: {i['predkosc_wiatru']}km/h")
                self.label5.setText(f"Opady: {i['suma_opadu']}mm")
                self.label6.setText(f"Ciśnienie: {i['cisnienie']}hPa")









    def text_changed(self, s):
        return self.text.text()

app = QApplication(sys.argv)

window = MainWindow()
window.setStyleSheet("MainWindow {background-color: indigo;}")

window.show()

app.exec()

