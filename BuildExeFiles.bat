REM Change to Environment directory (location of .bat file).
cd /D "%~dp0"
cd VENV_BilderVerwaltung\Scripts
REM cd VENV_BilderVerwaltung_T440s\Scripts
REM Activate Environment and run pyinstaller command
activate.bat^
 & cd /D "%~dp0"^
 & pyinstaller --onefile --icon "Icons\UnifyPictureNames.ico" "UnifyPictureNames.py" --version-file=Version.py --name "Bilder_Namen_Vereineitlichen"^
 & pyinstaller --onefile --icon "Icons\SetNameAsCaptureDate.ico" "SetNameAsCaptureDate.py" --version-file=Version.py --name "Name_Als_Aufnahmedatum"^
 & pyinstaller --onefile --icon "Icons\ReduceImageFileSize.ico" "ReduceImageFileSize.py" --version-file=Version.py --name "Dateigroesse_Reduzieren"^
 & pyinstaller --onefile --icon "Icons\ChangeCaptureDate.ico" "ChangeCaptureDate.py" --version-file=Version.py --name "Aufnahmedatum_Anpassen"^
 & PAUSE
