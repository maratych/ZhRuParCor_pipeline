#!/usr/bin/env python3
#coding=utf-8

from skuuper_cleaner.automate import *
from compare.XML_compare import *

#file_golden = 'CPP20000210000021_r_st_20170530_2152_0.tmx'
#tmx = align('skuuper_cleaner/thirdparty/aligner_ch/demo/CPP20000210000021.r.st', 'skuuper_cleaner/thirdparty/aligner_ch/demo/CPP20000210000021.c.utf8.st', ldc=True, lf=False, aligner='hunalign', df='ru-zh.dic')
#print(compare_data(file_golden, tmx))

file_golden = 'ZhRuParCor/data/idiot_ch2.xml'
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zh.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhEMPTY.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT60k.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT5k.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT10k.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT10k.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT20k.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT30k.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT40k.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT50k.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT60kEXT.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT50kEXT.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT40kEXT.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT30kEXT.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT20kEXT.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT10kEXT.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT5kEXT.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT60kCogn.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhMARAT60kCognEXT.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhCognEXT.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Idiot2ch_r.txt', 'ZhRuParCor/original_texts/Idiot2ch_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zhCogn.dic')
print(compare_data(file_golden, tmx))