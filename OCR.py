from PIL import Image
import pytesseract
import pyautogui
import time
import threading
from threading import Timer
from image import screenshot_timer
from cam import display_cam
from PIL import ImageFile
from translate import *

ImageFile.LOAD_TRUNCATED_IMAGES = True

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cam_thread = threading.Thread(target=display_cam)
cam_thread.start()

time.sleep(1.5)



def translate_image():
    last = ""
    while True:
        try:
            text_eng = pytesseract.image_to_string(screenshot_timer())
            read = True

            if text_eng != last:
                translator = Translator(to_lang="pt-br")
                translation = translator.translate(text_eng)

                last = text_eng

                print(f"Text: '{text_eng}' \nTradução: {translation}")

        except OSError as e:
            print(f"Error: {e}. Could not read image!")
        time.sleep(1.5)


    


