# app avec qlabel + bouton
# pip install PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

def action_btn1():
    print("Bouton Ok appuyé")
    lbl1.setText("Déjà cliqué :)")

# 1 Créer un objet application Qt
app = QApplication([])
# 2 Créer une fenetre Widget
fen = QWidget()
fen.setWindowTitle("========= Ma premiere application ============") # titre
fen.setGeometry(100,100,400,150) # taille de la fenetre

# creer QLabel ()
lbl1 = QLabel(fen)
lbl1.setText("Bonjour tout le monde !")
lbl1.setGeometry(10,0,250,50)

# creer un bouton
btn1 = QPushButton(fen)
btn1.setText("OK")
btn1.clicked.connect(action_btn1)
btn1.setGeometry(10,50,250,50)


# 3 la fenetre va etre visible
fen.show()
# 4 executer l'application
app.exec()
