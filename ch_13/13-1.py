import PyPDF2

pdfFileObj = open('C:\\Users\\94M0\\Downloads\\Facebook-Marketing-Guide-2022.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
numPages = len(pdfReader.pages)  # Use len(reader.pages) instead of numPages
print(f'The PDF document has {numPages} pages.')

pageObj = pdfReader.pages[4]
text = pageObj.extract_text
print(text)

pdfFileObj.close()
