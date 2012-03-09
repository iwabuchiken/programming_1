"""************************************`
 * Q2.java
 * Author: Iwabuchi Ken				*
 * Date: 20120308_174545
 * Aim:								*
 * 	1.
 * <Usage>
 *	1. Run the program
 * <Source>
 * 	1.
 ************************************"""
import os
import sys

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
	 4. i: int		=>	index for root_path, current_path
	 5. k: int	=>	index for new_path
	"""
	root_path_a		= root_path.split("\\")
	current_path_a	= current_path.split("\\")
	i						= 0
	k						= 0
	
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
	print "new_path_a=", new_path_a
	print "new_path=", new_path
	
	""" get a new dir list	"""
	print os.listdir(current_path)
	
	""" recurse the method	"""	
	for item in os.listdir(current_path):
		print "\t", os.path.join(current_path, item)
		get_path(root_path, os.path.join(current_path, item))
	#//for item in os.listdir(current_path)		
	print	
	#new_path		= 
	#//for i in range(len(root_path_a)
	
	#print current_path_a[(i - 1):]
	#debug
	"""
	print root_path_a[i:]
	print current_path_a[i:]
	print
	"""
	#debug
	#print "root_path_a=", root_path_a
	#print "current_path_a=", current_path_a
	#print
#//get_path()

if __name__ == '__main__':
	""" variables """
	root_path		= os.getcwd()
	dirs_a			= os.listdir(root_path)
	
	""" get path """
	print "root_path=", root_path
	#print dirs_a
	
	""" modify dirs_a """
	dirs_a	= [x for x in dirs_a if os.path.isdir(x)]
	for item in dirs_a:
		get_path(os.getcwd(), os.path.abspath(item))
		#print os.path.dirname(item)
		#print os.path.abspath(item)
	#//for item in dirs_a
	
	#get_path(os.getcwd(), os.getcwd() + r"\a\b\c")
	
	