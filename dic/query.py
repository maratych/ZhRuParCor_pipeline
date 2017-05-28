#!/usr/bin/env python
import sys
try:
    from DictionaryServices import *
except:
    print ("WARNING: The pyobjc Python library was not found. You can install it by typing: 'pip install -U pyobjc'")
    print ("..................\n")
    

try:
    from colorama import Fore, Back, Style
except:
    print ("WARNING: The colorama Python library was not found. You can install it by typing: 'pip install colorama'")
    print ("..................\n")

def main():
    fo = open("outdic.txt", 'w', encoding='utf-8')
    with open('bkrs_entries.txt', 'r', encoding='utf-8') as fh:
        for word in fh:
            word = word.strip()
            defi = query(word)
            if defi != None:
              # saving to dict
              fo.write(word + "\n")


def query(searchword):
    wordrange = (0, len(searchword))
    dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
    if not dictresult:
        return None
    else:
        s = dictresult
        return s
        arrow = doColor("\n\n\xe2\x96\xb6 ", "red")
        s = s.replace('\xe2\x96\xb6', arrow)  # arrow
        
        bullet = doColor("\n\xe2\x80\xa2 ", "red")        
        s = s.replace('\xe2\x80\xa2', bullet)        # bullet
        
        phrases_header = doColor("\n\nPHRASES\n", "important")
        s = s.replace('PHRASES', phrases_header)
        
        derivatives_header = doColor("\n\nDERIVATIVES\n", "important")
        s = s.replace('DERIVATIVES', derivatives_header)
        
        origin_header = doColor("\n\nORIGIN\n", "important")
        s = s.replace('ORIGIN', origin_header)
        
        print (doColor("Dictionary entry for:\n", "red"))
        print (s)
        print ("\n---------------------------------")


def doColor(s, style=None):
    """
    util for returning a colored string
    if colorama is not installed, FAIL SILENTLY
    """
    try:
        if style == "comment":
            s = Style.DIM + s + Style.RESET_ALL
        elif style == "important":
            s = Style.BRIGHT + s + Style.RESET_ALL
        elif style == "normal":
            s = Style.RESET_ALL + s + Style.RESET_ALL        
        elif style == "red":
            s = Fore.RED + s + Style.RESET_ALL        
        elif style == "green":
            s = Fore.GREEN + s + Style.RESET_ALL                        
    except: 
        pass
    return s



if __name__ == '__main__':
    main()