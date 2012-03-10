@echo off
REM ************************************`
REM * sub1_string.bat					*
REM * Author: Iwabuchi Ken				*
REM * Date: 20120118_080021			*
REM * Aim:								*
REM * 	1.
REM *									*
REM ************************************/

set str1=abcd
set str3=zxcv
echo %str1%
set str2=%str1:~0,2%
echo %str2%
echo %str1:~0,3%
echo %str3%

REM 'for' statement
FOR /L %%i IN (1,1,5) DO @ECHO %%i

REM for: list
for %%i in (a b c d) do @echo %%i
