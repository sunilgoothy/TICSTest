import eel
import psutil
import eel.browsers

eel.init('cpu')
eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')


@eel.expose
def get_cpu_load():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_str = f"{cpu_percent:04.1f}"
    # import random
    # cpu = random.randint(1, 100)
    # print(cpu_str)
    return cpu_str


if __name__ == '__main__':
    # options = {
    #     'mode': 'electron',
    #     'args': ['electron/electron.exe', '.']}
    # eel.start('index.html', size=(200, 140), position=(1100, 100))
    eel.start('index.html', mode='electron')
