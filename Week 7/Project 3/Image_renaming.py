''' Project 3
Image Renaming Tool using Metadata in Python '''

import os
import subprocess
from datetime import datetime
from exiftool import ExifTool


def get_metadata(image_path):
    with ExifTool() as et:
        metadata = et.get_metadata(image_path)
    return metadata

def renameImageInDir(input_dir, output_dir, rename_pattern):
    for i in os.listdir(input_dir):                             # i is filename
        if i.lower().endswith(('.jpg','.jpeg','.png','.gif')):
            image_path = os.path.join(input_dir, i)
            renameImage(image_path, output_dir, rename_pattern)
            
def renameImage(image_path, output_dir, rename_pattern):
    metadata = get_metadata(image_path)
    
    #extract metadata
    date = metadata.get('EXIF:DateTimeOrigindal','')[:10]
    time = metadata.get('EXIF:DateTimeOrigindal','')[11:]
    camera = metadata.get('EXIF:Model','')
    location = metadata.get('GPS:GPSLatitude','') + ', ' + metadata.get('GPS:GPSLongitude','')
    
    new_file_name = rename_pattern.format(date=date, time=time, camera=camera, location=location)

    new_image_path = os.path.join(output_dir, new_file_name)
    os.rename(image_path, new_image_path)

def main():
    input_dir = input("Enter input directory path: ")
    output_dir = input("Enter output directory path: ")
    rename_pattern = input("Enter rename pattern: ")
    renameImageInDir(input_dir, output_dir, rename_pattern)

if __name__ == "__main__":
    main()