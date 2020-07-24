import os

from ocr import imgocr
from check_input import check_for_images
from get_images import get_image_files

def main():
    input_folder = os.getcwd() + '/input'
    output_folder = os.getcwd() + '/output'
    input_extensions = ['']

    #Check if there is an input folder
    if not os.path.exists(input_folder):
        print('Place your images files inside the \'input\' folder.' )
        os.makedirs(input_folder)
        exit(1)

    #check if input folder has any image files
    if not check_for_images(input_folder):
        print('There are no images with the following extensions in the input folder: .png, .jpg, .jpeg, .tiff, .bmp, .jfif')
        exit(1)

    # Create output folder if no output folder is present
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # get a list of all the image files in the folder
    image_files = get_image_files(input_folder)

    print(image_files)

    
    
if __name__ == '__main__':
    main()
