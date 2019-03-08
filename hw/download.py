import os
import requests
import json
import re
from bs4 import BeautifulSoup

import jieba
jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('userdict.txt')
os.makedirs('./天龍八部/', exist_ok=True)
path = r'./天龍八部/'

url = 'http://www.millionbook.net/wx/j/jingyong/tlbb/index.html'
d1 = requests.get(url)
d1.encoding = 'big5'
titles = BeautifulSoup(d1.text, 'lxml').select('tr > td > a')

def text():

	for title in titles:
	    titleurl = 'http://www.millionbook.net/wx/j/jingyong/tlbb/' + title.get('href')
	    titlename = title.text
	    # print(titlename, titleurl)
	    
	    try:
	        f = open(path + '%s.txt' % titlename, 'w')
	        f.close()
	    except:
	        pass
	    
	    d2 = requests.get(titleurl)
	    d2.encoding = 'big5'
	    contents = BeautifulSoup(d2.text, 'lxml').select('tr > td.tt2')
	    
	    for content in contents:
	        try:
	            f = open(path + '%s.txt' % titlename, 'w')
	            f.write(content.text)
	            f.close()
	        except:
	            pass
	    print(titlename + '-----[下載完成]')

def main():
	text()

if __name__ == '__main__':
    main()