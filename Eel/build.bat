@ECHO OFF

python -m eel main_async.py web ^
    --noconsole ^
    --exclude-module tkinter ^
    --exclude-module babel ^
    --exclude-module pytz ^
    --exclude-module cryptography ^
    --exclude-module zope ^
    --exclude-module numpy ^
    --exclude-module multiprocessing ^
    --exclude-module curses ^
    --exclude-module asyncio