# app avec qlabel
# pip install PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

# 1 Créer un objet application Qt
app = QApplication([])
# 2 Créer une fenetre Widget
fen = QWidget()
fen.setWindowTitle("========= Ma premiere application ============") # titre
fen.setGeometry(100,100,400,150) # taille de la fenetre

# creer QLabel ()
lbl1 = QLabel(fen)
lbl1.setText("Bonjour tout le monde !")

# 3 la fenetre va etre visible
fen.show()
# 4 executer l'application
app.exec()
