import PySimpleGUI as sg
from random import randint
import time

def randomint1():
    time.sleep(randint(1,3))
    print(randint(1, 1000))

def randomint2():
    time.sleep(randint(1,10))
    print(randint(5000, 5999))

sg.theme("DarkGreen4")

layout = [
    [sg.Text("PSG Threads Test")],
    [sg.Button("START Thread 1", key="START1")],
    [sg.Button("START Thread 2", key="START2")],
    [sg.Button("Close")],
    
]
window = sg.Window(title="Threads Test 2", layout=layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Close"):
        break
    if event == "START1":
        window.perform_long_operation(lambda: randomint1(), end_key="RET1")
    if event == "START2":
        window.perform_long_operation(lambda: randomint2(), end_key="RET2")
    if event == "RET1":
        pass
    if event == "RET2":
        pass
        
        
    
    

