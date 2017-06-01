#!/usr/bin/env python
#coding=utf8
# A script to compare parallel texts in TMX and XML
# @author @netbug aka Oleg Urzhumtcev

import lxml.etree as ET
import re
import string
regex = re.compile('[%s]' % re.escape(string.punctuation + "«»“”，。……"))

debug = True

def read_XML(fn):
    d = []
    langs = []
    with open(fn, 'rb') as fh:
        html = fh.read()
        root = ET.XML(html)
        for parent in root.xpath('//PARAGRAPH'):  # Search for parent elements
            grp = []
            for sent in parent:
                grp.append(sent.text)
            d.append(list(reversed(grp)))
    return langs, d

def read_TMX(fn):
    d = []
    langs = []
    with open(fn, 'rb') as fh:
        html = fh.read()
        root = ET.XML(html)
        for parent in root.xpath('//tmx/body'):  # Search for parent elements
            for tu in parent:
                grp = []
                for tuv in tu:
                    #print(tuv.tag)
                    grp.append(tuv[0].text)
                d.append(grp)
    return langs, d

def read_file(fn):
    return read_XML(fn) if fn.lower().endswith('.xml') else read_TMX(fn)

def prep_text(s):
    return regex.sub(' ', s).replace(" ", "").lower().strip() if type(s) == str else s

def compare_list(l1, l2):
    cnt = 0
    c1 = 0
    c2 = 0
    for i, sent in enumerate(l2):	# sent - предложение из "нового" текста
      cnt +=	 1
      #print(sent[0])
      bFound = False
      bFnd = False
      for s1 in l1:
        # Если нашли такое же входное предложение. Если вход отличается - автоматом ошибка!
        if prep_text(s1[0]) == prep_text(sent[0]):
          bFound = True
          c1 += 1
          #print(l2[i][0])
          # Если совпадаем и перевод
          if prep_text(s1[1]) == prep_text(sent[1]):
            bFnd = True
            #print("Match!")
            c2 += 1
      if not bFound and debug:
          print("Not found source sentence: " + sent[0])
      elif not bFnd and debug:
          print("Not found translation %s for source sentence %s " % (sent[1], sent[0]))
    if debug:
        print("Total sentences in target: %d, source: %d, matching targets %d out of matching sources %d" % (cnt, len(l1), c2, c1))
    p = float(c2) / cnt
    r = float(c2) / len(l1)
    return p, r

def compare_data(f_orig, f_comp, b_ignore_spaces = True):
    langs1, t_orig = read_file(f_orig)
    #print(t_orig)
    langs2, t_trans = read_file(f_comp)
    #print(t_trans)
    # TODO: check languages... And other sanity stuff
    p, r = compare_list(t_orig, t_trans)
    return {"status": "OK", "precision": p, "recall": r}

if __name__ == '__main__':
    file_golden = 'data/demo_h.tmx'
    file_compare = 'data/demo_m.tmx'
    res = compare_data(file_golden, file_compare)
    print(res)