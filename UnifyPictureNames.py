import exifread
import os
import logging
import Progress
import BilderVerwaltung as BV


def UnifyPictureNames(inputFolder, outputFolder):
	processedFiles = 0
	renamedFiles = 0
	unchangedFiles = 0	
	allFilePaths = BV.GetListOfAllFilePaths(inputFolder)
	for filePath in allFilePaths:
		inputDirectory, inputFile = os.path.split(filePath)
		if inputFile.lower().endswith(('.png', '.jpg', '.jpeg')):
			# get file metadata
			metadata = exifread.process_file(open(filePath, "rb"))
			captureTime = ""
			try:
				captureTime = str(metadata["EXIF DateTimeOriginal"])
			except Exception:
				logging.info("{0} - No capture time found for: \"{1}\"".format(BV.GetFormattedDatetimeNow(), filePath))
				
			# pictures with creation timestamp
			if captureTime != "":
				_, fileExtension = os.path.splitext(inputFile)
				newFile = captureTime.replace(":", "").replace(" ", "_") + fileExtension.lower()
				BV.CopyFile(filePath, BV.GetUniqueFile(os.path.join(inputDirectory.replace(inputFolder, outputFolder), newFile)))
				logging.debug("{0} - {1} --> {2}".format(BV.GetFormattedDatetimeNow(), filePath, os.path.join(inputDirectory.replace(inputFolder, outputFolder), newFile)))
				renamedFiles += 1                
			# WhatsApp images
			elif "WA" in inputFile:
				newFile = inputFile.replace("IMG-", "")
				BV.CopyFile(filePath, BV.GetUniqueFile(os.path.join(inputDirectory.replace(inputFolder, outputFolder), newFile)))
				logging.debug("{0} - {1} --> {2}".format(BV.GetFormattedDatetimeNow(), filePath, os.path.join(inputDirectory.replace(inputFolder, outputFolder), newFile)))
				renamedFiles += 1
			# files without creation timestamp
			else:
				BV.CopyFile(filePath, BV.GetUniqueFile(filePath.replace(inputFolder, outputFolder)))
				unchangedFiles += 1
		else:
			BV.CopyFile(filePath, BV.GetUniqueFile(filePath.replace(inputFolder, outputFolder)))
			unchangedFiles += 1

		processedFiles += 1
		Progress.PrintProgress(processedFiles)

	logging.info("{0} - Processed Files: {1} | RenamedFiles: {2} | Unchanged Files: {3}".format(BV.GetFormattedDatetimeNow(), processedFiles, renamedFiles, unchangedFiles))


try:
	logging.basicConfig(filename="UnifyPictureNames.log", level=logging.INFO)
	logging.info("{0} - ##### Program Start #####".format(BV.GetFormattedDatetimeNow()))

	inputFolder = BV.GetInputFolder()
	outputFolder = BV.GetOutputFolder()
	UnifyPictureNames(inputFolder, outputFolder)

	logging.info("{0} - ##### Execution Finished #####\n".format(BV.GetFormattedDatetimeNow()))

except Exception as e:
	logging.exception("{0} - {1}".format(BV.GetFormattedDatetimeNow(), e))
