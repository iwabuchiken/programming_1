@echo off
REM ************************************`
REM * sub2_call.bat						*
REM * Author: Iwabuchi Ken				*
REM * Date: 20120130_075829			*
REM * Aim:								*
REM * 	1.
REM	Source:
REM		1. http://windows.g.hatena.ne.jp/cx20/20100203/p1
REM *									*
REM ************************************/

call :sum 1, 2
echo %total%
goto :end

:sum
set /A total=%1+%2

:end