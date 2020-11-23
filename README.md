# Pdf-to-Text
Extract Text from a PDF file using Python

### Languages and Tools
<img align="left" alt="Python" width="26px" src="python.png" />
<img align="left" alt="pip" width="26px" height="34px" src="pip.png" />
<img align="left" alt="VS Code" width="26px" src="vscode.png" />
<br>

#### installing libraries
```cmd
pip install PyPDF2
```
PyPDF2 is a pure-python PDF library capable of splitting, merging together, cropping,<br>and transforming the pages of PDF files

### Breaking the code

Importing required modules 
```python  
import PyPDF2  
```

Creating a pdf file object  
```python
pdfFileObj = open('file location', 'rb')  #Replace file location
```

Creating a pdf reader object 
```python
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
```

Printing number of pages in pdf file  
```python
print(pdfReader.numPages)
```
    
Creating a page object  
```python
pageObj = pdfReader.getPage(0) 
```
   
Extracting text from page  
```python
print(pageObj.extractText())
```
    
Closing the pdf file object  
```python
pdfFileObj.close()
```

### Submitted By
[Ankush Mishra](https://github.com/ankush0939) 
