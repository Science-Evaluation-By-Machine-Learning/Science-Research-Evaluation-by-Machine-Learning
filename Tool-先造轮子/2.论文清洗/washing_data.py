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


#Load the local PDF Document
#pdfFile = open("16_AM_02.pdf",'rb')
pdfFile = open("Test thesis_2.pdf",'rb')
#Load the online PDF Document
#pdfFile = urlopen("http://www.nanoscience.gatech.edu/paper/2016/16_AM_02.pdf")
outputString = readPDF(pdfFile)
print(outputString)
print(type(outputString))
print(len(outputString))
print('##########################################')
pdfFile.close()  ##很重要，防止占用内存


import nltk

# 大小写转换
outputString = outputString.lower() #小写转化
# outputString = outputString.upper() #大写转化
print(outputString)

# 文本替换，拆分连词，
# PS: 这部分可以自己扩展
  #文本替换，定义函数和类
import re
replacement_patterns = [
    (r'won\'t','will not'),
    (r'it\'s','it is'),
    (r'can\'t','can not'),
    (r'i\'m','i am'),
    (r'isn\'t','is not'),
    (r'(\w+)\'ll','g<1> will'),
    (r'(\w+)n\'t','\g<1> not'),
    (r'(\w+)\'ve','\g<1> have'),
    (r'(\w+)\'s','\g<1> is'),
    (r'(\w+)\'re','\g<1> are'),
    (r'(\w+)\'d','\g<1> would'),
    # 以下为防止pdfminer 将英文标点符号转化成中文标点符号异常特殊设定
    (r'won\ ’t','will not'),
    (r'it\ ’s','it is'),
    (r'can\ ’t','can not'),
    (r'i\ ’m','i am'),
    (r'isn\ ’t','is not'),
    (r'(\w+)\ ’ll','g<1> will'),
    (r'(\w+)n\ ’t','\g<1> not'),
    (r'(\w+)\ ’ve','\g<1> have'),
    (r'(\w+)\ ’s','\g<1> is'),
    (r'(\w+)\ ’re','\g<1> are'),
    (r'(\w+)\ ’d','\g<1> would'),
    (r'，',','), #将中文符号替换为英文符号
    (r'。','.'),
    (r'“','"'),
    (r'”','"'),
    (r'-',' '),
    (r'f igure','figure'), #pdfminer 转化的异常单词替换

]
class RegexpReplacer(object):  #没太看懂，仔细看看
    def __init__(self,patterns = replacement_patterns):
        self.patterns = [(re.compile(regex),repl) for (regex,repl) in patterns]
    def replace(self,text):
        s = text
        for (pattern, repl) in self.patterns:
            (s,count) = re.subn(pattern,repl,s)
        return s
   # 替换操作
replacer = RegexpReplacer()
outputString = replacer.replace(outputString)
print(outputString)
   #同义词替换
   #*******（待后续更新这部分）

# 语句分离器
sent_tokens = nltk.sent_tokenize(outputString)
print("语句分离：")
print(sent_tokens)
# 句词分离器
word_tokens =[]
for sent in sent_tokens:
    word_token = nltk.word_tokenize(sent)
    word_tokens.append(word_token)
    print("词句分离：")
    print(word_tokens)

#去除标点符号
import re
import string

x = re.compile('[%s]' % re.escape(string.punctuation))
word_tokens_no_punctuation = []
for sent in word_tokens:
    new_sent = []
    for word in sent:
        new_word = x.sub(u'',word)
        if not new_word ==u'':
            new_sent.append(new_word)
    word_tokens_no_punctuation.append(new_sent)
word_tokens = word_tokens_no_punctuation #再替换回word_tokens
print(word_tokens)

#词干提取(输入是单个字符串，输出是单个字符串)
 # Porter Stem
porter_stemmers = []
print("$$$$$$$$$$$$$$$")
for sent in word_tokens:
    new_sent = []
    for word in sent:
        new_word = nltk.stem.PorterStemmer().stem(word)
        new_sent.append(new_word)
        print(word, new_word)
    porter_stemmers.append(new_sent)
