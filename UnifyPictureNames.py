import exifread
from shutil import copy2
import os
from datetime import datetime
import logging
import Progress


def UnifyPictureNames(inputFolder, outputFolder):
    processedFiles = 0
    renamedFiles = 0
    unchangedFiles = 0
    for path, subDirectories, files in os.walk(inputFolder):
        # create output path
        if not os.path.exists(path.replace(inputFolder, outputFolder)):
            os.makedirs(path.replace(inputFolder, outputFolder))

        for file in files:
            filePath = os.path.join(path, file)
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # get file metadata
                metadata = exifread.process_file(open(filePath, "rb"))
                captureTime = ""
                try:
                    captureTime = str(metadata["EXIF DateTimeOriginal"])
                except Exception:
                    logging.info("{0} - No capture time found for: \"{1}\"".format(GetFormattedDatetimeNow(), filePath))
                
                # pictures with creation timestamp
                if captureTime != "":
                    _, fileExtension = os.path.splitext(file)
                    newFile = captureTime.replace(":", "").replace(" ", "_") + fileExtension.lower()
                    copy2(filePath, GetUniqueFile(path.replace(inputFolder, outputFolder), newFile))
                    logging.debug("{0} - {1} --> {2}".format(GetFormattedDatetimeNow(), filePath, os.path.join(path.replace(inputFolder, outputFolder), newFile)))
                    renamedFiles += 1                
                # WhatsApp images
                elif "WA" in file:
                    newFile = file.replace("IMG-", "")
                    copy2(filePath, GetUniqueFile(path.replace(inputFolder, outputFolder), newFile))
                    logging.debug("{0} - {1} --> {2}".format(GetFormattedDatetimeNow(), filePath, os.path.join(path.replace(inputFolder, outputFolder), newFile)))
                    renamedFiles += 1
                # files without creation timestamp
                else:
                    copy2(filePath, GetUniqueFile(path.replace(inputFolder, outputFolder), file))
                    unchangedFiles += 1
            else:
                copy2(filePath, GetUniqueFile(path.replace(inputFolder, outputFolder), file))
                unchangedFiles += 1

            processedFiles += 1
            Progress.PrintProgress(processedFiles)

    logging.info("{0} - Processed Files: {1} | RenamedFiles: {2} | Unchanged Files: {3}".format(GetFormattedDatetimeNow(), processedFiles, renamedFiles, unchangedFiles))


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
    logging.basicConfig(filename="UnifyPictureNames.log", level=logging.INFO)
    logging.info("{0} - ##### Program Start #####".format(GetFormattedDatetimeNow()))

    inputFolder = input("Please specify the relative input folder name.\nJust press Enter to use the default value \"input\".\n")
    if not inputFolder:
        inputFolder = "input"
    outputFolder = input("Please specify the relative output folder name.\nJust press Enter to use the default value \"output\".\n")
    if not outputFolder:
        outputFolder = "output"

    UnifyPictureNames(inputFolder, outputFolder)

    logging.info("{0} - ##### Execution Finished #####\n".format(GetFormattedDatetimeNow()))

except Exception as e:
    logging.exception("{0} - {1}".format(GetFormattedDatetimeNow(), e))
