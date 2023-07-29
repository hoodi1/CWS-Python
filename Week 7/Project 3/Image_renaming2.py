import os
import subprocess

def extract_metadata(image_path):
    # Use ExifTool to extract metadata from the image file
    command = ['exiftool', image_path]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    metadata = {}
    for line in result.stdout.strip().split('\n'):
        key, value = line.split(':', 1)
        metadata[key.strip()] = value.strip()
    return metadata

def rename_image_with_metadata(image_path, output_dir, renaming_pattern):
    # Extract metadata from the image file
    metadata = extract_metadata(image_path)

    # Get the relevant metadata fields (you can customize this based on your needs)
    date_time = metadata.get('DateTimeOriginal', 'Unknown_DateTime')
    camera_model = metadata.get('Model', 'Unknown_Model')
    location = metadata.get('Location', 'Unknown_Location')

    # Create the new filename using the specified pattern
    new_filename = renaming_pattern.format(date_time=date_time,
                                           camera_model=camera_model,
                                           location=location)
    
    # Join the output directory path and the new filename
    new_image_path = os.path.join(output_dir, new_filename)

    # Rename the image file
    os.rename(image_path, new_image_path)

def batch_rename_images(input_dir, output_dir, renaming_pattern):
    # Loop through all image files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(input_dir, filename)
            rename_image_with_metadata(image_path, output_dir, renaming_pattern)

if __name__ == "__main__":
    # Get input and output directories from the user
    input_directory = input("Enter the input directory path: ")
    output_directory = input("Enter the output directory path: ")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get the renaming pattern from the user
    renaming_pattern = input("Enter the renaming pattern (use {date_time}, {camera_model}, {location}): ")

    # Call the batch_rename_images function
    batch_rename_images(input_directory, output_directory, renaming_pattern)

    print("Image renaming complete!")
