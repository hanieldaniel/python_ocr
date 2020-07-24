import os
import cv2 
import pytesseract
import numpy as np

def img_preprocessing(_img):
    kernel = np.ones((5,5),np.uint8)
    grey = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    err_dialate = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
    canny_edge_detection = cv2.Canny(err_dialate, 100, 200)

    return canny_edge_detection


def imgocr(_input_folder, _image):
    
    img_path = os.path.join(_input_folder, _image)
    img = cv2.imread(img_path)

    # Preprocessing the image
    preprocessed_img = img_preprocessing(img)

    # Adding custom options
    # custom_config = r'--oem 3 --psm 6'
    output = pytesseract.image_to_string(img)

    return output