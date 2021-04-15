import PyPDF2
import os
# import fitz  # this is pymupdf

from tika import parser


APP_DIR = os.getcwd()
# Instantiates a client
# C:\Users\micha\Projects\google_speech\texts\asistenti_pedagoga_zaver.txt
theme_name = 'Stav_skolstvi_v_cechach_2008'
file_name = f'{APP_DIR}\\texts\\{theme_name}.pdf'

# mnoho chyb
# pdfFileObject = open(file_name, 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
# count = pdfReader.numPages
# for i in range(count):
#     page = pdfReader.getPage(i)
#     print(page.extractText())

# ještě horší
# with fitz.open(file_name) as doc:
#     text = ""
#     for page in doc:
#         text += page.getText()

# print(text)

raw = parser.from_file(file_name)
raw = str(raw)

safe_text = raw.encode('utf-8', errors='ignore')

safe_text = str(safe_text).replace("\n", "").replace("\\", "")
print('--- safe text ---' )
print( safe_text )