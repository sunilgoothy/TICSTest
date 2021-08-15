@ECHO OFF

pyinstaller ^
    --noconfirm ^
    --noconsole ^
    --onefile ^
    --exclude-module babel ^
    --exclude-module pytz ^
    --exclude-module cryptography ^
    --exclude-module zope ^
    --exclude-module numpy ^
    --exclude-module multiprocessing ^
    --exclude-module curses ^
    --exclude-module asyncio ^
    .\test_psg_threads.py