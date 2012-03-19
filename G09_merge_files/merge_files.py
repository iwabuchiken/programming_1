"""************************************`
 * merge_files.py
 * Author: Iwabuchi Ken				*
 * Date: 20120316_105144
 * Aim:								*
 * 	1.
 * <Usage>
 *	1. Run the program
 * <Source>
 * 	1.
 ************************************"""
import os
import sys
import inspect
import traceback
import re

def merge_files():
    """ open files """
    file_name_original  = "program.cpp"     # original file
    file_name_new       = "program_new.cpp" # new file
#    file_original       = file(file_name_original, "a") # open in add mode
#    file_original       = file(file_name_original, "r+") # open in revise mode
#    file_new            = file(file_name_new, "r") # open in read mode
    file_original       = open(file_name_original, "r+") # open in revise mode
    file_new            = open(file_name_new, "r") # open in read mode



    """ read content """
#    original_content    = list()
#    for line in file_original:
#        original_content.append(line)
#    #for line in file_original


    original_content    = file_original.readlines()
    new_content         = file_new.readlines()

#    #debug
#    print "original_content="
#    print original_content

    """ search functions """
    #compile
    reg     = re.compile("^(\w+\s)\w+::([\w_]+\(\))")
    

#//merge_files()

def create_header_file():
    """ open files """
    file_name_original  = "program.h"     # original file
    file_name_new       = "program_new.h" # new file
    file_original       = open(file_name_original, "r") # open in revise mode
    file_new            = open(file_name_new, "a") # open in read mode

    """ read content """
    reg = re.compile("[\s\t]*(\w+\s)([\w_]+)\(\);") # set a regex
    original_line = file_original.readline()
    print original_line
#    while (True):
    while (original_line != ""):
        """ read a line """
        original_line = file_original.readline()
        """ "public"? """
        if original_line == "public":
#            reg = re.compile("[\s\t]*(\w+\s)([\w_]+)\(\);")
#            reg = re.compile("^\s+(\w+\s)([\w_]+)\(\);")
#            original_line = file_original.readline()
            while (True):
                original_line = file_original.readline()
                if original_line == "private" \
                            or original_line == "}":
                    break
                else:
                    print "original_line=", original_line
#                    res = reg.search(original_line)
            #//if original_line == "private" or original_line == "}"
            #//while (True)

#//if original
        else:
            continue
#//if original_line == "public"
        break
    #//while (True)

    """ search functions """
    #compile
    reg     = re.compile("^(\w+\s)\w+::([\w_]+\(\))")

#//create_header_file()

if __name__ == '__main__':
#    merge_files()
    create_header_file()
#print "[LINE:%d]" % inspect.currentframe().f_lineno
#traceback.print_exc(file=sys.stdout)
#   => http://www.python.jp/doc/2.5/lib/traceback-example.html