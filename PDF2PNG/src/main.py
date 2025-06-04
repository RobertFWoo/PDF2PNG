import os
import sys
import glob
import shutil
from pdf2image import convert_from_path
from PIL import Image

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def delete_existing_images(folder):
    for file in glob.glob(os.path.join(folder, '*.png')):
        os.remove(file)

def resize_image(image, size=(1920, 1080)):
    return image.resize(size, Image.Resampling.LANCZOS)

def convert_pdf_to_png(pdf_path, output_folder):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_subfolder = os.path.join(output_folder, pdf_name)

    create_directory(output_subfolder)
    delete_existing_images(output_subfolder)

    images = convert_from_path(pdf_path)
    for page_number, image in enumerate(images):
        resized_image = resize_image(image)
        image_filename = os.path.join(output_subfolder, f"{pdf_name}_{page_number + 1:03}.png")
        resized_image.save(image_filename)
        print(f"Saved: {image_filename}")

def main():
    current_folder = os.getcwd()
    output_folder = os.path.join(current_folder, 'PDF2PNG')
    create_directory(output_folder)

    pdf_files = [f for f in os.listdir(current_folder) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print("No PDF files found in the current folder.")
        sys.exit(1)

    for pdf_file in pdf_files:
        pdf_path = os.path.join(current_folder, pdf_file)
        print(f"Processing: {pdf_file}")
        convert_pdf_to_png(pdf_path, output_folder)

    print("Conversion complete.")
    open_folder = input("Do you want to open the output folder? (y/n): ")
    if open_folder.lower() == 'y':
        os.system(f'xdg-open "{output_folder}"')

if __name__ == "__main__":
    main()