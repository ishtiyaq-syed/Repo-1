
### This code lets you search for the file with your name in a folder fo pdfs
### Dev : Ishtiyaq Syed
### Version : 1.0

import os
import PyPDF2


def find_pdf_with_name(folder_path, name):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                with open(pdf_path, 'rb') as f:
                    pdf = PyPDF2.PdfReader(f)
                    for page in pdf.pages:
                        text = page.extract_text()
                        if name.lower() in text.lower():
                            print(f"Found your name in: {pdf_path}")
                            return
    print("Your name was not found in any PDF files.")


# Specify the folder path and your name
folder_path = input("Enter the full path")
name = input("Enter the name")

find_pdf_with_name(folder_path, name)
