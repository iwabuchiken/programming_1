@echo off
REM ************************************`
REM * sub3_call2.bat					*
REM * Author: Iwabuchi Ken				*
REM * Date: 20120130_075829			*
REM * Aim:								*
REM * 	1. Run the script from the source 1
REM	Source:
REM		1. http://windows.g.hatena.ne.jp/cx20/20100203/p1
REM *									*
REM ************************************/

CALL :SUM 1, 2
ECHO %ERRORLEVEL%

GOTO END

:SUM
SET /A num1=%1
SET /A num2=%2
SET /A total=num1+num2

EXIT /B %total%

:END
