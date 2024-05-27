from pypdf import PdfWriter
import os
path="C:\\Users\\ashra\\OneDrive\\Desktop\\Python_Learning\\10hrs_lecture"
pdfs=os.listdir(path)
merger = PdfWriter()
for pdf in pdfs:
    if pdf.endswith(".pdf"):
        print(pdf)
        merger.append(pdf)
        
#pdfs = ['2073 GIS.pdf', '2073 Magh.pdf', '2074 Bhadra.pdf', '2025 Bhadra.pdf']

# merger = PdfWriter()

# for pdf in pdfs:
#     merger.append(pdf)

merger.write("result.pdf")
merger.close()

