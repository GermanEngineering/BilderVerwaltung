import exifread
import os
import Progress
import ImageManagement as IM


def UnifyPictureNames(inputFolder, outputFolder):
	processedFiles = 0
	renamedFiles = 0
	unchangedFiles = 0	
	allFilePaths = IM.GetListOfAllFilePaths(inputFolder)
	for filePath in allFilePaths:
		inputDirectory, inputFile = os.path.split(filePath)
		if inputFile.lower().endswith(('.png', '.jpg', '.jpeg')):
			# get file metadata
			metadata = exifread.process_file(open(filePath, "rb"))
			captureTime = ""
			try:
				captureTime = str(metadata["EXIF DateTimeOriginal"])
			except Exception:
				logger.info("No capture time found for: \"{}\"".format(filePath))
				
			# pictures with creation timestamp
			if captureTime != "":
				_, fileExtension = os.path.splitext(inputFile)
				newFile = captureTime.replace(":", "").replace(" ", "_") + fileExtension.lower()
				IM.CopyFile(filePath, IM.GetUniqueFile(os.path.join(inputDirectory.replace(inputFolder, outputFolder), newFile)))
				logger.debug("{} --> {}".format(filePath, os.path.join(inputDirectory.replace(inputFolder, outputFolder), newFile)))
				renamedFiles += 1                
			# WhatsApp images
			elif "WA" in inputFile:
				newFile = inputFile.replace("IMG-", "")
				IM.CopyFile(filePath, IM.GetUniqueFile(os.path.join(inputDirectory.replace(inputFolder, outputFolder), newFile)))
				logger.debug("{} --> {}".format(filePath, os.path.join(inputDirectory.replace(inputFolder, outputFolder), newFile)))
				renamedFiles += 1
			# files without creation timestamp
			else:
				IM.CopyFile(filePath, IM.GetUniqueFile(filePath.replace(inputFolder, outputFolder)))
				unchangedFiles += 1
		else:
			IM.CopyFile(filePath, IM.GetUniqueFile(filePath.replace(inputFolder, outputFolder)))
			unchangedFiles += 1

		processedFiles += 1
		Progress.PrintProgress(processedFiles)

	logger.info("Processed Files: {} | RenamedFiles: {} | Unchanged Files: {}".format(processedFiles, renamedFiles, unchangedFiles))


try:
	logger = IM.GetLogger("UnifyPictureNames")
	logger.info("##### Program Start #####")
	
	#print("This program will help you to save and present pictures from different camera vendors in a chronological order by unifying their names.")
	print("Dieses Program speichert Bilder mit dem Aufnahmedatum als Dateiname.")
	inputFolder = IM.GetInputFolder()
	outputFolder = IM.GetOutputFolder()
	UnifyPictureNames(inputFolder, outputFolder)
	
	logger.info("##### Execution Finished #####")

except Exception as ex:
	logger.exception(ex)
