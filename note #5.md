# IR note #5

- 繼 [note #4](https://github.com/chuang76/IR-2018/blob/master/note%20%234.md "link") 我們算出重要程度, 接下來該如何處理呢 ?

- 首先考慮 document collection

  - 把 n 個 documents 表示成 term-document matrix, 其中每個 entry 代表這個 term 在這篇 document 的重要程度, 可以想像出這整個 matrix 是一個 sparse matrix, 很多 entry 都是 0

    ![](https://www.researchgate.net/profile/Lukasz_Kurgan/publication/285339419/figure/fig3/AS:534986446118912@1504562116514/Example-term-document-matrix-for-a-database-of-n-documents-and-t-terms.png)

    

  - TDM (term-document matrix) and DTM (document-term matrix)

  - 幾個 term 代表有幾個維度 (所以高維) , documents 則是這個空間的 point 或 vector (文章向量化 document as vecor)

    ![](https://image.slidesharecdn.com/thevectorspacemodel-150830181233-lva1-app6892/95/the-vector-space-model-6-638.jpg?cb=1440958729)

- 那麼 query 來的時候, 該如何處理 ?

  - 對每個 document 做排名

  - 排名依據為 document 和 query 的相似度

- similarity

  - how to measure ?

    - distance ? angle ? projection ?

  - possible choices

    - Euclidean distance : bad idea

      -> two documents with very similar content can have a significant vector difference because one is much longer than the other ! (對向量長度很敏感)

    - inner product

    - cosine similarity

    - Jaccard (重疊度)

      -> 沒有考慮稀有詞比高頻率的詞更有鑑別度

- cosine similarity measure

  - 算向量夾角, 越小相似度越高

  - 而且出來的值會落在 0 和 1 之間

  - 其實也可說是 inner product / unit vector (歸一化)

    

    ![](https://lh4.googleusercontent.com/SodVc3Xo77b8LhEjqXymSaA-bI-kQdPeY8uG-J0wSSp5q-pxVAf_rPMUX9Y)

- Bag-of-words

  - 一段文本 (句子或文章) 能夠以裝著詞彙的袋子表示, 這種表示方式不考慮文法或詞的順序

    ex. John is quicker than Marry 和 Marry is quicker than John 是一樣的

    - lose the relative ordering of the terms in each document! (丟失了文本中詞出現的先後順序的訊息)
    
    - 所以之後需要把恢復它的位置訊息, 現在先只考慮詞袋模型

  - 有點類似從一篇文章提取關鍵字的感覺, 利用向量來描述文本的主要內容

  - [詞袋模型](https://zh.wikipedia.org/wiki/%E8%AF%8D%E8%A2%8B%E6%A8%A1%E5%9E%8B "link")

- TF-IDF 和 bag-of-words 一起使用

  - TF-IDF 的主要作用為找到某個或某些詞來區別文本

  - bag-of-words 則是找到文本中頻率最高的詞, 在搜尋上很方便, 但沒有語義, 因此後續常靠 TF-IDF 補充

- Summary of vector space ranking

  1. represent the query as a weighted vector (把要下的 query 以 vector 表示)

  2. represent each document as a weighted vector (所有文檔以 vector 表示)

  3. compute the cosine similarity score for the query vector and each document vector (計算相似度)

  4. rank documents with respect to the query by score (依據相似度大小作出排序)

  5. return the top K to user (返回前 K 個結果給使用者)

------
- 補充

  - 首先扣除停用詞 (stop words)

  - tf or idf or tf-idf 做歐氏歸一化 (Euclidean normalized)

    - why normalization ? -> 更精準

    - 以 tf 為例, 原本 tf 是某個 term 在某篇文章出現的頻率, 現在將文章向量化, 可將頻率除以文章向量的長度即完成 normalization

    - ex.  table of tf values

      |           | Doc1 |
      | --------- | ---- |
      | car       | 27   |
      | auto      | 3    |
      | insurance | 0    |
      | best      | 14   |

      接下來將算出 Doc1
      $$
      \sqrt{27^2 + 3^2 + 0^2 + 14^2} = 30.56
      $$
      並且把文章除以長度, 即完成 tf 的normalization

      |           | Doc1              |
      | --------- | ----------------- |
      | car       | 27 / 30.56 = 0.88 |
      | auto      | 3 / 30.56 = 0.10  |
      | insurance | 0 / 30.56 = 0     |
      | best      | 14 / 30.56 = 0.46 |

      

  - 小結 : 算出 tf-idf 後, 可進行 normalization, 之後將 query 也轉成向量

    假設向量表示方式為 : 若出現這個 term, 那就標 1, 反之則標 0

    ex. query 為 (1, 0, 1, 0), Doc1 的 tf-idf 為 (0.897, 0.126, 0, 0.423), 則 Doc1 針對 query 的相似度分數為
    $$
    1 * 0.897 + 0 * 0.126 + 1 * 0 + 0 * 0423 = 0.897
    $$

  - 總結 : 先做 document collection, 得到 document-term matrix, 其中每個 weight 可藉由 tf-idf 等指標得到, 最後可利用 bag-of-words 方便進行查找
