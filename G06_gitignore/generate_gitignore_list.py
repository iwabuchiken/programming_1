"""************************************`
* generate_gitignore_list.py
* Author: Iwabuchi Ken				*
* Date: 20120308_174545
* Aim:								*
* 	1.
* <Usage>
*	1. Run the program
* <Source>
* 	1.
************************************"""
import os.path
#from multiprocessing import join
import os
import sys
import inspect

def set_extension_data(file_name="extensions.dat"):
    """ vars """
    file_path   = os.path.join(os.path.dirname(__file__), file_name)
#    f       = file(file_name)   #   data file
    f       = file(file_path)   #   data file
    exts    = list()            #   hold extensions

    """ read lines """
    line = f.readline()
    while line:
        exts.append(line.rstrip('\r\n'))
        line = f.readline()
    #//while (f.readline())

    #debug
    """ show exts """
    #print exts

    """ return """
    return exts

#//set_extension_data()

def set_omit_dirs_data(file_name="omit.dat"):
    """ vars """
    file_path   = os.path.join(os.path.dirname(__file__), file_name)
#    f       = file(file_name)   #   data file
    f       = file(file_path)   #   data file
    omit_dirs_a  = list()            #   hold extensions

    """ read lines """
    line = f.readline()
    while line:
        omit_dirs_a.append(line.rstrip('\r\n'))
        line = f.readline()
    #//while (f.readline())

    #debug
    """ show exts """
    #print exts

    """ return """
    return omit_dirs_a

#//def set_omit_dirs_data(file_name="extensions.dat")

""" 
write_to_file()

"""
def write_to_file(new_path, ignore_files, file_name):
    file_out    = file(file_name, "a")
#    file_out    = file(file_name, "w")
    for item in ignore_files:
        name    = "*.%s" % item
        string  = "/".join((new_path, name))
        file_out.write(string + "\n")
    #for item in ignore_files

    """ close file  """
    file_out.close()
#//write_to_file()
"""
Algorythm of the function "get_path()"
	(Reminder)
		Both s1 and s2 are defined as string in the function
		parameter brace, yet in this instruction, please assume
		that both are turned into arrays using such methods as
		"split()"
(Set variables)
1. root path s1, current path s2	
2. set the index for the both as i, starting from 0

(Process elements)
3. compare the chars at index i of the two arrays
4. increment i if the two chars equal, using a while loop
5. if the two chars don't equal, exit the loop

(Construct a new string)
6. At the exit point, i is 1 point larger than the length of s1
7. Decrement i by 1
8. A subarray of s2, i.e. s2[i:], is the new array s3.
9. Modify s3:
	(1) The first element changed to "."
	(2) Join the elements using "/"(slash, not back slash) 
	(3) The generated string will be the path you wanted

(Example)
	(1) Data: s1="c:\a\b", s2="c:\a\b\c\d"
	(2) Result: s3="./c/d" (Notice: A slash is NOT added at the tail
		of s3)
"""
def get_path(root_path, current_path):
	"""
	 variables
	 1. root_path_a: array
	 2. current_path_a
	 3. new_path_a: array
	 4. new_path: str
         5. next_path_a: array  => list of dirs for recurse
	 4. i: int		=>	index for root_path, current_path
	 5. k: int	=>	index for new_path
         6. file_out: file      => ouput file
         7. file_name: str      => file name
         8. ignore_files: array/str => files to be ignored
	"""
	root_path_a	= root_path.split("\\")
	current_path_a	= current_path.split("\\")
	i						= 0
	k						= 0
	file_name       = ".gitignore"
#        ignore_files    = ["obj", "tds", "o", "exe", "class", "mk"]
	ignore_files    = set_extension_data()

	""" compare """
	#for i in range(len(root_path_a)):
	while (i < len(root_path_a) 
				and root_path_a[i] == current_path_a[i]):
		#print "match: %s || %s" % (root_path_a[i], current_path_a[i])
		i += 1
		#print "Now i is: %d" % i
		#while (root_path_a[i] == current_path_a[i])
	""" get a path string	"""
	new_path_a		= current_path_a[(i - 1):]
	new_path_a[0]	= "."
	new_path			= "/".join(new_path_a)
	#debug
	#print "new_path_a=", new_path_a
	#print "new_path=", new_path

        """ write to the file   """
        write_to_file(new_path, ignore_files, file_name)
	
#	""" get a new dir list	"""
        
        """ recurse the method	"""	
        omit_dirs_a = set_omit_dirs_data()
        
        #debug
        print "[LINE:%d]" % inspect.currentframe().f_lineno
        print "omit_dirs_a=", omit_dirs_a
        
        next_path_a     = [x for x
                in os.listdir(current_path)
                #if os.path.isdir(os.path.join(current_path, x))]
                if os.path.isdir(os.path.join(current_path, x)) and
                x not in omit_dirs_a]
#                if os.path.isdir(x)]

        print "[LINE:%d]" % inspect.currentframe().f_lineno
        print "next_path_a=", next_path_a
        #print "current_path=", current_path
	#print "os.listdir(current_path)=", os.listdir(current_path)
	#print "next_path_a=", next_path_a

#        for item in os.listdir(current_path):
        for item in next_path_a:
		#print "\t", os.path.join(current_path, item)
			get_path(root_path, os.path.join(current_path, item))
	#//for item in os.listdir(current_path)		
	#print	
	#new_path		= 
	#//for i in range(len(root_path_a)
	
	#print current_path_a[(i - 1):]
	#debug
	"""
	#print root_path_a[i:]
	#print current_path_a[i:]
	#print
	"""

def set_up():
    """ variables """
    root_path	= os.getcwd()           			#   the root dir
    entries_a      = os.listdir(root_path)	#   the entries in the root
    dirs_a	= [x for x in entries_a if os.path.isdir(x)]
                                        					#   the dirs among the entries
    git_file_name   = ".gitignore"		   	     #  .gitignore file

    """ delete the existing file """
    if git_file_name in entries_a:
        os.remove(os.path.join(root_path, git_file_name))

    """ return """
    return root_path, dirs_a
#//set_up()

if __name__ == '__main__':

    """ variables """
    root_path, dirs_a   = set_up()

    """ get path """

    """ modify dirs_a """
    
    for item in dirs_a:
        get_path(os.getcwd(), os.path.abspath(item))
