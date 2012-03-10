@echo off
REM ************************************`
REM * sub8_set_p_option.bat				*
REM * Author: Iwabuchi Ken				*
REM * Date: 20120130_075829			*
REM * Aim:								*
REM		1. 'set' command: 'p' option
REM	Usage:
		1. Run the batch => data in sub8.txt shown
REM	Source:
REM		1. http://stackoverflow.com/questions/1707058/how-to-split-a-string-in-a-windows-batch-file
REM		2. FILE: sub8.txt
REM *									*
REM ************************************/

set /p data= < sub8.txt

echo data=%data%