import pyltp
import os
import codecs
import re
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser

def word_splitter(filedir):
    model_path = "..\\LTP\\ltp_data_v3.4.0\\cws.model"
    segmentor = Segmentor()
    segmentor.load(model_path)
    file_read = open(filedir,'rb')
    # file_read = open("..\\LTP\\ceshi.txt", 'rb')
    # file_out = open("..\\LTP\\ceshi_seg.txt", 'w')
    texts = file_read.readlines()
    # allist=[]
    for line in texts:
        words = segmentor.segment(line)
        # words_list = list(words)
        # allist.append(list(words))
        # file_out.write(words_list)
        print(list(words))
    return list(words)
    segmentor.release()
    file_read.close()
    # file_out.close()


def word_tag(words):
    postagger = Postagger()
    postagger.load('..\\LTP\\ltp_data_v3.4.0\\pos.model')
    # file_read = open(file_dir1, "rb")
    # texts = file_read.readlines()
    postags = postagger.postag(words)
    print("词性标注结果：")
    for word, tag in zip(words, postags):
        print(word+':'+tag)

    # for text in texts:
    #     postags = postagger.postag(text)
    #     for word, pos in zip(text, postags):
    #         print(word + ':' + tag)
    #         file_write_pos.write(word + ':' + pos + "\n")
    postagger.release()
    return postags

def parse(words, postags):
    # file_dir = "..\\LTP\\ltp_data_v3.4.0\\pos.txt"
    parser = Parser()
    parser.load('..\\LTP\\ltp_data_v3.4.0\\parser.model')
    # file_read = open("..\\LTP\\pos.txt", "rb")

    arcs = parser.parse(words, postags)  # 句法分析
    file_out = open(".\\jffx.txt", "w")
    print("句法分析结果：")
    print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    file_out.write("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    parser.release()  # 释放模型

    # texts = file_read.readlines()
    # for line in texts:
    #     wordlists = dict(line.split(':'))
    #     for words, postags in wordlists:
    #         arcs = parser.parse(words, postags)
    #         print("句法分析结果：")
    #         print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    #         file_out.write("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    parser.release()
    # file_read.close()
    file_out.close()
    return

# parse("..\\LTP\\ltp_data_v3.4.0\\testceshi.txt")
filedir="..\\LTP\\testceshi.txt"
# file_dir1="..\\LTP\\pos.txt"

words = word_splitter(filedir)
tags = word_tag(words)
parse(words, tags)