' https://superuser.com/questions/198525/how-can-i-execute-a-windows-command-line-in-background
' https://serverfault.com/questions/9038/run-a-bat-file-in-a-scheduled-task-without-a-window

Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "cpu.exe" & Chr(34), 0
Set WinScriptHost = Nothing
