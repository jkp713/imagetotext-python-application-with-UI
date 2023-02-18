import tkinter as tk
from tkinter import *

window=Tk()

from tkinter import filedialog
from PIL import Image


#define the function to execute securitycam.py script, first import the securitycam.py module as following

def imagetotext():

    from pytesseract import pytesseract
    #Define path to tessarect
    path_to_tesseract = 'C://Program Files//Tesseract-OCR//tesseract.exe'
    
    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract
 
    filetypes = (
        ('Text files', '*.TXT'),
        ('All files', '*.*'),
    )

    root = tk.Tk()
    filedir = tk.filedialog.askopenfilename(
        title='Select a file...',
        filetypes=filetypes,
    )
    root.destroy()
    
    #Open image with PIL
    img = Image.open(filedir)
    
    text = pytesseract.image_to_string(img)
    
    print(text)
    
    f = open("myfile.txt", "x")
    
    f.write(text)
    f.close()

    
#put a button named 'Transform' which will execute the securitycam module when clicked
btn=Button(window, text="Transform", fg='blue', bg = "white", font=("Helvetica", 8),command = imagetotext)

#define positions of the button
btn.place(x=80, y=100)

#define window title
window.title('Image tot Text')

#define window geonmetry
window.geometry("300x200+10+20")
window.mainloop()