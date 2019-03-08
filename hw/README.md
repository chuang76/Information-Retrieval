# 文本相似度排序

利用 gensim 進行文本分析，挑選天龍八部一章與其他章節做相似度排序

<br>

## 0. Idea

以下會利用到 gensim 的三個核心分別為 corpus、vector、model

1. 爬蟲

2. 斷詞 : 利用 jieba 進行斷詞

3. 建立語料庫 : 利用 `bag-of-words` 建立 `corpus`，並從字典格式轉成向量空間格式
4. 建立模型 : 這裡使用 `TF-IDF` 模型，也可以考慮使用 Lsi 模型
5. 計算相似度 : 建立索引並排序，輸出章節相似度 score

<br>

## 1. Dependencies

- jieba

```
$ pip install jieba
```

- gensim

```
$ pip install -U gensim
```

<br>

## 2. Usage

1. 下載天龍八部全部章節

```
$ python run.py
```

2. 建立 TF-IDF 模型

```
$ python run.py
```

3. 相似度排序

```
$ 請輸入欲比較的章節: 
```

