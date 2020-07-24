from docx import Document
import os

def create_doc(_output_folder, _file, _img_text):
    
    # print (f'{_output_folder} {_file} {_img_text}')

    filename, ext = os.path.splitext(_file)
    output_filename = os.path.join(_output_folder, filename + '.docx')
    
    try:
        document = Document()
        print (f'Creating {filename}.docx')
        document.add_paragraph(_img_text)
        document.save(output_filename)
        print (f'{filename}.docx saved...')
    except Exception:
        print (f'something went wrong while writing {filename}.docx')

    