import os
import PyPDF2
import Split
from subprocess import call
import sys
import os
import glob

path =  os.getcwd() + '\\inputs'
input_books = os.listdir(path)

for input_book in input_books:
    filename = input_book
    book_name = filename.split('.pdf')[0]
    directory = "splitted/" + filename.split('.pdf')[0]
    output_directory ='outputs/'+filename.split('.pdf')[0]
    input_file_dir = path+'/'+filename
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    Split.split(directory, input_file_dir)
    print('here....')
    pdfFileObj = open(input_file_dir, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for i in range(pdfReader.numPages):
        splitted_file_name = directory + "/" + repr(i)
        print(f'splited dir : {splitted_file_name}')
        print(f"director {os.getcwd()}" )
        call(["pdftotext", splitted_file_name + ".pdf"])

    lines = []
    fileCounter = len(glob.glob1(f"{directory}","*.txt"))

    for i in range(fileCounter):
        with open(f'{directory}/{i}.txt','r') as file:
            lines.append(file.readlines())
        file.close()

    with open(f'{output_directory}/{book_name}.txt', 'a+') as filehandle:
            for listitem in lines:
                for li in listitem:
                    filehandle.write('%s\n' % li)

    

