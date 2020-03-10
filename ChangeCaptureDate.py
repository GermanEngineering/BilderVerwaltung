from shutil import copy2
import os
from datetime import datetime, timedelta
import logging
import Progress
import piexif


def ChangeCaptureDate(inputFolder, outputFolder, timeDifferenceInSeconds):
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

            if file.lower().endswith(('.jpg', '.jpeg')):
                captureTime = ""
                try:
                    exif_dict = piexif.load(filePath)
                    exifData = exif_dict.get("Exif")
                    
                    if exifData != {}:
                        captureTime_original = exifData[36867]
                        captureTime = str(captureTime_original)[2:-1]
                        captureTime = datetime.strptime(captureTime, "%Y:%m:%d %H:%M:%S")
                        newCaptureTime = captureTime + timedelta(seconds=timeDifferenceInSeconds)
                        newCaptureTime_string = newCaptureTime.strftime("%Y:%m:%d %H:%M:%S")
                        newCaptureTime_bytes = bytes(newCaptureTime_string, 'utf-8')
                        exif_dict["Exif"][36867] = newCaptureTime_bytes
                        exif_bytes = piexif.dump(exif_dict)
                        piexif.insert(exif_bytes, newFilePath)
                        changedFiles += 1

                    else:                        
                        unchangedFiles += 1

                except Exception:
                    logging.info("{0} - No capture time found for: \"{1}\"".format(GetFormattedDatetimeNow(), filePath))

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
    logging.basicConfig(filename="ChangeCaptureDate.log", level=logging.INFO)
    logging.info("{0} - ##### Program Start #####".format(GetFormattedDatetimeNow()))

    print("This program will adapt the capture date of .jpg images by the specified time difference.\n")
    inputFolder = input("Please specify the relative input folder name.\nJust press Enter to use the default value \"input\".\n")
    if not inputFolder:
        inputFolder = "input"
    outputFolder = input("Please specify the relative output folder name.\nJust press Enter to use the default value \"output\".\n")
    if not outputFolder:
        outputFolder = "output"
    timeDifferenceInSeconds = input("Please enter the time difference in seconds.\nJust press Enter to use the default value: 0.\n")
    if not timeDifferenceInSeconds:
        timeDifferenceInSeconds = 0
    else:
        timeDifferenceInSeconds = int(timeDifferenceInSeconds)
        
    ChangeCaptureDate(inputFolder, outputFolder, timeDifferenceInSeconds)

    logging.info("{0} - ##### Execution Finished #####\n".format(GetFormattedDatetimeNow()))

except Exception as e:
    logging.exception("{0} - {1}".format(GetFormattedDatetimeNow(), e))

