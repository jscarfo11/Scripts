import pyautogui
import time

pyautogui.alert(text="Please make sure Discord is opened and selected. "
                     "You can cancel the macro by moving the mouse to the top left corner of the screen.",
                button='Okay')
while True:
    pyautogui.typewrite('Message For Poketwo Spawns')
    time.sleep(0.5)
    pyautogui.press('enter', 1, 0.5)
    pyautogui.typewrite('Ben is a Nerd')
    pyautogui.press('enter', 1, 0.5)
