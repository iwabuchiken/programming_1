@echo off
echo %1

rem if %1=="aaa" echo you wrote %1
rem if "%1"=="aaa" echo you wrote %1
if "%~1"=="aaa" echo you wrote %1

pause