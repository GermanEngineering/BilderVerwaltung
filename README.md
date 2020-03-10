# Unify Picture Names
This program will help you to save and present pictures from different camera vendors in a chronological order by unifying their names.

## Downloads:
Clone or download the [Git Repository](https://github.com/GermanEngineering/UnifyPictureNames) or from my website:<br>
For Windows:<br>
[20190130 - UnifyPictureNames.exe](https://trustmeimanengineer.de/wp-content/uploads/2019/01/UnifyPictureNamesWindows.7z)<br>
For Linux / MAC:<br>
[20190130 - UnifyPictureNames.py](https://trustmeimanengineer.de/wp-content/uploads/2019/01/UnifyPictureNamesPython.7z)

## Application:
1. Unzip the downloaded files.
1. Execute UnifyPictureNames.exe.
1. Specify the input folder in which your images are located.
	(all subdirectories will be processed as well)
1. Specify the output folder for the results.
1. Check the output folder for the results.

The application of the program is very simple and explained in [this YouTube video](https://www.youtube.com/watch?v=A-gYWGp0qLk).
![Unify Picture Names](https://trustmeimanengineer.de/wp-content/uploads/2018/05/UnifyPictureNames.png)

## Function:
The program will go through all pictures in the specified input folder, including subfolders.<br>
Only .jpg, .jpeg and .png files will be processed, while all others will be copied without any change.<br>
Next, the program will try to get the capture date from the image exif data.<br>
Every image containing this information will then be renamed according to the following pattern: YYYYMMDD_hhmmss<br>
The renamed images will be saved into the specified output folder.

This will allow you to save or present pictures from different camera vendors in a chronological order.

I’ve already tested it successfully with LG and Samsung (Android Phone), Apple (iPhone), a Sony Camera, Android WhatsApp and GoPro images.

***

I'm frequently using this program in combination with another one helping you to automatically rotate your images into horizontal orientation.<br>
You can find more about the project on this site: [Rotate Images](https://trustmeimanengineer.de/rotate-images/).
