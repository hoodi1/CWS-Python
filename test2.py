## empty dictionary
#product = {}
#
## infinite loop breaks when user asks
#while True:
#    print("1 -> Add a product ")
#    print("2 -> Update a product ")
#    print("3 -> Delete a product ")
#    print("4 -> View all product ")
#    print("5 -> Exit ")
#
#    a = int(input("Please choose an option (1-5): "))
#
#    # Add a product
#    if a == 1:
#        name = input("Enter product name: ")
#        pid = input("Enter product ID: ")
#        quant = input("Enter quantity: ")
#        price = input("Enter price: ")
#     
#        product[pid] = {"Name": name, "Quantity": quant, "Price": price}    
#        print(product)
#    # update a product
#    elif a == 2:
#        pid = int(input("Enter Product ID: "))
#        if pid in product:
#            name = input("Enter product name: ")
#            pid = input("Enter product ID: ")
#            quant = input("Enter quantity: ")
#            price = input("Enter price: ")
#            product[pid] = {"Name": name, "Quantity": quant, "Price": price}
#        else:
#            print("ID not found.")
#  
#    # Delete a product
#    elif a == 3:
#        pid = input("Enter product id: ")
#        if pid in product:
#            del product[pid]
#        else:
#            print("Expense ID not found.")
#
#    # View all products
#    elif a == 4:
#        if product:
#            for v in product.values():
#                for k,v1 in v.items():
#                    print(k,":",v1)
#                
#        else:
#            print("No Product found")
#    
#    # exit
#    elif a == 5:
#        print("Exiting the app ")
#        break
#    
#    else:
#        print("Invalid choice. Please select a valid option.\n")



import os
import subprocess
from exiftool import ExifTool

def get_metadata(image_path):
    with ExifTool() as et:
        metadata = et.get_metadata(image_path)
    return metadata

def rename_image(image_path, output_dir, renaming_pattern):
    metadata = get_metadata(image_path)

    # Extract relevant metadata fields from the 'metadata' dictionary
    date = metadata.get('EXIF:DateTimeOriginal', '')[:10]  # Get the first 10 characters for the date
    time = metadata.get('EXIF:DateTimeOriginal', '')[11:]  # Get the characters after the first 11 for the time
    camera = metadata.get('EXIF:Model', '')
    location = metadata.get('GPS:GPSLatitude', '') + ', ' + metadata.get('GPS:GPSLongitude', '')

    # Replace placeholders in the renaming pattern with actual metadata values
    new_file_name = renaming_pattern.format(date=date, time=time, camera=camera, location=location)

    new_image_path = os.path.join(output_dir, new_file_name)
    os.rename(image_path, new_image_path)


def rename_images_in_directory(input_dir, output_dir, renaming_pattern):
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(input_dir, filename)
            rename_image(image_path, output_dir, renaming_pattern)

def main():
    input_dir = input("Enter the input directory path: ")
    output_dir = input("Enter the output directory path: ")
    renaming_pattern = input("Enter the renaming pattern: ")
    rename_images_in_directory(input_dir, output_dir, renaming_pattern)

if __name__ == "__main__":
    main()

