import PyPDF2

pdf=open("D:\Sample_Patient.pdf",'rb')
pdfreader=PyPDF2.PdfFileReader(pdf)
pages=pdfreader.numPages

for i in range(0,pages):
    text=pdfreader.getPage(i)
    print(text.extractText())

