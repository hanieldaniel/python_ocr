import os

def get_image_files(_folder):

    if os.path.isdir(_folder):
        ext_filter_set = {'.png', '.jpg', '.jpeg', '.jfif', '.tiff', '.bmp'}
        file_list = os.listdir(_folder)
        output = []

        for file in file_list:
            filename, ext = os.path.splitext(file)
            if ext in ext_filter_set:
                output.append(file)
        return output

    else:
        print('The inupt path is not a folder')
        exit(1)
