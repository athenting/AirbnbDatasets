# -*- coding: utf-8 -*-
# coding=utf-8

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

txt1 = open('D:/Project/dataset/new/cq.txt', 'r', encoding='utf-8').read() 
words_ls = jieba.cut(txt1, cut_all=True)
words_split = " ".join(words_ls)

wc = WordCloud(
    background_color="white",
    repeat=True
)   
wc.font_path="simhei.ttf"  
my_wordcloud = wc.generate(words_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

wc.to_file('zzz.png')
