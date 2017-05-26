#!/usr/bin/env python3
# A script to compare parallel texts in TMX and XML
# @author @netbug aka Oleg Urzhumtcev

def read_TMX(fn):
    pass

def read_XML(fn):
    pass

def read_file(fn):
    return read_TMX(fn) if fn.lower().endswith('.xml') else read_XML(fn)

def compare_data(f_orig, f_comp, b_ignore_spaces = True):
    return {"status": "OK", "precision": 0, "recall": 0}

if __name__ == '__main__':
    file_golden = 'data/text1.xml'
    file_compare = 'data/sample.tmx'
    res = compare_data(file_golden, file_compare)
    print_f(res)