from PyPDF2 import PdfFileWriter, PdfFileReader
import os, errno

filename = "long-sample.pdf"
directory = "splitted/"+filename

def split(directory, filename):
    inputpdf = PdfFileReader(open(filename, "rb"))
    try:
        os.makedirs(directory)
        print(f' directory : {directory}')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    print("here----")
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(directory+ "/%s.pdf" % i, "wb") as outputStream:
            print(f' directory : {directory}/{i}.pdf')
            output.write(outputStream)

if __name__ == "__main__":
    split(directory, filename)