from shutil import copy2
import os
from datetime import datetime
import logging
import Progress
import piexif


def SetNameAsCaptureDate(inputFolder, outputFolder):
    processedFiles = 0
    changedFiles = 0
    unchangedFiles = 0
    for path, subDirectories, files in os.walk(inputFolder):
        # create output path
        if not os.path.exists(path.replace(inputFolder, outputFolder)):
            os.makedirs(path.replace(inputFolder, outputFolder))

        for file in files:
            filePath = os.path.join(path, file)

            newFilePath = GetUniqueFile(path.replace(inputFolder, outputFolder), file)
            copy2(filePath, newFilePath)

            if file.lower().endswith((".jpg", ".jpeg")):                
                try:
                    captureTime = datetime.strptime(file[0:15], "%Y%m%d_%H%M%S")
                except Exception:
                    try:
                        captureTime = datetime.strptime(file[0:8], "%Y%m%d")
                    except Exception:
                        logging.info("{0} - Unable to set capture time for: \"{1}\"".format(GetFormattedDatetimeNow(), filePath))
                        continue

                captureTime_string = captureTime.strftime("%Y:%m:%d %H:%M:%S")
                exif_dict = piexif.load(filePath)
                exifData = exif_dict.get("Exif")
                captureTime_bytes = bytes(captureTime_string, 'utf-8')
                exif_dict["Exif"][36867] = captureTime_bytes
                exif_bytes = piexif.dump(exif_dict)
                piexif.insert(exif_bytes, newFilePath)
                changedFiles += 1

            else:
                unchangedFiles += 1

            processedFiles += 1
            Progress.PrintProgress(processedFiles)

    logging.info("{0} - Processed Files: {1} | ChangedFiles: {2} | Unchanged Files: {3}".format(GetFormattedDatetimeNow(), processedFiles, changedFiles, unchangedFiles))


def GetFormattedDatetimeNow():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


# Check if file already exists and rename if needed
def GetUniqueFile(fileDirectory, file):
    fileName, fileExtension = os.path.splitext(file)
    filePath = os.path.join(fileDirectory, fileName)
    if os.path.isfile("{0}{1}".format(filePath, fileExtension)):
        fileNumber = 2
        while os.path.isfile("{0}_{1}{2}".format(filePath, fileNumber, fileExtension)):
            fileNumber += 1
        filePath = "{0}_{1}".format(filePath, fileNumber)

    return "{0}{1}".format(filePath, fileExtension)


try:
    logging.basicConfig(filename="SetNameAsCaptureDate.log", level=logging.INFO)
    logging.info("{0} - ##### Program Start #####".format(GetFormattedDatetimeNow()))

    print("This program will take file names in the format YYYYMMDD_hhmmss and set them as capture date of .jpg images.\n")
    inputFolder = input("Please specify the relative input folder name.\nJust press Enter to use the default value \"input\".\n")
    if not inputFolder:
        inputFolder = "input"
    outputFolder = input("Please specify the relative output folder name.\nJust press Enter to use the default value \"output\".\n")
    if not outputFolder:
        outputFolder = "output"
        
    SetNameAsCaptureDate(inputFolder, outputFolder)

    logging.info("{0} - ##### Execution Finished #####\n".format(GetFormattedDatetimeNow()))

except Exception as e:
    logging.exception("{0} - {1}".format(GetFormattedDatetimeNow(), e))


