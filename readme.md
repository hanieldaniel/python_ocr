# Python OCR - Image to docx - file by file

Implementation of OCR(Optical Character Recognition) using tesseract using Python

## Reason for doing this project

-One of my friends is doing a transription job where he has transcribe about 500 print images into individual doc files.

### Things I intend to do
    - Create .docx files for each of the 500 image files
    - Learn a bit of python along the way

## Installation:
### Install tesserct-ocr using this command:
    - On Ubuntu
      ```
      sudo apt-get install tesseract-ocr
      ```
    - On Mac
      ```
      brew install tesseract
      ```
    - On Windows, download installer from [here](https://github.com/UB-Mannheim/tesseract/wiki)

### Install the requirments
```
pip install -r requirements.txt
```

### Run

1. Place your image files inside the 'input' folder. Currently recursive searching in subdirectories will not been implemented
2. Run the 'main.py' file using:
   ```
   py main.py
   ```
3. Have fun playing around with the code.