from pypdf import pdfWriter
import os
merger = pdfWriter()

files = [file for file in os.listdir() if file.endswith(".pdf")]
for pdf in files:
    merger.append(pdf)
merger.write("merged-pdf.pdf")
merger.close()    