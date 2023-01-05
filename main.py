import time
import keyboard
import pyautogui
from password_generator import PasswordGenerator

# const values
PASSWORD_LENGTH = 15
ENTER_KEY_VALUE = (1266, 689)
REFRESH_KEY_VALUE = (1262, 623)
BAR_KEY_VALUE = (916, 567)

pwo = PasswordGenerator()

keyboard.wait('enter')  # press to start
count_till_reset = 0
# run until we press the escape key
while not keyboard.is_pressed('esc'):
    if count_till_reset == 3:  # refreshing the screen
        pyautogui.click(REFRESH_KEY_VALUE[0], REFRESH_KEY_VALUE[1])
        time.sleep(0.01)  # waiting until the page resets
        pyautogui.click(BAR_KEY_VALUE[0], BAR_KEY_VALUE[1])
        count_till_reset = 0
    value = pwo.non_duplicate_password(PASSWORD_LENGTH)  # recreate a new password
    keyboard.write(value)
    pyautogui.click(ENTER_KEY_VALUE[0], ENTER_KEY_VALUE[1])  # send the info
    count_till_reset += 1
    print(f'tried: {value}')

