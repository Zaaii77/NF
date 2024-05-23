import pyautogui
import sys
import time
from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt

pixel_x, pixel_y = 170, 66
target_color = (4, 81, 104) 

def get_pixel_color(x, y):
    screen = ImageGrab.grab()
    return screen.getpixel((x, y))

def check_and_click():
    while True:
        current_color = get_pixel_color(pixel_x, pixel_y)

        if current_color == target_color:
            # Cliquer à la position spécifiée
            pyautogui.click(pixel_x, pixel_y)
            print(f"Clicked at ({pixel_x}, {pixel_y})")

        time.sleep(2)


class App(QWidget):

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        button = QPushButton("Cliquez-moi !", self)
        button.clicked.connect(self.button_click)
        button.setStyleSheet("border: 0px;")
        button.setFixedSize(60, 60)
        button.move(0, 0)
        self.show()
        check_and_click()

    def button_click(self):
        
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
        time.sleep(2.5)
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
