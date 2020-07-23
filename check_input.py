import os

def check_for_images(_folder):
    """
        Check if image files are present in the provided folder
    """

    has_image_file = False
    image_extensions = {'.png', '.jpg', '.jpeg', '.tiff', '.bmp'}

    try:
        all_files = os.listdir(_folder)

        if all_files == []:
            return False

        else:
            for file in all_files:
                filename, ext = os.path.splitext(file)

                if ext in image_extensions:
                    has_image_file = True
                    break
                else:
                    pass

            return has_image_file
    
    except OSError:
        print('Check if that is a valid folder')
        exit(1)
    
