import pyautogui
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # Garde la fenêtre toujours en avant-plan et sans bordure
        self.setGeometry(20, 490, 60, 60)  # Positionne la fenêtre à 20x490 avec une taille de 60x60

        button = QPushButton("Cliquez-moi !", self)
        button.clicked.connect(self.button_click)
        button.setStyleSheet("border: 0px;")
        button.setFixedSize(60, 60)
        button.move(0, 0)  # Positionne le bouton à l'intérieur de la fenêtre
        self.show()

    def button_click(self):
        # Fonction à exécuter lorsque le bouton est cliqué
        pyautogui.click(1542, 257)
        pyautogui.click(1542, 339)
        pyautogui.click(1542, 410)
        pyautogui.click(1542, 482)
        pyautogui.click(1542, 558)
        pyautogui.click(1542, 640)
        pyautogui.click(1542, 698)
        pyautogui.click(1542, 778)
        pyautogui.click(1542, 855)
        pyautogui.click(1542, 940)
        pyautogui.click(1420, 261)
        pyautogui.click(1420, 341)
        pyautogui.click(1420, 413)
        pyautogui.click(1420, 486)
        pyautogui.click(1420, 559)
        pyautogui.click(1420, 635)
        pyautogui.click(1420, 710)
        pyautogui.click(1420, 783)
        pyautogui.click(1420, 854)
        pyautogui.click(1420, 935)
        pyautogui.click(184, 105)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
