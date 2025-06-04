# PDF2PNG

PDF2PNG is a Python application that converts PDF files into PNG images. The images are resized to 1920x1080 pixels, and the application manages the folder structure for saving the images efficiently.

## Features

- Reads PDF files from the current folder.
- Generates PNG images from each page of the PDF.
- Resizes images to 1920x1080 pixels, maintaining the aspect ratio.
- Creates a default output folder named `PDF2PNG` with a subfolder named after the PDF file.
- Deletes existing images in the output subfolder before saving new ones.
- Provides terminal output to display progress during conversion.
- Offers an option to open the output folder after processing is complete.

## Requirements

To run this application, you need to install the following dependencies:

- [Pillow](https://pypi.org/project/Pillow/): For image processing.
- [PyMuPDF](https://pypi.org/project/PyMuPDF/): For reading PDF files.

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Usage

1. Place the PDF file you want to convert in the current directory.
2. Run the application:

```
python src/main.py
```

3. Follow the terminal prompts to complete the conversion.
4. After processing, you can choose to open the folder where the images are saved.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.