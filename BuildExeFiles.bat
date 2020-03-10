REM Change to Environment directory.
cd /d C:\CZ\Projects\UpdateScript\VENV_UpdateScript\Scripts
REM Activate Environment and run pyinstaller command
activate.bat^
 & cd /d c:\CZ\Projects\UpdateScript^
 & pyinstaller -F -i "Icons\UpdateScript.ico" "UpdateScript.py" --version-file=Version.py -n UpdateScript_0.0.0.5^
 & PAUSE
