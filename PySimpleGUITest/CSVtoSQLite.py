import sqlite3, csv, json, time, sys
import datetime as dt
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import RELIEF_FLAT

sg.theme("Dark2")

def connect_to_db(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def close_connection(conn):
    conn.close()

def csv_to_db(filename, conn, table):

    with open(filename, mode="r") as csv_file:

        csv_dict = csv.DictReader(csv_file)
        total_rows = sum(1 for _ in csv_dict)
        print(f"{total_rows = }")
        csv_file.seek(0)

        csv_dict = csv.DictReader(csv_file)
        i = 0

        # Check if table exists
        try:
            query = f"Select Datetime from {table} where 1 = 0"
            conn.execute(query)
        except sqlite3.DatabaseError as e:
                if str(e).find("no such table") != -1:
                    print(e)
                    with open(f"config/{table}_Table_Script.sql", mode="r") as script:
                        create_stmt = script.read()
                        conn.execute(create_stmt)
                        conn.commit()
                        print("Table did not exist!!. Now generated.")
                else:
                    print(f"Exception in Checking table: {e}")

        for row in csv_dict:
            try:
                row["Datetime"] = row["Date"] + " " + row["Time"] + "." + row["Milli Sec"]
                datetime = row["Datetime"]
                query = f"insert into {table} {str(tuple(row.keys()))} values {str(tuple(row.values()))};"
                conn.execute(query)
            except sqlite3.DatabaseError as e:
                print(f"Exception in inserting to DB: {datetime}, {e}")

            
            # sg.one_line_progress_meter('Import Progress', i+1, total_rows, orientation='h')
            if ( not sg.one_line_progress_meter('Import Progress', i+1, total_rows, orientation='h') ) and ( i+1 != total_rows ):
                sg.popup_auto_close('Aborting Import....', non_blocking=True, auto_close_duration=1)
                print(f"Aborted at row: {i+1}")
                break

            i+=1
        conn.commit()
        print(f"{filename} imported. Check if there are any errors.")
    
def read_last_save():
    last_values = {}
    try:
        with open("config/last_save.json", "r") as last_save:
            last_saved_values = json.load(last_save)
            last_values["-DB-"] = last_saved_values.get("-DB-", "config/test.db")
            last_values["-TABLE-"] = last_saved_values.get("-TABLE-", "RMODGS")
            last_values["-CSVFILES-"] = last_saved_values.get("-CSVFILES-", "data/test.csv")
    except Exception as e:
        print(f"Error in reading last save / default values")
        last_values["-DB-"] = "config/test.db"
        last_values["-TABLE-"] = "RMODGS"
        last_values["-CSVFILES-"] = "data/test.csv"
    return last_values

def save_values():
    with open("config/last_save.json", "w") as save_file:
            json.dump(values, save_file, indent=4)

def window_layout(last_values):
    tables = ['RMODGS', 'FMODGS', 'DCODGS']
    dbtooltip = "If you want to create a new DB file, then enter the name manually in Input box" 
    button_layout = [sg.Button("Import", size=(10,1)), sg.Cancel("Exit", focus=True, bind_return_key=True, size=(10,1), button_color="red")]
    layout = [
        [sg.Text("Select DB", size=(15,1)), sg.Input(last_values['-DB-'], tooltip = dbtooltip, key='-DB-'), sg.FileBrowse(tooltip=dbtooltip, file_types=(("DB Files", "*.db"),))],
        [sg.Text("Select Table", size=(15,1)), sg.Combo(tables, default_value=last_values['-TABLE-'], size=(20,1), readonly=False, key='-TABLE-')],
        [sg.Text("Select CSV Files", size=(15,1)), sg.Input(last_values['-CSVFILES-'], key='-CSVFILES-'), sg.FilesBrowse(initial_folder=last_values['-CSVFILES-'], file_types=(("CSV Files", "*.csv"),))],
        [sg.Frame('', [button_layout], pad=((200,200),(1,1)), relief = RELIEF_FLAT)],
        # [sg.Output(key='-OUT-', size=(70, 10), font = "Consolas 12", echo_stdout_stderr = True, background_color="black", text_color="white")]
        [sg.Output(key='-OUT-', size=(60, 10), font = "Consolas 12", background_color="black", text_color="white")]
    ]
    return layout

def start_csv_import(csv_files, db_file, table):
    print(f"{db_file = }")
    print(f"{table = }")

    start = dt.datetime.now()
    print(f"Start time: {start}")

    conn = connect_to_db(db_file)
    for csv_file in csv_files:
        print(f"{csv_file = }")
        csv_to_db(csv_file, conn, table)
    close_connection(conn)

    end = dt.datetime.now()
    print(f"End time: {end}")

    elapsed_time = end - start
    print(f"Elapsed Time: {elapsed_time}")

def save_output(window):
    try:
        out = window['-OUT-'].get()
        with open(r"logs/CSVtoSQLite.log", "w") as log_file:
                log_file.write(out)
    except Exception as e:
        print(f"Error in saving log file: {e}")

if __name__ == '__main__':

    last_values = read_last_save()

    layout = window_layout(last_values)
    window = sg.Window("Import CSV to DB", layout, resizable=True, finalize=True)
    window['-OUT-'].TKOut.output.config(wrap='none')
    window['-OUT-'].expand(expand_x=True, expand_y=True)

    while True:
        try:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            
            if event == 'Import':
                confirm = sg.popup_yes_no('Are you sure?')
                if confirm == 'Yes':
                    csv_files = values['-CSVFILES-'].split(';')
                    start_csv_import(csv_files, values['-DB-'], values['-TABLE-'])

                    save_values()
        except Exception as e:
            print(f"Exception in Main: {e}")
        finally:
            save_output(window)

    window.close()