
REM Batch file to automate Level2

@echo off 
REM Run server.py
start cmd /k "python server.py"

REM Wait for the server to start up 
timeout /t 2 /nobreak > NUL

REM Run main.py
python main.py

REM Click to exit on terminal
pause
