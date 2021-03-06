#!/usr/bin/env python3
#coding=utf-8

from skuuper_cleaner.automate import *
from compare.XML_compare import *

#file_golden = 'CPP20000210000021_r_st_20170530_2152_0.tmx'
#tmx = align('skuuper_cleaner/thirdparty/aligner_ch/demo/CPP20000210000021.r.st', 'skuuper_cleaner/thirdparty/aligner_ch/demo/CPP20000210000021.c.utf8.st', ldc=True, lf=False, aligner='hunalign', df='ru-zh.dic')
#print(compare_data(file_golden, tmx))


file_golden = 'ZhRuParCor/data/mumu.xml'
tmx = align('ZhRuParCor/original_texts/Mumu_r.txt', 'ZhRuParCor/original_texts/Mumu_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zh.dic')
print(compare_data(file_golden, tmx))
tmx = align('ZhRuParCor/original_texts/Mumu_r.txt', 'ZhRuParCor/original_texts/Mumu_zh.txt', ldc=True, lf=False, aligner='champollion', df='rcdict.utf8.txt')
print(compare_data(file_golden, tmx))


file_golden = 'data/GoldenStandard/idiot_all.xml'
tmx = align('data/OriginalTexts/idiot_all_ru.txt', 'data/OriginalTexts/idiot_all_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zh.dic')
print(compare_data(file_golden, tmx))
tmx = align('data/OriginalTexts/idiot_all_ru.txt', 'data/OriginalTexts/idiot_all_zh.txt', ldc=True, lf=False, aligner='champollion', df='rcdict.utf8.txt')
print(compare_data(file_golden, tmx))

