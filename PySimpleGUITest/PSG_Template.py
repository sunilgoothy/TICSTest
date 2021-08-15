import json, time
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import RELIEF_FLAT

def read_last_save():
    with open("config/last_save.json", "r") as last_save:
            last_values = json.load(last_save)
    return last_values

def save_values():
    with open("config/last_save.json", "w") as save_file:
            json.dump(values, save_file, indent=4)

def window_init(last_values):
    tables = ['RMODGS', 'FMODGS', 'DCODGS']
    button_layout = [sg.Button("TestPB"), sg.Cancel(focus=True, bind_return_key=True)]
    layout = [
        [sg.Text("Select DB", size=(15,1)), sg.Input(last_values['-DB-'], key='-DB-'), sg.FileBrowse(file_types=(("DB Files", "*.db"),))],
        [sg.Text("Select Table", size=(15,1)), sg.Combo(tables, default_value=last_values['-TABLES-'], size=(20,1), readonly=True, key='-TABLES-')],
        [sg.Text("Select CSV Folder", size=(15,1)), sg.Input(last_values['-CSVFOLDER-'], key='-CSVFOLDER-'), sg.FolderBrowse(initial_folder=last_values['-CSVFOLDER-'])],
        [sg.Frame('', [button_layout], pad=((200,200),(1,1)), relief = RELIEF_FLAT)]
    ]
    return layout

if __name__ == '__main__':

    last_values = read_last_save()

    layout = window_init(last_values)
    window = sg.Window("Import CSV to DB", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        
        if event == 'TestPB':
            MAX = 100

            # Method 2 Progress bar. Comment out when using Method 1.
            # pb_layout = [
            #     [sg.ProgressBar(MAX, size=(20, 20), key='-progress-')]
            # ]
            # pb_window = sg.Window('Import Progress', pb_layout, finalize=True)
            # progress_bar = pb_window['-progress-']       

            for i in range(0, MAX):
                # Method 1 Progress bar. Comment out when using Method 2.
                if not sg.one_line_progress_meter('Import Progress', i+1, MAX, orientation='h') and i+1 != MAX:
                    sg.popup_auto_close('Aborting Import....')
                    break

                # Method 2 contd...  Comment out when using Method 1.
                # progress_bar.update_bar(i+1)
                
                time.sleep(0.001)

            # Method 2 contd...  Comment out when using Method 1.
            # pb_window.close()

            save_values()

    window.close()