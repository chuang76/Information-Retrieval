# IR note #6

接下來我們要考慮 rank retrieval 的效率問題

- speeding up vector space ranking

- principle cost 

  - compute the cosine similarities between the query and a large number of ducouments! (付出很大運算成本)

- we are interested in the <u>relative</u> rather than absolute scores of the documents in the collection

- efficient scoring and ranking

  - choose the K largest cosine values

    - can we do this without computing all N cosines ?

- two-step scheme

  1. find a set A of documents that ate contenders ( K < |A| << N)

     A 不一定包括全部的 K, 但裡面有很多 documents 接近 top K

  2. return the K top-scoring documents in A



## TAAT and DAAT

- 兩種查詢處理

- TAAT (term at a time)

  - evaluate documents one query term at a time

  - 處理完一個 inverted list 再處理下一個

  - 每處理完一個 inverted list , 部分更新 document score (每一篇部分算出來)

  - 其中 list 不以 id 做排序 , 而是根據 weight 排序的結果

  - 優點

    1. 好理解
    
    2. 高效 (以 term 比 document 大很多的情況)

  - 缺點 : large memory footprint

    1. query 包含 frequent term -> 有很長的 inverted list
  
    2. query 複雜 -> 很多的 inverted list

  - 總結 : need to iterate only one inverted list at a time, but <u>store all possible candidates</u>

    ​           所以 TAAT 很少用在 large scale 的系統

  - 以 query 是 "salt water tropical" 為例 :  

    ![](https://slideplayer.com/slide/1507467/5/images/50/Term-At-A-Time.jpg)

- DAAT (document at a time)

  - evaluate one document at a time (score all query terms)

  - 處理完一篇 document 後再處理下一篇

  - 每處理完一篇 document , 就算出它的 complete score (完全算出來)

  - 每次最多維護 K 筆值

  - 還是以 query 是 "salt water tropical" 為例 :  

    ![](https://slideplayer.com/slide/1607482/6/images/61/Query+Processing+Document-at-a-time.jpg)



## Optimization By TopK

- WAND (Weighted AND)

  - 加速 DAAT 用

  - basic idea : branch and bound 

    - 前提是 Top K

  - inverted list 是以 docID 排序

  - threshold score (越往右移 變大)

  - upper bound (越往右移 變小)

    

------


- Search engine

  1. on-line : query processing
  
  2. off-line : inverted index

- Optimization principles 

  - optimization -> 偷工減料
  
    1. read less data from inverted lists
    
    2. calculate scores for fewer documents (e.g. reduce the number of candidate documents) 

- Safe ranking 

  Non-safe ranking ? (Is it ok ?)

  思考 : effective v.s. efficientcy



## Non-safe Ranking


- Index elimination (non-safe)

  - only consider docs containing terms whose idf exceeds a preset threshold

    因為 low idf 代表每一篇文章都出現 , 通常是 stop words , 對整個分數沒有貢獻 ; 

    而 high idf 則對分數貢獻越多 

  - only consider docs containg many query terms

    

- Bloom filter

  - 集合 , 很快告訴你 set 裡面是否含某 element , 可能會有錯 , 但通常不會有

    如果真的出錯 , 再多算它真正的 score

  - 利用 hash

  - false postive & false negative

    1. 前者代表 x 沒有 , 但我們說它有
    
    2. 後者代表 x 有 , 但我們說它沒有

  - bloom filer 可能會出現 false positive 的情況 , 因為當初的 1 可能是別人 hash 來的

  - 小結 : bloom filer 保證說沒出現的一定真的沒出現 , 有出現則不一定真的有出現

    

- Clustering pruning

  - 隨機挑 doc 當 leader (通常為 N^0.5 個)

  - 再找跟它最近的當 follower (利用 cosine similarity)

  - 接下來 query 先和 leader 算

  - 之後才與最近的 leader 所帶領的 followers 開始真正算 

    - non safe 

    - 因為一開始只和 leader 算 , 跟錯大哥就完啦

  - best choice

    - 因為 leader 會影響精確度 , 所以我們一開始就應該好好的、有意識的挑 leader

    - leader selection algo : 不斷的更新 leader , 挑出 best

    - 為了避免掉答案 , 還可以 :

      1. 和兩個 leader 的 followers 算 (兩群)

      2. 一個點可以跟不只一個 leader

      -> 缺點是多運算 , 可以 off-line 先算好相似的群 , on-line 再實際算

  