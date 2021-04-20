@echo off
set tp="%cd%"
cd /d "%~dp0
python functionNames.py %1 %tp%
