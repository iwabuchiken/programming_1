"""************************************`
* File: recipe_3-15_search_and_replace_p206.py
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
    result    = re.sub(r"\bSahara\b", "Mohave", subject)
    
    """ processes """
    
    print "subject="
    print subject
    print
    print "result="
    print result
#//do_regex(subject)

if __name__ == '__main__':
    #debug
    #print sys.argv
    
    """ vars """
    subject = file("3-15.txt", "r").read() 
    #subject     = "Do you like 12 or 42"
    do_regex(subject)
