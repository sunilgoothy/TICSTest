@ECHO OFF

pyinstaller --onefile --noconfirm ^
    --distpath=.\dist\ ^
    --exclude-module tkinter ^
    --exclude-module babel ^
    --exclude-module pytz ^
    --name=app ^
    --specpath .\spec\ ^
    .\app.py