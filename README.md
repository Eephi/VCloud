# wordCloud

用python进行文本分词并生成词云，词云程序credit to: <https://github.com/fuqiuai/wordCloud>

## 需要安装的包

* `sudo pip3 install jieba`
* `sudo pip3 install wordcloud`
* wordcloud包依赖于Pillow，numpy，matplotlib

## 其他

* 分词采用结巴分词，并支持自定义字典
* 分词结果进行词频统计分析，并导出
* 词云图可自己设定背景图（英文词云图不需先进行分词）

## 运行结果

运行demo.py，会生成相应的的词云图"output/xx.png"，和"freq/词频统计xx.txt"

eg:输入“B1.txt”的词云图如下：

![image](https://github.com/MsEspeon/VCloud/blob/main/output/B1.png)

输入“B50.txt”的词云图如下：

![image](https://github.com/MsEspeon/VCloud/blob/main/output/B50.png)