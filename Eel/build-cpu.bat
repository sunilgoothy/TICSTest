@ECHO OFF
REM --noconsole switch does not work with electron
python -m eel cpu.py cpuweb ^
    --noconfirm ^
    --onefile ^
    --exclude-module tkinter ^
    --exclude-module babel ^
    --exclude-module pytz ^
    --exclude-module cryptography ^
    --exclude-module zope ^
    --exclude-module numpy ^
    --exclude-module multiprocessing ^
    --exclude-module curses ^
    --exclude-module asyncio

copy main.js .\dist\main.js
copy package.json .\dist\package.json