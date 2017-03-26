import pyautogui
import pytesseract
from PIL import Image
import time


time.sleep(3)

# It's not advised to use while loop
# There is a built-in mechanism in pyautogui to terminate program if we
# move our cursor to top left. This will cause program to break

while True:
    # region may vary for different screen
    im = pyautogui.screenshot(region=(232, 279, 835, 106))
    im.save('data.png')

    # To click text area and start typing
    pyautogui.click(x=464, y=425)

    # To get text from given image
    value = pytesseract.image_to_string(Image.open('data.png'))

    # To replace new line from it and make one clean list
    value = value.replace('\n\n',' ')
    b = value.split(' ')

    print(b)

    # Backspace is used to avoid any error
    for i in b:
        pyautogui.press('backspace')
        pyautogui.typewrite(i)
        pyautogui.press('space')
    if len(b) <= 4:
        break
