import os
import Progress
from PIL import Image
import ImageManagement as IM


def ReduceImageFileSize(inputFolder, outputFolder, imageQuality):
	processedFiles = 0
	changedFiles = 0
	unchangedFiles = 0
	allFilePaths = IM.GetListOfAllFilePaths(inputFolder)
	for filePath in allFilePaths:
		inputDirectory, inputFile = os.path.split(filePath)
		newFilePath = IM.GetUniqueFile(filePath.replace(inputFolder, outputFolder))

		if inputFile.lower().endswith((".jpg", ".jpeg")):
			try:
				img = Image.open(filePath)
				img.save(newFilePath, quality=imageQuality)                    
				changedFiles += 1

			except Exception:
				logger.info("The following file could not be processed: \"{}\"".format(filePath))

		else:
			IM.CopyFile(filePath, newFilePath)
			unchangedFiles += 1

		processedFiles += 1
		Progress.PrintProgress(processedFiles)

	logger.info("Processed Files: {} | ChangedFiles: {} | Unchanged Files: {}".format(processedFiles, changedFiles, unchangedFiles))


try:
	logger = IM.GetLogger("ReduceImageFileSize")
	logger.info("##### Program Start #####")
	
	#print("This program will reduce the quality and hence the filesize of .jpg images.\n")
	print("Dieses Program verringert die Qualität und dadurch die Dateigröße von .jpg Bildern.")
	inputFolder = IM.GetInputFolder()
	outputFolder = IM.GetOutputFolder()
	#imageQuality = input("Please enter the desired quality (between 1 (low) and 95 (high)).\nJust press Enter to use the default value: 75.\n")
	imageQuality = input("Bitte gib die gewünschte Qualität (als Wert zwischen 1 (gering) und 95 (hoch)) an.\nDrücke Enter um die Standard-Einstellung 75 zu verwenden.\n")
	if not imageQuality:
		imageQuality = 75
	else:
		imageQuality = int(imageQuality)
		
	ReduceImageFileSize(inputFolder, outputFolder, imageQuality)

	logger.info("##### Execution Finished #####")

except Exception as ex:
	logger.exception(ex)
