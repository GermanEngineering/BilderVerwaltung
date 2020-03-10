import os
import logging
import Progress
from PIL import Image
import BilderVerwaltung as BV


def ReduceImageFileSize(inputFolder, outputFolder, imageQuality):
	processedFiles = 0
	changedFiles = 0
	unchangedFiles = 0
	allFilePaths = BV.GetListOfAllFilePaths(inputFolder)
	for filePath in allFilePaths:
		inputDirectory, inputFile = os.path.split(filePath)
		newFilePath = BV.GetUniqueFile(filePath.replace(inputFolder, outputFolder))

		if inputFile.lower().endswith((".jpg", ".jpeg")):
			try:
				img = Image.open(filePath)
				img.save(newFilePath, quality=imageQuality)                    
				changedFiles += 1

			except Exception:
				logging.info("{0} - The following file could not be processed: \"{1}\"".format(BV.GetFormattedDatetimeNow(), filePath))

		else:
			BV.CopyFile(filePath, newFilePath)
			unchangedFiles += 1

		processedFiles += 1
		Progress.PrintProgress(processedFiles)

	logging.info("{0} - Processed Files: {1} | ChangedFiles: {2} | Unchanged Files: {3}".format(BV.GetFormattedDatetimeNow(), processedFiles, changedFiles, unchangedFiles))


try:
	logging.basicConfig(filename="ReduceImageFileSize.log", level=logging.INFO)
	logging.info("{0} - ##### Program Start #####".format(BV.GetFormattedDatetimeNow()))

	print("This program will reduce the quality and hence the filesize of .jpg images.\n")
	inputFolder = BV.GetInputFolder()
	outputFolder = BV.GetOutputFolder()
	imageQuality = input("Please enter the desired quality (between 1 (low) and 95 (high)).\nJust press Enter to use the default value: 75.\n")
	if not imageQuality:
		imageQuality = 75
	else:
		imageQuality = int(imageQuality)
		
	ReduceImageFileSize(inputFolder, outputFolder, imageQuality)

	logging.info("{0} - ##### Execution Finished #####\n".format(BV.GetFormattedDatetimeNow()))

except Exception as e:
	logging.exception("{0} - {1}".format(BV.GetFormattedDatetimeNow(), e))
