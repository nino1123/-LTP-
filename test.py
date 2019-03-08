# coding:utf-8
import codecs
import os
import pyltp
import os
import pyltp

LTP_DATA_DIR = "f:\\NLPJP\\xlbz\\LTP\\ltp_data_v3.4.0/"  # ltp模型目录的路径

cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`

par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

srl_model_path = os.path.join(LTP_DATA_DIR, 'pisrl')  # 语义角色标注模型目录路径，模型目录为`pisrl`。注意该模型路径是一个目录，而不是一个文件。

 

# from pyltp import SentenceSplitter

from pyltp import Segmentor

# from pyltp import Postagger

# from pyltp import NamedEntityRecognizer

# from pyltp import Parser

# from pyltp import SementicRoleLabeller

# from pyltp import Segmentor

def read_and_seg_pos(file_dir):
    segmentor = Segmentor()
    # postagger = Postagger()
    segmentor.load_with_lexicon("f:\\NLPJP\\xlbz\\LTP\\ltp_data_v3.4.0\\cws.model","ceshi.txt")
    # postagger.load_with_lexicon("f:/NLPJP/xlbz/LTP/ltp_data_v3.4.0/pos.model","ceshi.txt")
    file_read = open(file_dir,"r")
    texts = file_read.readlines()
    file_write_seg = open(file_dir+"_seg","w")
    # file_write_pos = open(file_dir+"_pos","w")
    
	
	
	for text in texts:
        words = segmentor.segment(text)
        file_write_seg.write(" ".join(words)+"\n")
        # postags = postagger.postag(words)
        # words_and_pos.append('$','$')
        # for word,pos in words_and_pos:
        #     if word != '$':
        #         file_write_pos.write(word+" "+pos+" ")
        #     else:
        #         file_write_pos.write('\n')
    file_read.close()
    file_write_seg.close()
    # file_write_pos.close()
    segmentor.release()
    postagger.release()

    read_and_seg_pos()