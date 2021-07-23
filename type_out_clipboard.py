from tkinter import Tk
from pyautogui import*

import time

clip_board_data = Tk().clipboard_get()

time.sleep(2)
for each in clip_board_data:
    press(each)
    time.sleep(.001)
