from PIL import Image

def is_grayscale(image_path):
    img = Image.open(image_path).convert('RGB')
    w, h = img.size
    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i,j))
            if r != g != b: return False
    return True

def check_imgs_in_dir(input_dir):
    # Get a list of all the image files in the input_dir
    image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    # Loop through all the images and check if they are grayscale
    for image_file in image_files:
        input_image_path = os.path.join(input_dir, image_file)
        if is_grayscale(input_image_path):
            print(f"{image_file} is grayscale")
        else:
            print(f"{image_file} is not grayscale")

check_imgs_in_dir('./my_crack_imgs')
