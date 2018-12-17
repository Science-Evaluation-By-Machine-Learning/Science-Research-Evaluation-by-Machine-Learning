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


#���ض�ȡPDF
pdfFile = open("F:/3. Python&���ݿ�ѧ&����ѧϰ&�˹�����/0.��Ŀ/5.������Ŀ��ץȡ̫���ܵ�����²�����/16_AM_02.pdf",'rb')
#�������϶�ȡPDF�ĵ�
#pdfFile = urlopen("http://www.nanoscience.gatech.edu/paper/2016/16_AM_02.pdf")
outputString = readPDF(pdfFile)
print(outputString)
print(len(outputString))
print('##########################################')
pdfFile.close()  #����Ҫ����ֹռ���ڴ