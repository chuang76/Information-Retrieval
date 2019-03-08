# IR note #1

information retrieval 

- an activity of obtaining information relevant to an informtion we need from a collection of information resources

- query 

- e.g. ctrl + f

- environment : user, process, collection(data)

- compare to web search engine ? 

  - web search engine : designed to search for information on World Wide Web

- google

  - why so fast ?
  
  - why precise ?  
  
  - how to store large data ?

- problem

  - efficiency
  
  - effectiveness : the quality of its search results
  
    - precision
    
    - recall
    
  - scalability

- Hadoop, MapReduce

- Databases v.s. IR

  - DB : structured data, formal queries, exact result
  
  - IR : mostly unstructured, free text, natural language (e.g. keyword)

- types of information need (舉例)

  - retrospective 
  
    - search the <u>past</u>

  - prospective

    - search the <u>future</u>

------
- inverted index

- posting list

- bolean query model

- query optimization

- Boolean retrieval model 

  - ask a query that is a Boolean expression
  
- proximity operator 相近運算子

- WestLaw 法律資料庫 

------
- term-document incidence matrix

  - extremely sparse
  
  - we can just record position "1"

- inverted index

  - dictionary + postings (frequency is also added)

- the major steps in inverted index construction

  1. collect the documents to be indexed
  
  2. tokenize the text
  
  3. do linguistic preprocessing of tokens
  
  4. index the documents that each term occurs in

------
- text processing 前處理

  - tokenization 中文和日本不比英文 需要先做斷詞
  
  - normalization   e.g. USA and U.S.A.
  
  - stemming   有同樣字根
  
  - stop words  (dropping common terms)

- query processing 'AND'

  - intersection

  - merge
  
    - O(x+y)
    
  - faster : augment postings 
  
    - 用空間換時間
    
    - 多記一個 <u>skip pointer</u>
    
    - 通常間距是取 L 開根號
    
  - query optimization
  
    - 從小的 set 開始做
    
    - 將詞頻作排序, 從小的開始

- phase queries

  - e.g. 我們想找 "stanford university", 希望搜尋到的是那間史丹佛大學, 而非位於史丹佛的一間大學
  - <u>biword index</u>
  
    - 暴力 直接把他們也變成 dictionary term 了
    
    - 但如果單字更長更複雜該怎麼辦 ?
    
  - <u>positional index</u>
  
    - 比較彈性 記住 term 出現在哪一頁哪一位置
    
    - 所有 query 都可以支援 但需花時間檢查
    
    - e.g. to be or not to be
    
    - 以時間換空間 
    
  - 兩個該怎麼選 ?

    - 常見的存成 biword index 
