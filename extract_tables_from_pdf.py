#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import camelot
import PyPDF2
from PyPDF2 import PdfReader
import pandas as pd

path = r'C:\Users\Nowy_użytkownik\Desktop\kursy_walut'
#creating list to store all pdf files in folder
pdf_files = []
#looping through pdf files in directory and appending them to the list
for file in os.listdir(path):
    if file.endswith('.pdf'):
        pdf_files.append(file)

#looping through the list of pdf files
for file in pdf_files:
    pdf_read = PyPDF2.PdfReader(path + '\\' + file, 'rb')
    #getting first page of each file
    page = pdf_read.pages[0]
    #extracting text from file
    txt = page.extract_text()
    #splitting text on '\n' sign 
    list_txt = txt.split("\n")
    #grabing first line of the text 
    title = list_txt[0]
    #taking part of the first line of text to use as a sheet name
    s_name = title[:20]
    #using camelot library to read tables from file
    tbl = camelot.read_pdf(path + '\\' + file)
    #grabing first table and converting to data frame
    tbl_df = tbl[0].df
    #removing unnecessary column
    tbl_df = tbl_df.drop(4, axis=1)
    #saving table to excel file 
    tbl_df.to_excel(path + "\\" + file[:-4] +'.xlsx', sheet_name=s_name, header=False, index=False )

