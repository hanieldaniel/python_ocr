import os

import check_input
import get_images
from ocr import imgocr
import make_docx
# from 


def main():
    input_folder = os.getcwd() + '/input'
    output_folder = os.getcwd() + '/output'
    input_extensions = ['']

    # Check if there is an input folder
    if not os.path.exists(input_folder):
        print('Place your images files inside the \'input\' folder.')
        os.makedirs(input_folder)
        exit(1)

    # check if input folder has any image files
    if not check_input.check_for_images(input_folder):
        print('There are no images with the following extensions in the input folder: .png, .jpg, .jpeg, .tiff, .bmp, .jfif')
        exit(1)

    # Create output folder if no output folder is present
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # get a list of all the image files in the folder
    image_files = get_images.get_image_files(input_folder)

    for image in image_files:
        img_text = imgocr(input_folder, image)
        make_docx.create_doc(output_folder, image, img_text)


if __name__ == '__main__':
    main()
