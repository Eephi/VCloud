# VCloud

用python进行文本分词并生成词云，词云程序credit to: <https://github.com/fuqiuai/wordCloud>

## 需要安装的包

* `sudo pip3 install jieba`
* `sudo pip3 install wordcloud`
* wordcloud包依赖于Pillow，numpy，matplotlib

## 数据集

原始数据为S1 v区VUP综合讨论楼B1-B57的发言记录，数据来源于: <https://github.com/TomoeMami/S1PlainTextGeneral>

在进行分词前，对原始数据做了预处理，删除了用户名信息

## 其他

* 分词采用结巴分词，并支持自定义字典
* 分词结果进行词频统计分析，并导出
* 词云图可自己设定背景图（英文词云图不需先进行分词）

## 字典和停用词表

为了提高分词的准确性，选取了一些v圈常用词汇加入字典[dict.txt](https://github.com/MsEspeon/VCloud/blob/main/dict.txt)，词汇的选取仅与使用热度有关，不代表作者本人立场

此外制作了停用词表[stopwords.txt](https://github.com/MsEspeon/VCloud/blob/main/stopwords.txt)，用于筛选一些无意义的高频词

字典和停用词表可根据个人需求修改

## 运行结果

运行demo.py，会生成相应的的词云图"output/xx.png"，和词频统计"freq/词频统计xx.txt"

eg:输入“B1.txt”的词云图如下：

![image](https://github.com/MsEspeon/VCloud/blob/main/output/B1.png)

输入“B51.txt”的词云图如下：

![image](https://github.com/MsEspeon/VCloud/blob/main/output/B51.png)

## 4.7更新

新增了英文文本的词频统计，更新了字典和停用词表，重做了B57的词频统计和词云图

纯中文的词云图存放在[output_old](https://github.com/MsEspeon/VCloud/tree/main/output_old)

中英文混合的词云图存放在[output](https://github.com/MsEspeon/VCloud/tree/main/output)
