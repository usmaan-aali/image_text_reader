#loading libraries for the reading the text from image
from PIL import Image
from pytesseract import *

#path to the pytesseract library
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#looping to read all of the images one by one
for x in range(1322,1521):
    #loading the image to read
    img = Image.open(f'Data\IMG_{x}.jpeg')

    #Reading text from image
    output = pytesseract.image_to_string(img)

    #appending the text to a file
    f = open("text_readed.txt","a")
    f.write(output)
    f.close
