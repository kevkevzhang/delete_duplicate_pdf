# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import PyPDF2
import os
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
import base64


if __name__ == '__main__':
    print("hi")
    pdf_path = (Path.home()/"Downloads"/"ACHEM Fall 2020 Lectures.pdf")

    pdf = PdfFileReader(str(pdf_path))

    print(pdf.getNumPages())

    print(pdf.getPage(1096).extractText())
    print(pdf.getPage(32).extractText())

    pages = dict()
    output_PDF = PdfFileWriter()

    for page in pdf.pages:
        duplicate = True
        page_line = page.extractText()
        i = pdf.getPageNumber(page) + 1
        print( "page number " + str(i))
        if page_line == "":
            pages[page_line] = i
            output_PDF.addPage(page)
            print("New page")
        elif page_line in pages:
            print("page " + str(i) + " is a duplicate to " + str(pages[page_line]))
        else:
            pages[page_line] = i
            output_PDF.addPage(page)
            print("New page")
    newFile = open("shortned.pdf",'wb')
    output_PDF.write(newFile)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
