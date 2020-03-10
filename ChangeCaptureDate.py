import os
from datetime import datetime, timedelta
import logging
import Progress
import piexif
import BilderVerwaltung as BV


def ChangeCaptureDate(inputFolder, outputFolder, timeDifferenceInSeconds):
	processedFiles = 0
	changedFiles = 0
	unchangedFiles = 0	
	allFilePaths = BV.GetListOfAllFilePaths(inputFolder)
	for filePath in allFilePaths:
		inputDirectory, inputFile = os.path.split(filePath)
		newFilePath = BV.GetUniqueFile(filePath.replace(inputFolder, outputFolder))
		BV.CopyFile(filePath, newFilePath)

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
				logging.info("{0} - No capture time found for: \"{1}\"".format(BV.GetFormattedDatetimeNow(), filePath))

		else:
			unchangedFiles += 1

		processedFiles += 1
		Progress.PrintProgress(processedFiles)

	logging.info("{0} - Processed Files: {1} | ChangedFiles: {2} | Unchanged Files: {3}".format(BV.GetFormattedDatetimeNow(), processedFiles, changedFiles, unchangedFiles))


try:
	logging.basicConfig(filename="ChangeCaptureDate.log", level=logging.INFO)
	logging.info("{0} - ##### Program Start #####".format(BV.GetFormattedDatetimeNow()))

	print("This program will adapt the capture date of .jpg images by the specified time difference.\n")
	inputFolder = BV.GetInputFolder()
	outputFolder = BV.GetOutputFolder()
	timeDifferenceInSeconds = input("Please enter the time difference in seconds.\nJust press Enter to use the default value: 0.\n")
	if not timeDifferenceInSeconds:
		timeDifferenceInSeconds = 0
	else:
		timeDifferenceInSeconds = int(timeDifferenceInSeconds)
		
	ChangeCaptureDate(inputFolder, outputFolder, timeDifferenceInSeconds)

	logging.info("{0} - ##### Execution Finished #####\n".format(BV.GetFormattedDatetimeNow()))

except Exception as e:
	logging.exception("{0} - {1}".format(BV.GetFormattedDatetimeNow(), e))

