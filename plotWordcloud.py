# coding:utf-8

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import re

def generate_wordcloud(text, outname):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    # 设置显示方式
    alice_mask = np.array(Image.open('./output/heart_mask.png'))
    font_path = './font/msyh.ttf'

    stopwords = set(STOPWORDS) 
    with open('stopwords.txt', 'r', encoding='utf-8') as f:
       lines = f.read()
       newLines = re.split('\n', lines)
       for line in newLines:
           stopwords.add(line)
    """
    with open(userlist, 'r', encoding='utf-8') as f:
       lines = f.read()
       newLines = re.split('\n', lines)
       for line in newLines:
           stopwords.add(line)
    """
    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words=200, # 词云显示的最大词数  
           mask=alice_mask,# 设置背景图片       
           stopwords=stopwords, # 设置停用词
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
                  )

    # 生成词云 
    wc.generate(text)

    # 生成的词云图像保存到本地
    wc.to_file('./output/' + outname + '.png')

    # 显示图像
    #plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    #plt.axis("off")# 关掉图像的坐标
    #plt.show()

