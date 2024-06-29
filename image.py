import pyautogui
from threading import Timer
import numpy as np

def screenshot_timer():
    screenshot = pyautogui.screenshot(region=(7, 7, 640, 460))

    imagem = screenshot.convert('RGB')
    
    npimagem = np.asarray(imagem).astype(np.uint8)

    Timer(1.5, screenshot_timer).start()

    return npimagem
    
