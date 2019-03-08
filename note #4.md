# IR note #4

- Boolean retrieval 

  - document 就是所有 keywords 的集合
  
  - queries 
  
    - Boolean expressions of keywords
    
    - AND, OR, NOT

    - 輸出相關的 document
    
  - 缺點是非常 grid, keyword 下錯就找不到 result, 需要花費很多精力去建構一個合適的 query
  
  - 因此我們需要容錯 or 評分機制
  
  - 也就是針對 query 算每個 document 的分數
  
    - assign a score to each document
  
- Problems with Boolean search

  - 沒有 ranking
  
    - no partial matches
    
    - output 常常要不是 0 (too few), 不然就全吐出來 (too many) -> 盛宴 or 飢荒
    
  - 沒有 semantics
  
    - e.x. 我愛你 vs 你愛我

------

- Rank retrieval 

  - 那我們要怎麼針對我們所下的 query 來替所有 document 做排名呢 ? (ranking)

  - 想法是為每個 documnet 給一個分數 (score), 而這個分數是看 document 和所下的 query 有多 match 來決定

  - how ?

    - 想要知道這篇 document 的內容, 我們先看裡面的字, 我們先為這些 words 決定它的重要性 (類似文字雲), 越重要就可以知道這篇 document 大概在講什麼

  - TF-IDF

    - 把 word 的重要程度量化成數字

    - term frequency 和 inverse document frequency

      ![](https://1.bp.blogspot.com/-tnzPA6dDtTU/Vw6EWm_PjCI/AAAAAAABDwI/JatHtUJb4fsce9E-Ns5t02_nakFtGrsugCLcB/s1600/%25E8%259E%25A2%25E5%25B9%2595%25E5%25BF%25AB%25E7%2585%25A7%2B2016-04-14%2B%25E4%25B8%258A%25E5%258D%25881.39.07.png)

    - 上面的公式是想算單字 x 在文章 y 的重要程度

      前面 tf 代表這個單字 x 出現在文章 y 的次數

      後面 idf 為總文章數 / 有幾篇出現單字 x

      因為像的、了這些字, 雖然在文章 y 中可能出現很多次, 但它其實每篇文章都出現, 所以這些字其實不重要,  idf 可以說是看這個單字是不是某篇文章的專屬

      取 log 是為了避免成長太快

    - TF-IDF 並非絕對的指標, 只是反映重要程度