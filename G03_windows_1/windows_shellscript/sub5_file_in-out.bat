@echo on
REM ************************************`
REM * sub5_file_in-out.bat				*
REM * Author: Iwabuchi Ken				*
REM * Date: 20120130_075829			*
REM * Aim:								*
REM		1. File write, read
REM	Source:
REM		1. http://windows.g.hatena.ne.jp/cx20/20100203/p1
REM *									*
REM ************************************/

for /f "tokens=*" %%i in (input.txt) do echo %%i
@echo
REM for /f "*" %%i in (input.txt) do echo %%i
