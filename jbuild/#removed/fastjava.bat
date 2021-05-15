@echo off
set fastjava="%cd%"
set backto="%cd"
cd /d "%~dp0
set fastjava=python fastjava.py %1 %2 %fastjava%
%fastjava%