import keyboard

def on_press(key):
    print(f'нажата клавиша{key.name}')

keyboard.on_press(on_press)

keyboard.wait()