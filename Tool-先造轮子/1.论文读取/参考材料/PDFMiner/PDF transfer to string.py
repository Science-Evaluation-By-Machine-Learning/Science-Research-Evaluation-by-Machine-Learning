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


#本地读取PDF
pdfFile = open("F:/3. Python&数据科学&机器学习&人工智能/0.项目/5.【大项目】抓取太阳能电池文章并分析/16_AM_02.pdf",'rb')
#在线网上读取PDF文档
#pdfFile = urlopen("http://www.nanoscience.gatech.edu/paper/2016/16_AM_02.pdf")
outputString = readPDF(pdfFile)
print(outputString)
print(len(outputString))
print('##########################################')
pdfFile.close()  #很重要，防止占用内存