print("porter_stemmers 词干提取：")
print(porter_stemmers)

  # Lancaster Stem
print("$$$$$$$$$$$$$$$")
lancaster_stemmers = []
for sent in word_tokens:
    new_sent = []
    for word in sent:
        new_word = nltk.stem.LancasterStemmer().stem(word)
        new_sent.append(new_word)
        print(word, new_word)
    lancaster_stemmers.append(new_sent)
print("lancaster_stemmers 词干提取：")
print(lancaster_stemmers)

 #Snowball Stem
print("$$$$$$$$$$$$$$$")
snowball_stemmers = []
for sent in word_tokens:
    new_sent = []
    for word in sent:
        new_word = nltk.stem.SnowballStemmer("english").stem(word)
        new_sent.append(new_word)
        print(word, new_word)
    snowball_stemmers.append(new_sent)
print("snowball_stemmers 词干提取：")
print(snowball_stemmers)

#获取单词词性 (输入是单个字符串组成的list，输出也是)
print("$$$$$$$$$$$$$$$")
tagged_word_tokens = []
for sent in word_tokens:
    tagged_sent = nltk.pos_tag(sent)
    tagged_word_tokens.append(tagged_sent)
print(tagged_word_tokens)

#词形还原 (需要制定词性，结合pos_tag使用)
print("$$$$$$$$$$$$$$$")
from nltk.corpus import wordnet
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

word_netlemmatizers = []
for pos_sent in tagged_word_tokens:
    new_sent = []
    for pos_word in pos_sent:
        wordnet_pos = get_wordnet_pos(pos_word[1]) or wordnet.NOUN #提取词性，替换为lemmatizer标准输入pos
        new_word = nltk.stem.WordNetLemmatizer().lemmatize(pos_word[0],pos=wordnet_pos)
        new_sent.append(new_word)
        print(pos_word[0],new_word)
    word_netlemmatizers.append(new_sent)
print("word_netlemmatizers 词形还原：")
print(word_netlemmatizers)
word_tokens = word_netlemmatizers

#去除停用词,建议先词形还原
from nltk.corpus import stopwords
stoplist = stopwords.words('english')
print(stoplist)

cleanwordlist = []
#for word in word_tokens:
for sent in word_tokens:
    new_sent = []
    for word in sent:
        if word not in stoplist:
            new_sent.append(word)
    cleanwordlist.append(new_sent)
print("&&&&&&&&&&&&&&&&&&&&&")
print(cleanwordlist)
word_tokens = cleanwordlist

#罕见词移除

# 拼写纠错

# 文本清理

#列表转化为字符串
   #先转化为标准列表
word_tokens_list = []
for sent in word_tokens:
    for word in sent:
        word_tokens_list.append(word)
   #再由列表转化为字符串
word_tokens_str = " ".join(word_tokens_list)
print(word_tokens_str)

# 统计词频
import numpy as np
from nltk.probability import FreqDist
freq_dist = FreqDist(word_tokens_list)
print(freq_dist)
freq_list = []
num_words = len(freq_dist.values())
print(num_words)
for i in range(num_words):
    freq_list.append([list(freq_dist.keys())[i],list(freq_dist.values())[i]])
freqArr = np.array(freq_list)
print(freqArr)
'''
from nltk.probability import FreqDist
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
for sent in word_tokens:
    for word in sent:
        fd = FreqDist().inc(word)
ranks = []
freqs = []
for rank,word in enumerate(FreqDist()):
    ranks.append(rank+1)
    freqs.append(FreqDist()[word])
plt.loglog(ranks,freqs)
plt.xlabel('frequency(f)',fontsize=14,fontweight = 'bold')
plt.ylabel('rank(r)',fontsize=14,fontweight = 'bold')
plt.grid(True)
plt.show()
'''