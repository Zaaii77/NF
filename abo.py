import time
import pyautogui
from PIL import ImageGrab

# Position du pixel à vérifier
pixel_x, pixel_y = 170, 66

# Couleur cible (R, G, B) que le pixel doit avoir pour cliquer
target_color = (4, 81, 104)  # Remplacez par la couleur souhaitée

def get_pixel_color(x, y):
    # Capture l'écran et obtient la couleur du pixel à la position (x, y)
    screen = ImageGrab.grab()
    return screen.getpixel((x, y))

while True:
    # Obtenir la couleur actuelle du pixel
    current_color = get_pixel_color(pixel_x, pixel_y)

    # Vérifier si la couleur actuelle correspond à la couleur cible
    if current_color == target_color:
        # Cliquer à la position spécifiée
        pyautogui.click(pixel_x, pixel_y)

    # Attendre 2 secondes avant de vérifier à nouveau
    time.sleep(2)