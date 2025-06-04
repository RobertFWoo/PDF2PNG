This program will read the PDF files in the current folder, giving each its own subfolder.
The program will then generate png images from the pdf file.
These images will be resized to 1920x1080 pixels in size at 300 dpi, regardless of original aspect ratio.
The default folder name should be PDF2PNG, and the images will be saved in a subfolder named after the pdf file.
If the folder and subfolder do not exist, they will be created.
If the folders already exists, the contents of the sub folder will be deleted and the images generated into it.
The images will be saved to that sub folder with the name of the pdf file and the page number, e.g., "example_001.png", "example_002.png", etc.
The program will give the user an option to open the folder where the images are saved after the conversion is complete.
The program will display the progress in the terminal output.
The application will terminate after processing.
