REM ************************************`
REM * sub9_file_f_option.bat			*
REM * Author: Iwabuchi Ken				*
REM * Date: 20120130_075829			*
REM * Aim:								*
REM		1. 'for' command: 'f' option
REM	Usage:
REM		1. Run the batch => tokens shown
REM	Source:
REM		1. http://stackoverflow.com/questions/1707058/how-to-split-a-string-in-a-windows-batch-file
REM		2. "for /?"
REM * <File history>
REM *	1. Created: 20120130
REM ************************************/

@echo off

REM **************************************
REM * <Descriptions>
REM *	1. Using 'f' option
REM *	2. Using "tokens", "delims" parameters
REM * <Problems>
REM *	1. Want to display "%i=xxx", but
REM *		the expression "%i" results in "i",
REM *		and the rest of the code not shown
REM **************************************
set x=ab.cd.ef.gh

for /f "tokens=1,2* delims=." %%i in ("%x%") do (
		@echo i=%%i
		@echo j=%%j
		@echo k=%%k
		REM @echo ^%%i=%%i
		REM @echo \%%i=%%i REM=> \ab
		REM @echo "%i"=%%i REM=> "i
		REM @echo %i=\%%i REM=> i
		@echo %j=%%j REM=> j
)
REM for /f "tokens=1,2* delims=." %%i in ("%x%") do (
REM	echo x=%x%
REM	echo %i=%%i
REM	echo %j=%%j
REM	echo %k=%%k
REM )

REM **************************************
REM * <Descriptions>
REM *	1. Using 'f' option
REM *	2. Using "tokens", "delims" attributes
REM *	3. "tokens" attribute: value expressed in
REM *		"n1-n2" format (see line: 63, or, search
REM *		for "tokens=1-3,4*")
REM * <Sources>
REM *	1. http://www.computing.net/answers/programming/split-a-string-dos-batch-script/16443.html
REM *		=> section: "tokens=1-5"
REM * <Tips>
REM *	1. The characters '<' and '>' escaped
REM *		using '^'(caret) character(see line:64,
REM *		or, search for "^<Play:2^>")
REM * <Problems>
REM *	1. None so far
REM * <Further>
REM *	1. No ideas for now
REM **************************************

set x=ab.cd.ef.gh.ijk
REM for /f "tokens=1-3 delims=." %%i in ("%x%") do (
for /f "tokens=1-3,4* delims=." %%i in ("%x%") do (
		@echo ^<Play:2^>
		@echo x=%x%
		@echo i=%%i
		@echo j=%%j
		@echo k=%%k
		@echo l=%%l
		REM @echo ^%i
			REM result ----------------------
				REM x=ab.cd.ef.gh.ijk
				REM i=ab
				REM j=cd
				REM k=ef
				REM l=gh
			REM -----------------------------

)

REM --------------- EOF ---------------
