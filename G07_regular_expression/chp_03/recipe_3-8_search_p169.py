"""************************************`
* File: recipe_3-8_search_p169.py
* Author: Iwabuchi Ken                *
* Date: 20120311_130603
* Aim:                                *
*     1.
* <Usage>
*    1. Run the program
* <Source>
*     1.
************************************"""
import re
import sys

def do_regex(subject):
    """ vars """
    #matchobj    = re.search(r"\d+", subject)
    matchobj    = re.search(r"\b\d+\b", subject)
    
    """ processes """
    if matchobj:
        result  = matchobj.group()
    else:    #matchobj
        result  = ""
    #//if matchob
    
    print subject
    print result
#//do_regex(subject)

if __name__ == '__main__':
    #debug
    #print sys.argv
    
    """ vars """
    if len(sys.argv) > 1:
        subject     = sys.argv[1]
    else:    #len(sys.argv) > 
        subject     = "Do you like 12 or 42"
    #//if len(sys.argv) > 
    #subject     = "Do you like 12 or 42"
    do_regex(subject)
