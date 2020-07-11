## Pyinstaller command
* Execute below command to generate single executable file for flask app

`pyinstaller -F --paths e:\devprojects\devenv\flaskvenv\lib\site-packages --add-data "..\templates;templates" --add-data "..\static;static" flask_start.py`
`pyinstaller -F --paths --add-data "..\templates;templates" --add-data "..\static;static" flask_start.py`


## Run directly
* Run flask_start.py file from venv


__Run above commands from venv__



sc create TICSTest binpath= "E:\DevProjects\TICSTest\dist\flask_start.exe" DisplayName= "TICSTestSvcSC" start=demand