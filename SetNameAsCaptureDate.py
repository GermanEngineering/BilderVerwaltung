import os
from datetime import datetime
import logging
import Progress
import piexif
import BilderVerwaltung as BV


def SetNameAsCaptureDate(inputFolder, outputFolder):
	processedFiles = 0
	changedFiles = 0
	unchangedFiles = 0
	allFilePaths = BV.GetListOfAllFilePaths(inputFolder)
	for filePath in allFilePaths:
		inputDirectory, inputFile = os.path.split(filePath)
		newFilePath = BV.GetUniqueFile(filePath.replace(inputFolder, outputFolder))

		BV.CopyFile(filePath, newFilePath)

		if inputFile.lower().endswith((".jpg", ".jpeg")):                
			try:
				captureTime = datetime.strptime(inputFile[0:15], "%Y%m%d_%H%M%S")
			except Exception:
				try:
					captureTime = datetime.strptime(inputFile[0:8], "%Y%m%d")
				except Exception:
					logging.info("{0} - Unable to set capture time for: \"{1}\"".format(BV.GetFormattedDatetimeNow(), filePath))
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

	logging.info("{0} - Processed Files: {1} | ChangedFiles: {2} | Unchanged Files: {3}".format(BV.GetFormattedDatetimeNow(), processedFiles, changedFiles, unchangedFiles))


try:
	logging.basicConfig(filename="SetNameAsCaptureDate.log", level=logging.INFO)
	logging.info("{0} - ##### Program Start #####".format(BV.GetFormattedDatetimeNow()))

	print("This program will take file names in the format YYYYMMDD_hhmmss and set them as capture date of .jpg images.\n")
	inputFolder = BV.GetInputFolder()
	outputFolder = BV.GetOutputFolder()
	SetNameAsCaptureDate(inputFolder, outputFolder)

	logging.info("{0} - ##### Execution Finished #####\n".format(BV.GetFormattedDatetimeNow()))

except Exception as e:
	logging.exception("{0} - {1}".format(BV.GetFormattedDatetimeNow(), e))
