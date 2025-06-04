import os
import shutil
from PIL import Image

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def delete_existing_images(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    create_directory(folder_path)

def resize_image(image_path, output_path, size=(1920, 1080)):
    with Image.open(image_path) as img:
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)