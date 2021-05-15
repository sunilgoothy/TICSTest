# Reference: https://docs.python.org/3.9/library/asyncio-task.html

import time
import psutil
import threading
import PySimpleGUI as sg

CLOSE = False

sg.theme('Black')


btn_exit = [sg.Text('', size=(15, 1), font=('Helvetica', 10), justification='left', key='-test-'),
            sg.Exit(button_text='x', key='Exit',
                    button_color=('white', 'firebrick4')),
            ]

layout = [
    [sg.Text('', size=(10, 1), font=('Helvetica', 20),
             justification='center', key='-text-')],

    # [sg.Exit(button_color=('white', 'firebrick4'), size=(20, 1), pad=((5,0),0))]
    [sg.Column([btn_exit], justification='right')]

]

# Layout the rows of the Window
window = sg.Window('CPU Meter',
                   layout,
                   no_titlebar=True,
                   keep_on_top=True,
                   grab_anywhere=True, location=(1170, 635), finalize=True)

window['-text-'].update(f'CPU {0:02.0f}%')


def open_ui():
    global CLOSE
    while True:
        # --------- Read and update window --------
        event, values = window.read(timeout=1000)

        # --------- Do Button Operations --------
        if event in (sg.WIN_CLOSED, 'Exit'):
            print(window.current_location())
            CLOSE = True
            break

    # Broke out of main loop. Close the window.
    window.close()


def cpu_load():
    updates = 0
    while not CLOSE:
        cpu_percent = psutil.cpu_percent(interval=1)
        updates = updates + 1
        # print(cpu_percent, updates)
        if not CLOSE:
            window['-text-'].update(f'CPU {cpu_percent:02.1f}%')
            window['-test-'].update(f'UPDATES: {updates}')

        time.sleep(0.5)


if __name__ == '__main__':
    print(f"started at {time.strftime('%X')}")

    threading.Thread(target=cpu_load).start()

    open_ui()

    print(f"finished at {time.strftime('%X')}")
