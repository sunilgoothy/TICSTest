# Reference: https://docs.python.org/3.9/library/asyncio-task.html

import asyncio, time, psutil
import PySimpleGUI as sg


CPU_PERCENT = 0
CLOSE = False
UPDATES = 0

async def open_ui():
    global CLOSE
    sg.theme('Black')

    layout = [
            [sg.Text('', size=(8, 1), font=('Helvetica', 20), justification='center', key='-text-')],
            [sg.Text('', size=(16, 1), font=('Helvetica', 10), justification='center', key='-test-')],
            [sg.Exit(button_color=('white', 'firebrick4'), size=(16, 1))]
            ]

    # Layout the rows of the Window
    window = sg.Window('CPU Meter',
                    layout,
                    no_titlebar=True,
                    keep_on_top=True,
                    grab_anywhere=True, finalize=True)

    window['-text-'].update(f'CPU {CPU_PERCENT:02.0f}%')
    # ----------------  main loop  ----------------
    while True:
        # --------- Read and update window --------
        event, values = window.read(timeout=3000)

        # --------- Do Button Operations --------
        if event in (sg.WIN_CLOSED, 'Exit'):
            CLOSE = True
            break
 
        window['-text-'].update(f'CPU {CPU_PERCENT:02.0f}%')
        window['-test-'].update(f'UPDATES: {UPDATES}')

        await asyncio.sleep(0.0001)

    # Broke out of main loop. Close the window.
    window.close()



async def cpu_load(delay):
    global CPU_PERCENT
    global UPDATES
    while not CLOSE:
        CPU_PERCENT = psutil.cpu_percent(interval=1)
        UPDATES = UPDATES + 1
        await asyncio.sleep(delay)

async def main():
    task1 = asyncio.create_task(cpu_load(1))
    task2 = asyncio.create_task(open_ui())

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2
    
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())