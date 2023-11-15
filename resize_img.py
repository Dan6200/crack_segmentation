import os
from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)

def resize_images_in_dir(input_dir, output_dir, size):
    # Get a list of all the image files in the input_dir
    image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    # Loop through all the images and resize them
    for image_file in image_files:
        input_image_path = os.path.join(input_dir, image_file)
        output_image_path = os.path.join(output_dir, image_file)
        resize_image(input_image_path, output_image_path, size)

# Call the function
resize_images_in_dir('./my_crack_imgs', './my_crack_imgs', (448, 448))

