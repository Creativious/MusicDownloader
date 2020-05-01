@echo off
:start
cls
echo Creativious's Youtube to Music Program
echo.
set /p url=Give a youtube video link or playlist link? 
"source\python.exe" musicgrabber.py %url%
pause
set /p chv=Do you want to choose where to move the files[Y/N]?
if %chv% == Y goto var
if %chv% == y goto var
if %chv% == N goto end
if %chv% == n goto end
goto end
:var
cls
set /p dest=Path to move files? 
move "video_to_audio\output\*" "%dest%"
echo Files moved to %dest%
pause
:end
