# app de base
# pip install PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

# 1 Créer un objet application Qt
app = QApplication([])
# 2 Créer une fenetre Widget
fen = QWidget()

# 3 la fenetre va etre visible
fen.show()
# 4 executer l'application
app.exec()
