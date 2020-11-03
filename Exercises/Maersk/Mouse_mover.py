#! python3
# Mouse_mover.py - Moves the mouse, so Gunhilde doesn't fall asleep.
import pyautogui
from time import sleep

pyautogui.FAILSAFE = False

while True:
    sleep(1)
    screen = pyautogui.getActiveWindow()
    active_screen_name = str(screen).split(',')[4]
    sleep(1800)
    screen = pyautogui.getActiveWindow()
    active_screen = str(screen).split(',')[4]
    if active_screen == active_screen_name:

    sleep(1800)
