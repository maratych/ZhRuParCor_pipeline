#!/usr/bin/env python3
#coding=utf-8

from skuuper_cleaner.automate import *
from compare.XML_compare import *

file_golden = 'data/GoldenStandard/idiot_all.xml'
tmx = align('data/OriginalTexts/idiot_all_ru.txt', 'data/OriginalTexts/idiot_all_zh.txt', ldc=True, lf=False, aligner='hunalign', df='ru-zh.dic')
print(compare_data(file_golden, tmx))
