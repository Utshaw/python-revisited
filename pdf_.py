#!/usr/bin/env python3
import PyPDF2
import os
pdfFile = open('meetingminutes.pdf', 'rb') # read binary mode
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages) # total pages in the pdf
page = reader.getPage(0) # get a page on the pdf
pageText = page.extractText()
print(pageText)

def readPdf(fileName):
    pdfFile = open(fileName, 'rb')
    reader = PyPDF2.PdfFileReader(pdfFile)
    for pageNum in range(reader.numPages):
        print(pageNum)
        print(reader.getPage(pageNum).extractText())

def mergePDF(pdf1Name, pdf2Name):
    pdf1File = open(pdf1Name, 'rb')
    pdf2File = open(pdf2Name, 'rb')
    reader1 = PyPDF2.PdfFileReader(pdf1File)
    reader2 = PyPDF2.PdfFileReader(pdf2File)
    writer = PyPDF2.PdfFileWriter()
    for pageNum in range(reader1.numPages):
        page = reader1.getPage(pageNum)
        writer.addPage(page)
    
    for pageNum in range(reader2.numPages):
        page = reader2.getPage(pageNum)
        writer.addPage(page)
    outputFile = open('mergedPDF', 'wb')
    writer.write(outputFile)
    outputFile.close()
    pdf1File.close()
    pdf2File.close()


# readPdf('meetingminutes.pdf')
mergePDF('meetingminutes.pdf', 'meetingminutes2.pdf')