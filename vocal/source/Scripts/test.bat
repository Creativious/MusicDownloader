@echo off
cls
set /p module=Module Install? 
"pip.exe" install %module%
pause