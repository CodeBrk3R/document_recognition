import PySimpleGUI as sg
import sys
from PIL import Image
import pytesseract
import PyPDF2

#locate pytesseract binary for PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\mike\Anaconda3\Lib\tesseract.exe'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

#convert pdf to text function
def read_pdf(filename):
    opened_pdf = PyPDF2.PdfFileReader(filename, 'rb')
    if opened_pdf.isEncrypted:
        opened_pdf.decrypt('')
    Pages_cnt = opened_pdf.getNumPages()
    x=0
    while x < Pages_cnt:
        data = opened_pdf.getPage(x).extractText()
        print(f'-----------------------THIS IS PAGE {x}--------------------\n')
        print(data)
        x=x+1 

#process image function
def ocr_core(filename):
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    text = pytesseract.image_to_string(Image.open(filename))  
    return text



##COMPARISON DOCS
aoi_doc = """The name ofthe corporation is
ARTICLE
Duration

“The period of the corporation's duration is

ARTICLE
Purpose

‘The purpose for which the corporation is organized isto conduct any and al awful
‘business for which corporations canbe organized pursuant to statute,
Including but not limited to:

ARTICLE IV
Powers,

“The corporation has the power to engage in any lawful activity under the corporation code of
the State of. Including opening and operating a bank account.
"""








##APP LOOP
while True:
    try:
        #get file input
        fname = sg.popup_get_file('Document to open')

        #check file input and return filename as popup
        if not fname:
            sg.popup("Cancel", "No filename supplied")
            raise SystemExit("Cancelling: no filename supplied")
            break
        else:
            if fname.split('.')[1] in ALLOWED_EXTENSIONS:
                sg.popup('The filename you chose was', fname)
                #print text from image
                print(ocr_core(fname))

                if aoi_doc in ocr_core(fname):
                    print("\nTHIS IS ARTICLES OF INCORPORATION\n\n")
                else:
                    print("\nNO DOC MATCH\n\n")

            elif fname.split('.')[1] == 'pdf':
                if aoi_doc in read_pdf(fname):
                    print("\nTHIS IS ARTICLES OF INCORPORATION\n\n")
                else:
                    print("\nNO DOC MATCH\n\n")


            else:
                sg.popup("Cancel", "Incorrect format supplied")
                raise SystemExit("Cancelling: no filename supplied")
                break
    except NotImplementedError:
        print("PDF type not supported")
        break
