import os
from datetime import datetime, timedelta
import Progress
import piexif
import ImageManagement as IM


def ChangeCaptureDate(inputFolder, outputFolder, timeDifferenceInSeconds):
	processedFiles = 0
	changedFiles = 0
	unchangedFiles = 0	
	allFilePaths = IM.GetListOfAllFilePaths(inputFolder)
	for filePath in allFilePaths:
		inputDirectory, inputFile = os.path.split(filePath)
		newFilePath = IM.GetUniqueFile(filePath.replace(inputFolder, outputFolder))
		IM.CopyFile(filePath, newFilePath)

		if inputFile.lower().endswith(('.jpg', '.jpeg')):
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
				logger.info("No capture time found for: \"{}\"".format(filePath))

		else:
			unchangedFiles += 1

		processedFiles += 1
		Progress.PrintProgress(processedFiles)

	logger.info("Processed Files: {} | ChangedFiles: {} | Unchanged Files: {}".format(processedFiles, changedFiles, unchangedFiles))


try:	
	logger = IM.GetLogger("ChangeCaptureDate")
	logger.info("##### Program Start #####")
	
	#print("This program will adapt the capture date of .jpg images by the specified time difference.\n")
	print("Dieses Program verrechnet einen Offset auf die Aufnahmedaten von .jpg Bildern.")
	inputFolder = IM.GetInputFolder()
	outputFolder = IM.GetOutputFolder()
	#timeDifferenceInSeconds = input("Please enter the time difference in seconds.\nJust press Enter to use the default value: 0.\n")
	timeDifferenceInSeconds = input("Bitte gib den gewünschten Offset in Sekunden an.\nDrücke Enter um den Standard Wert 0 zu verwenden.\n")
	if not timeDifferenceInSeconds:
		timeDifferenceInSeconds = 0
	else:
		timeDifferenceInSeconds = int(timeDifferenceInSeconds)
		
	ChangeCaptureDate(inputFolder, outputFolder, timeDifferenceInSeconds)
	
	logger.info("##### Execution Finished #####")

except Exception as ex:
	logger.exception(ex)

