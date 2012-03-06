@echo off
set dig=dir
%dig%
echo Done
echo %1
echo %2
set change=pushd
set dst=%1
%change% %1
rem set do2=cd..
rem %do2%