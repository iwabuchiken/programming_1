@echo off
REM ************************************`
REM * sub7_split_string.bat				*
REM * Author: Iwabuchi Ken				*
REM * Date: 20120130_075829			*
REM * Aim:								*
REM		1. Split a given string using a given delimiter
REM	Source:
REM		1. http://stackoverflow.com/questions/1707058/how-to-split-a-string-in-a-windows-batch-file
REM *									*
REM ************************************/

set test=test.bat.file

for /f "delims=." %%a in ("test") do (
		echo a=%%a
		echo test=%test%
		REM echo %%b
)