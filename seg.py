import pyltp
import os
import codecs
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser

model_path = "..\\LTP\\ltp_data_v3.4.0\\cws.model"
from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load(model_path)
file_read = open("..\\LTP\\testceshi.txt",'rb')
file_out = open("..\\LTP\\testceshi_seg.txt",'w')
texts= file_read.readlines()
for line in texts:
    words = segmentor.segment(line)
    file_out.write('\t'.join(words))
    print('\t'.join(words))

segmentor.release()  # 释放模型
file_read.close()