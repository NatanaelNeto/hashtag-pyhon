import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# pyautogui.alert('Vai começar. Aperte OK')

pyautogui.press('win')
pyautogui.write('chrome')
# time.sleep(5)
pyautogui.press('enter')
pyautogui.write('youtube.com')
pyautogui.press('enter')

time.sleep(3)
pyperclip.copy('Never Gonna Give You Up')
pyautogui.click(x=715, y=140)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(3)
pyautogui.click(x=715, y=500)

# print(pyautogui.position())
