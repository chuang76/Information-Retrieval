# QA bot

機器人問答系統，demo 時間為 5 分鐘，讀取題目 200 題，並提交正確選項。

<br>

## Prerequisite

於 Google Colaboratory 上運行，事先至 [FastText](https://fasttext.cc/docs/en/pretrained-vectors.html "link") 下載 pre-trained model

- Python 2
- jieba
- pyfasttext 

<br>

## Format

- 讀取 json 檔題目，例如

```json
 {"Question":"中華民國第14任總統，民主進步黨第16屆黨主席，同時也是台灣歷史上首位女性元首，她是:" 
  , "A":"蔡正元"
  , "B":"蔡英文"
  , "C":"洪慈庸" },

  {"Question":"明末清初著名軍事將領，曾因「引清兵入關」而被世人斥責為漢奸，他的名字叫做:" 
  , "A":"吳一桂"
  , "B":"吳二桂"
  , "C":"吳三桂" }
```

- 繳交答案應為 json 格式，如 ["A", "B", "C"]