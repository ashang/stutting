#encoding=utf-8
import jieba

# Big5
#jieba.set_dictionary('dict.txt.big')
#jieba.set_dictionary('dict.txt.big')

# User dict
#jieba.load_userdict("user.dict")

content = open('lyric-tw.txt', 'rb').read()

print "Input：", content

words = jieba.cut(content, cut_all=False)

print "Output 精確模式 Full Mode："
for word in words:
    print word
