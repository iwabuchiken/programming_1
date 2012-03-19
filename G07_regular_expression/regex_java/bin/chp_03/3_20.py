"""************************************`
 * 3_20.py
 * Author: Iwabuchi Ken                *
 * Date: 20120315_072910
 * Aim:                                *
 *     1.
 * <Usage>
 *    1. Run the program
 * <Source>
 *     1.
 ************************************"""
import os
import sys
import inspect
import re

def func1():
    """  """
    target_string   = "I like <b>bold</b> and <i>italic</i> fonts"
    reobj               = re.compile("<[^<>]*>")
    result              = reobj.split(target_string)
    
    """ display """
    print "target=%s" % target_string
    print "result=%s" % result
    print "string=%s" % "".join(result)
#//func1()
if __name__ == '__main__':
    func1()

#print "[LINE:%d]" % inspect.currentframe().f_lineno