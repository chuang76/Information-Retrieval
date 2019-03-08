# IR note #2

1. How do we store dictionary efficiently ? (index compression)

2. quickly look up elements at a query time ?

兩種資料結構 (dictionary data structures)

- hash table 

  - O(1)
  
  - 不同的詞就有不同的 hash function
  
- tree 

  - O(logM)

  - binary tree, B-tree

  - support wild query

  - rebalancing binary trees is expensive

------
- tolerant retrieval 允許容錯

  - wildcard query

  - misspelled correction

- google service

  - google trend
  
  - google flu
  
    - CDC v.s. Google Flu Trends
    
  - google correlate
  
    - get back queries whose frquency follows a similar pattern
    
   - 不是因為有人同時搜尋兩個字 而是 pattern 一樣
------
- wildcard query 使用場合

  1. 使用者不確定 query term 怎麼拼

     ex. 到底是 Sydney 還是 Sidney 呢 ? 這時候可以下 S*dney 這個關鍵字

  2. color and colour

  3. 知道字根

  4. 使用者不確定正確的翻譯

  - (trailing wildcard query) search mon* 
  
    - 找 mon 開頭的
    
    - 找介於 mon 和 moo 中間
    
  - (leading wildcard query) search *mon 
  
    - 找 mon 結尾的
    
    - harder, need an additional tree for terms backwards
    
    - (反轉) 找介於 nom 和 non 中間

------
- Bigram (k-gram) index

  - for general wildcard query!

  - 把字拆開

  - e.g.  (k=3) kitten : \$ki kit itt tte ten en\$

  - k 大小也很重要 太小沒效率 太大湊不出來 無法處理

  - post filter 還需要再過濾一次 (後處理) 
------
- google 的 wildcard (*)

  - used in <u>whole words</u>, not parts of words

    - why doesn't google fully support wildcard queries ?  -> 效率問題

  - 它其實不是用 k-gram index 和 dictionary 實作

------
- spell correction 語意

  - 困難點
  
    1. 要知道你打錯 (藉由 word 的 frquency 很低發現)
    
    2. 還知道你原本想打什麼
    
       - find the similar terms
       
       - choose the most frquency one

  - 兩大情況

    1. misspelled

    2. context-sensitive

------
- misspelled

   - 知道它什麼時候出錯 ? -> query word is rare 或甚至在 dictionary 找不到

    - 解決

      1. 找出與它最接近的字
      
      2. 計算相似度 
      
      3. 選擇頻率最高的那個字

    - closet ?

      1. edit distance ([Levenshtein distance](https://people.cs.pitt.edu/~kirk/cs1501/Pruhs/Spring2006/assignments/editdistance/Levenshtein%20Distance.htm "link")) 編輯距離
      
         - e.g. from cat to act is 2
         
         - e.g. from cat to dog is 3
         
         - expensive and slow
         
         - O((m * n) * M)
         
         - [minimum edit distance](http://cpmarkchang.logdown.com/posts/222651-minimum-edit-distance "link")
         
      2. weighted edit distance 加上權重 算某字和某字互換的 cost
      
      3. k-gram overlap

  - k-gram overlap
  
    - 切成的塊有多少相似
    
    - O((m + n) * M)

  - Jaccard coefficient

    - 為避免太長的單字 結果反而相似高 (因為可能剛好重疊很多)

    - 交集 / 聯集

    - 因為考慮聯集 所以太長的單字即使 overlap 多 但分母也大

    - always assigns a number between 0 and 1!

    - e.g. q = bord (bo, or, rd)

      ​	t = boardroom(bo, oa, ar, rd, dr, ro, oo, om)

      ​	overlap = 2 (bo, rd)

      ​	J.C. = 2 / (3 + 8 - 2) =  2 / 9

------
- context-sensitive

  - need surrounding context to catch this