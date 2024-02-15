from PIL import Image
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def resize_images(input_folder, output_folder, scale_percent):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):  # Add more extensions if needed
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            img = Image.open(input_path)
            
            # Calculate the new dimensions while maintaining aspect ratio
            width, height = img.size
            new_width = int(width * scale_percent / 100)
            new_height = int(height * scale_percent / 100)

            # Resize the image
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)

            # Save the resized image
            resized_img.save(output_path)

if __name__ == "__main__":
    input_folder = "/Users/bhavanbhatt/Documents/IT492_RecSys/archive/Images/Images/"
    output_folder = "/Users/bhavanbhatt/Documents/IT492_RecSys/archive/Compressed/"
    scale_percent = 25  # Adjust this value as needed

    resize_images(input_folder, output_folder, scale_percent)
