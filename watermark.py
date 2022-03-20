import PyPDF2
import sys

inputs = sys.argv[1:]

targetpdf = inputs[0]
waterpdf = inputs[1]

with open(f'./assets/{targetpdf}', 'rb') as in_targetpdf:
    with open(f'./assets/{waterpdf}', 'rb') as in_waterpdf:
        water_reader = PyPDF2.PdfFileReader(in_waterpdf)
        water_page = water_reader.getPage(0)

        outname = 'water.pdf'
        with open(f'./assets/{outname}', 'wb') as out_targetpdf:
            target_writer = PyPDF2.PdfFileWriter()

            target_reader = PyPDF2.PdfFileReader(in_targetpdf)
            for i in range(0, target_reader.getNumPages()):
                target_page = target_reader.getPage(i)
                target_page.mergePage(water_page)
                target_writer.addPage(target_page)
            
            target_writer.write(out_targetpdf)
        

