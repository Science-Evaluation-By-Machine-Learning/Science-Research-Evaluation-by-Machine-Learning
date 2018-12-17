'''
from urllib.request import urlopen
pdfFile = urlopen("http://www.nanoscience.gatech.edu/paper/2018/18_NC_02.pdf")
print(pdfFile)
'''
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

def read_pdf():

    #Load the local PDF Document
    pdfFile = open("16_AM_02.pdf",'rb')
    #Load the online PDF Document
    #pdfFile = urlopen("http://www.nanoscience.gatech.edu/paper/2016/16_AM_02.pdf")
    outputString = readPDF(pdfFile)
    #print(outputString)
    print(type(outputString))
    print(len(outputString))
    print('##########################################')
    pdfFile.close()  ##很重要，防止占用内存