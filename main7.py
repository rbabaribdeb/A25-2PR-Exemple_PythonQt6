# app avec qlabel + bouton + gridLayout + QLineEdit + image
#https://www.tutorialspoint.com/pyqt/pyqt_qformlayout_class.htm
# pip install PyQt6
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QLineEdit

def action_btn1():
    lbl1.setText("Bonjour " + ledit1.text())

def action_btn2():
    lbl1.setText("Buenos dias " + ledit1.text())

# 1 Créer un objet application Qt
app = QApplication([])
# 2 Créer une fenetre Widget
fen = QWidget()
fen.setWindowTitle("========= Ma premiere application ============") # titre
fen.setGeometry(100,100,400,250) # taille de la fenetre

# creer un QGridLayout
grid = QGridLayout()
fen.setLayout(grid)

# creer QLabel ()
lbl1 = QLabel(fen)
lbl1.setText("Bonjour tout le monde !")
grid.addWidget(lbl1,0,0)

# creer QLineedit 1,0
ledit1 = QLineEdit("votre nom ici",fen)
grid.addWidget(ledit1,3,0)

# creer un bouton 1
btn1 = QPushButton(fen)
btn1.setText("Message FR")
btn1.clicked.connect(action_btn1)
grid.addWidget(btn1,2,0)

# creer un bouton 2
btn2 = QPushButton(fen)
btn2.setText("Message ES")
btn2.clicked.connect(action_btn2)
grid.addWidget(btn2,2,1)

# creer QPixmap object
im1 = QPixmap("./images/laptop.png")
# donner le qpixmap au qlabel
lbl_im1 = QLabel(fen)
lbl_im1.setPixmap(im1)
#lbl_im1.setGeometry(0,0,50,50)

lbl_im1.setFixedSize(50, 50)           # obligatoire dans un layout
lbl_im1.setScaledContents(True)

# modifier la taille de l'image
#lbl_im1.setScaledContents(True)
#lbl_im1.resize(200,200)
grid.addWidget(lbl_im1,1,0)

# 3 la fenetre va etre visible
fen.show()
# 4 executer l'application
app.exec()
