@echo off
REM ************************************`
REM * sub4_call3_call_exit.bat					*
REM * Author: Iwabuchi Ken				*
REM * Date: 20120130_075829			*
REM * Aim:								*
REM		1.
REM	Source:
REM		1. http://windows.g.hatena.ne.jp/cx20/20100203/p1
REM *									*
REM ************************************/
if "%1"=="" (
		set a=3
		set b=5
		echo set: a=3, b=5
) else (
		set a=%1
		echo a=%a%
REM		set b=%2
			if "%2"=="" (
				set b=5
			) else (
				set b=%2
			)
)

echo a=%a%
echo b=%b%

call :sum 3, 5
echo ans=%ans%
goto :end

:sum
 set total=%1+%2
REM if %1==3 (
 if %1=="3" (
 	 set ans="It's 3"
 	 exit /B %ans%
 )
REM else (
	 set ans="It's not 3"
	 exit /B %ans%
REM )

:end
