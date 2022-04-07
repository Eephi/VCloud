# coding:utf-8

import os
import chnSegment
import plotWordcloud
import re

if __name__=='__main__':
    # 读取文件
    text_path = './doc'
    text_files = os.listdir(text_path)
    for text_file in text_files:
        with open(text_path + '/' + text_file, 'r', encoding='utf-8') as t:
            text = t.read()
            end = text_file.find('.')
            outname = text_file[0:end]
            # 忽略英文文本
            # text = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&amp;\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\&lt;\&gt;\/\?\~\。\@\#\\\&amp;\*\%]", "",text)
            # 中文分词
            text=chnSegment.word_segment(text, outname)
            # 生成词云
            plotWordcloud.generate_wordcloud(text, outname)
