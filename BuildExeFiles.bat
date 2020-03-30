REM Change to Environment directory.
cd /d D:\tmp\xxx\Projects\BilderVerwaltung\VENV_BilderVerwaltung\Scripts
REM Activate Environment and run pyinstaller command
activate.bat^
 & cd /d D:\tmp\xxx\Projects\BilderVerwaltung^
 & pyinstaller --onefile --icon "Icons\UnifyPictureNames.ico" "UnifyPictureNames.py" --version-file=Version.py --name "Bilder_Namen_Vereineitlichen.py"^
 & pyinstaller --onefile --icon "Icons\SetNameAsCaptureDate.ico" "SetNameAsCaptureDate.py" --version-file=Version.py --name "Name_Als_Aufnahmedatum.py"^
 & pyinstaller --onefile --icon "Icons\ReduceImageFileSize.ico" "ReduceImageFileSize.py" --version-file=Version.py --name "Dateigröße_Reduzieren.py"^
 & pyinstaller --onefile --icon "Icons\ChangeCaptureDate.ico" "ChangeCaptureDate.py" --version-file=Version.py --name "Aufnahmedatum_Anpassen.py"^
 & PAUSE
