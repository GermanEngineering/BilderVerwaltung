import os
from datetime import datetime
import Progress
import piexif
import ImageManagement as IM


def SetNameAsCaptureDate(inputFolder, outputFolder):
	processedFiles = 0
	changedFiles = 0
	unchangedFiles = 0
	allFilePaths = IM.GetListOfAllFilePaths(inputFolder)
	for filePath in allFilePaths:
		inputDirectory, inputFile = os.path.split(filePath)
		newFilePath = IM.GetUniqueFile(filePath.replace(inputFolder, outputFolder))

		IM.CopyFile(filePath, newFilePath)

		if inputFile.lower().endswith((".jpg", ".jpeg")):                
			try:
				captureTime = datetime.strptime(inputFile[0:15], "%Y%m%d_%H%M%S")
			except Exception:
				try:
					captureTime = datetime.strptime(inputFile[0:8], "%Y%m%d")
				except Exception:
					logger.info("Unable to set capture time for: \"{}\"".format(filePath))
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

	logger.info("Processed Files: {} | ChangedFiles: {} | Unchanged Files: {}".format(processedFiles, changedFiles, unchangedFiles))


try:
	logger = IM.GetLogger("SetNameAsCaptureDate")
	logger.info("##### Program Start #####")
	
	#print("This program will take file names in the format YYYYMMDD_hhmmss and set them as capture date of .jpg images.\n")
	print("Dieses Program nimmt den Namen von .jpg Bildern im Format YYYYMMDD_hhmmss und setzt diesen als Aufnahmedatum.\n")
	inputFolder = IM.GetInputFolder()
	outputFolder = IM.GetOutputFolder()
	SetNameAsCaptureDate(inputFolder, outputFolder)
	
	logger.info("##### Execution Finished #####")

except Exception as ex:
	logger.exception(ex)
