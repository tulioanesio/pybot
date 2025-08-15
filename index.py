import pyautogui

while True:
    print("Is red")
    if(pyautogui.pixel(399, 394) == (75, 219, 106)):
        pyautogui.click()
        print("Clicked on green")
        break