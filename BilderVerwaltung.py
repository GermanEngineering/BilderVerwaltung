import os
from datetime import datetime
from shutil import copy2


def GetFormattedDatetimeNow():
	"""Returns the current datetime in format YYYYMMDD_hhmmss"""
	return datetime.now().strftime("%Y%m%d_%H%M%S")


def GetUniqueFile(filePath):
	"""Check if file already exists and rename if needed."""
	directory, file = os.path.split(filePath)
	fileName, fileExtension = os.path.splitext(file)
	if os.path.isfile(filePath):
		fileNumber = 2
		while os.path.isfile("{}\\{}_{}{}".format(directory, fileName, fileNumber, fileExtension)):
			fileNumber += 1
		filePath = "{}\\{}_{}{}".format(directory, fileName, fileNumber, fileExtension)

	return filePath


def GetInputFolder():
	"""Asks the user for the input folder name."""
	inputFolder = input("Please specify the relative input folder name.\nJust press Enter to use the default value \"input\".\n")
	if not inputFolder:
		inputFolder = "input"

	return inputFolder

def GetOutputFolder():
	"""Asks the user for the input folder name."""
	outputFolder = input("Please specify the relative output folder name.\nJust press Enter to use the default value \"output\".\n")
	if not outputFolder:
		outputFolder = "output"

	return outputFolder


def GetListOfAllFilePaths(root):
	"""Returns a list of all files in the specified folder and all its sub folders."""
	allFilePaths = []
	for path, subDirectories, files in os.walk(root):
		for file in files:
			allFilePaths.append(os.path.join(path, file))
	
	return allFilePaths


def CopyFile(source, target):
	"""Copy file from source to target and print name of file to console."""
	if not os.path.exists(os.path.dirname(target)):
		os.makedirs(os.path.dirname(target))
	copy2(source, target)

