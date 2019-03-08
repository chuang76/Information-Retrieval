# IR note #3

- index construction / indexing
  - construct an inverted index

- dictionary compression
  - uncompressed indexes might be large

- problem size

    - size of web (documents)
    - size of vocabulary

- Heap's Law

    - estimating the number of terms

    - estimating vocabulary size as a function of collection size
         $$
         M = kT^b
         $$
         M : vocabulary size  ; T : collection size ; k, b : constant

- Zipf's Law

    - modeling the distribution of terms

    $$
    f * r = k (constant)
    $$
    ​        f : frequency ; r : rank

------

- Dictionary compression
  - 和 postings 相比, dictionary 其實小很多

- fixed-width terms are wasteful
  -  一個英文單字平均約 8 個字, 通常不會超過 20 個字, 所以假設每個單字固定開 20 bytes 來存
  
  - 又 frequency 也用 4 個 bytes 來存
  
  - 以及指標 (指向 postings list) 也用 4 個 bytes 來存
  
  - 假設有 40 萬個單字, 那麼我們共需要 M * (20 + 4 + 4) = 400,000 * 28 = 11.2 MB 來存下這整個 dictionary
  
  - 很明顯 fixed-width 是一個很浪費的作法, 並且也不能解決長度超過 20 的單字這個問題 (ex. supercalifragilisticexpialidocious)

- dictionary as a string
  - 因此我們改成把這 40 萬的單字串起來存成一個超長字串

  - 這個字串大小約為 400,000 * 8 個 byte (因為單字平均約 8 個字) = 3.2 MB

  - 但我們需要指標來指向這個超長字串, 用來記得起始點, 區隔哪裡到哪裡是某個單字

  - 從上述可得知總共有 3,200,000 個位置, 取 log 就可以知道指標需要幾個 bit, 約 3 個 bytes

    

    ![](https://nlp.stanford.edu/IR-book/html/htmledition/img259.png)

  - 所以如果有 40 萬個單字的話, 整個 dictionary 需要的 space 大小約為 400,000 * (4 + 4 + 3 + 8) = 7.6 MB

    (8 bytes 是因為還是要記得哪個字)

- Blocked storage

  - 待補

- Postings compression

  - 比起 dictionary, postings 大很多, 因此怎麼簡潔的存下 postings 很重要

  - 假設有 80 萬篇文章, 那麼一個 docID 需要的大小就是把 80 萬取 log, 約為 20 bits

  - 因此我們改採用的方式為 : 不直接存文章的 ID, 而是存它們的 gap, 來降低編碼的數字

  - 比方說很常出現的單字 the, 假設它每篇文章都出現, 如果改存 gap, 它就可以不必記到很大的 docID, 而是存 : 1,1,1,1... 

- Y codes

  - 待補

    
