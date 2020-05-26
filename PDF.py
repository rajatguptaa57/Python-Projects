# Combining 2 given PDFs using PyPDF2

import PyPDF2

# Open both PDFs
pdf1File = open('meetingminutes1.pdf', 'rb')

pdf2File = open('meetingminutes2.pdf', 'rb')

# Create object for reading 
reader1 = PyPDF2.PdfFileReader(pdf1File)

reader2 = PyPDF2.PdfFileReader(pdf2File)

# Create object for writing
writer = PyPDF2.PdfFileWriter()

# Read and write contents of PDF into writer object
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

# Write into a new PDF    
outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
