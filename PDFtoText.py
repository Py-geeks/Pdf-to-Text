import PyPDF2  
pdfFileObj = open('file location', 'rb')  #Replace file location
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
print(pdfReader.numPages)  
pageObj = pdfReader.getPage(0)  
print(pageObj.extractText())  
pdfFileObj.close()
