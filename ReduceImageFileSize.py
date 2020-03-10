from shutil import copy2
import os
from datetime import datetime
import logging
import Progress
from PIL import Image


def ReduceImageFileSize(inputFolder, outputFolder, imageQuality):
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

            if file.lower().endswith((".jpg", ".jpeg")):
                try:
                    img = Image.open(filePath)
                    img.save(newFilePath, quality=imageQuality)                    
                    changedFiles += 1

                except Exception:
                    logging.info("{0} - The following file could not be processed: \"{1}\"".format(GetFormattedDatetimeNow(), filePath))

            else:                
                copy2(filePath, newFilePath) 
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
    logging.basicConfig(filename="ReduceImageFileSize.log", level=logging.INFO)
    logging.info("{0} - ##### Program Start #####".format(GetFormattedDatetimeNow()))

    print("This program will reduce the quality and hence the filesize of .jpg images.\n")
    inputFolder = input("Please specify the relative input folder name.\nJust press Enter to use the default value \"input\".\n")
    if not inputFolder:
        inputFolder = "input"
    outputFolder = input("Please specify the relative output folder name.\nJust press Enter to use the default value \"output\".\n")
    if not outputFolder:
        outputFolder = "output"
    imageQuality = input("Please enter the desired quality (between 1 (low) and 95 (high)).\nJust press Enter to use the default value: 75.\n")
    if not imageQuality:
        imageQuality = 75
    else:
        imageQuality = int(imageQuality)
        
    ReduceImageFileSize(inputFolder, outputFolder, imageQuality)

    logging.info("{0} - ##### Execution Finished #####\n".format(GetFormattedDatetimeNow()))

except Exception as e:
    logging.exception("{0} - {1}".format(GetFormattedDatetimeNow(), e))
