REM Change to Environment directory.
cd /d D:\tmp\xxx\Projects\BilderVerwaltung\VENV_BilderVerwaltung\Scripts
REM Activate Environment and run pyinstaller command
activate.bat^
 & cd /d D:\tmp\xxx\Projects\BilderVerwaltung^
 & pyinstaller -F -i "Icons\UnifyPictureNames.ico" "UnifyPictureNames.py" --version-file=Version.py^
 & pyinstaller -F -i "Icons\SetNameAsCaptureDate.ico" "SetNameAsCaptureDate.py" --version-file=Version.py^
 & pyinstaller -F -i "Icons\ReduceImageFileSize.ico" "ReduceImageFileSize.py" --version-file=Version.py^
 & pyinstaller -F -i "Icons\ChangeCaptureDate.ico" "ChangeCaptureDate.py" --version-file=Version.py^
 & PAUSE
