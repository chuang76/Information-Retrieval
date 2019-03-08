# encoding: utf8

# from download import text
import requests, os
import json
import re
from bs4 import BeautifulSoup
from gensim import corpora, models, similarities

import jieba
jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('userdict.txt')

# os.makedirs('./天龍八部/', exist_ok=True)
path = r'./天龍八部/'

url = 'http://www.millionbook.net/wx/j/jingyong/tlbb/index.html'
d1 = requests.get(url)
d1.encoding = 'big5'
titles = BeautifulSoup(d1.text, 'lxml').select('tr > td > a')

# def download():
#     for title in titles:
#         titleurl = 'http://www.millionbook.net/wx/j/jingyong/tlbb/' + title.get('href')
#         titlename = title.text
#         # print(titlename, titleurl)
        
#         try:
#             f = open(path + '%s.txt' % titlename, 'w')
#             f.close()
#         except:
#             pass
        
#         d2 = requests.get(titleurl)
#         d2.encoding = 'big5'
#         contents = BeautifulSoup(d2.text, 'lxml').select('tr > td.tt2')
        
#         for content in contents:
#             try:
#                 f = open(path + '%s.txt' % titlename, 'w')
#                 f.write(content.text)
#                 f.close()
#             except:
#                 pass
#         print(titlename + '-----[下載完成]')

def main():
    # download()
    docs = []
    for title in titles:
        titlename = title.text
        doc = open(path + '%s.txt' % titlename, 'r').read().split()
        # print(doc)
        docs.append(doc)

    term = []          # t[0], t[1], ... 含每一章節的詞
    i = 0
    for doc in docs: 
        term.append([])
        for s in doc:
            words = jieba.cut(s, cut_all=False)    # 每句話作斷詞
            for word in words:
                term[i].append(word)             
        i += 1

    dictionary = corpora.Dictionary(term)
    corpus = [dictionary.doc2bow(i) for i in term]
    # print(corpus)
    tfidf = models.TfidfModel(corpus)

    num = input('\n請輸入欲比較的章節: ')
    test_vec = dictionary.doc2bow(term[int(num)])
    # print(test_vec)
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    sim = index[tfidf[test_vec]]
    # print(sim)
    result = sorted(enumerate(sim), key=lambda item: -item[1])
    print('相似度排序結果: ')
    for (i, j) in result:
        if i != int(num):
            print('第 %2d 章   %.4f' % (i, j))

if __name__ == '__main__':
    main()
