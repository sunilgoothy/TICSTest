import eel
import psutil
import eel.browsers
import os

eel.init('cpuweb')
eel.browsers.set_path('electron', r'E:/DevProjects/TICSTest/Eel/node_modules/electron/dist/electron')

APPLICATION_PATH = os.getcwd()

# with open(r"E:/DevProjects/TICSTest/Eel/out.txt", "w") as file1:
#     # Writing data to a file
#     file1.write(APPLICATION_PATH)

print(f"Current Application Directory {APPLICATION_PATH}")
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
    # eel.start('index.html', size=(200, 100), position=(1200, 610))
    eel.start('index.html', mode='electron')
