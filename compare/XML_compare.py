#!/usr/bin/env python3
# A script to compare parallel texts in TMX and XML
# @author @netbug aka Oleg Urzhumtcev

import lxml.etree as ET

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
            d.append(grp)
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

def compare_data(f_orig, f_comp, b_ignore_spaces = True):
    langs1, t_orig = read_file(f_orig)
    #print(t_orig)
    langs2, t_trans = read_file(f_comp)
    print(t_trans)
    return {"status": "OK", "precision": 0, "recall": 0}

if __name__ == '__main__':
    file_golden = 'data/sample.xml'
    file_compare = 'data/sample.tmx'
    res = compare_data(file_golden, file_compare)
    print(res)