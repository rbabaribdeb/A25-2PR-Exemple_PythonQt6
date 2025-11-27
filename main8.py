# Exercice de calculateur
# qlineEdit champs a
# qlineEdit champ  b
# lbl    resultat
# btn    calculer +
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QLabel, QPushButton

#1 une fenetre vide ...
def btn_calculer_action():
    global resultat
    try:
        a = int(input1.text())
        b = int(input2.text())
        resultat = a + b
    except Exception as e:
        print("Exception recuperee : " + e.__str__())
        resultat = "erreur"
        input1.setText("")
        input2.setText("")
    finally:
        lbl_resultat.setText(" = " + str(resultat))

# app + fen
app = QApplication([])
fen = QWidget()

# grid layout
grid = QGridLayout()
fen.setLayout(grid)

# lbl1
lbl_input1 = QLabel("a = ")
grid.addWidget(lbl_input1,0,0)
# input1
input1 = QLineEdit(fen)
grid.addWidget(input1,0,1)
#lbl2
lbl_input2 = QLabel("b = ")
grid.addWidget(lbl_input2,1,0)
#input2
input2 = QLineEdit(fen)
grid.addWidget(input2,1,1)
# lbl_resultat
lbl_resultat = QLabel(fen)
lbl_resultat.setText("...")
grid.addWidget(lbl_resultat,2,0)
# btn_calculet
btn_calculer = QPushButton("Calculer +")
btn_calculer.clicked.connect(btn_calculer_action)
grid.addWidget(btn_calculer,3,1)
# affiche la fenetre + execute l'application ... :)
fen.show()
app.exec()
