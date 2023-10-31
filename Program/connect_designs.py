import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MonApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ma Application Qt')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Créez les boutons
        bouton_jouer = QPushButton('Jouer')
        bouton_options = QPushButton('Options')
        bouton_rejouer = QPushButton('Rejouer')
        bouton_conseil = QPushButton('Conseil')
        bouton_annuler = QPushButton('Annuler')
        bouton_annuler_tout = QPushButton('Annuler Tout')
        bouton_sauvegarder = QPushButton('Sauvegarder')
        bouton_annuler2 = QPushButton('Annuler 2')  # J'ai ajouté un bouton "Annuler 2" pour montrer comment connecter plusieurs boutons "Annuler"

        # Connectez les boutons à des actions
        bouton_jouer.clicked.connect(self.action_jouer)
        bouton_options.clicked.connect(self.action_options)
        bouton_rejouer.clicked.connect(self.action_rejouer)
        bouton_conseil.clicked.connect(self.action_conseil)
        bouton_annuler.clicked.connect(self.action_annuler)
        bouton_annuler_tout.clicked.connect(self.action_annuler_tout)
        bouton_sauvegarder.clicked.connect(self.action_sauvegarder)
        bouton_annuler2.clicked.connect(self.action_annuler2)

        # Ajoutez les boutons au layout
        layout.addWidget(bouton_jouer)
        layout.addWidget(bouton_options)
        layout.addWidget(bouton_rejouer)
        layout.addWidget(bouton_conseil)
        layout.addWidget(bouton_annuler)
        layout.addWidget(bouton_annuler_tout)
        layout.addWidget(bouton_sauvegarder)
        layout.addWidget(bouton_annuler2)

        self.setLayout(layout)

    def action_jouer(self):
        print("Action Jouer")

    def action_options(self):
        print("Action Options")

    def action_rejouer(self):
        print("Action Rejouer")

    def action_conseil(self):
        print("Action Conseil")

    def action_annuler(self):
        print("Action Annuler")

    def action_annuler_tout(self):
        print("Action Annuler Tout")

    def action_sauvegarder(self):
        print("Action Sauvegarder")

    def action_annuler2(self):
        print("Action Annuler 2")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MonApplication()
    fenetre.show()
    sys.exit(app.exec_())
