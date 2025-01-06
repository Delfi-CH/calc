@echo off

cd C:\Users\%USERPROFILE%\Downloads

type calcinfo.txt

set /P i1=Number 1 = 
set /P i2=Number 2 = 
set /P how=Operator =

set /A o = %i1% %how% %i2%

echo Result : %o%
pause