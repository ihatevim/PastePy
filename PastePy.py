import pyperclip
import pyautogui
from pynput import keyboard

print("Press insert to print and escape to exit.")

def on_press(key):
    try:
        if key == keyboard.Key.insert:
            print("Pasting...")
    except AttributeError:
        print('{0} pressed, something broke...'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key == keyboard.Key.insert:
        pyautogui.typewrite(pyperclip.paste())

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
