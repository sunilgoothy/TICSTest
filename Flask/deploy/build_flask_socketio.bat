xcopy /E /C /F /Y /Z ..\templates dist\templates\ 
xcopy /E /C /F /Y /Z ..\static dist\static\
pyinstaller --onefile --noconfirm --log-level=INFO ..\flask_socketio_start.py