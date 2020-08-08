#!/usr/bin/python

"""
Problem: Word Count
~~~~~~~~~~~~~~~~~~~
Read a fie given in the command-line argument and print the number of 
lines, words and characters - similar to UNIX's wc utility

"""
import sys

# check if the filename is given in the command line arguments using sys module

# command line arguments are kept in a list sys.argv
if len(sys.argv) != 2:
	print("Usage: ./wordCount.py <filename>")
	sys.exit(1)  # return a non-zero value to indicate abnormal termination

# variables are created via initial assignment
num_lines = num_words = num_chars = 0

# Get input filename from list sys.argv
# sys.argv[0] is the script name, sys.argv[1] is the filename
with open(sys.argv[1]) as infile:    # with-as closes the file automatically
	for line in infile:              # process each line (including newline) in a for-loop
		num_lines += 1            
		num_chars += len(line)       
		line = line.strip()          # remove leading and trailing whitespace as delimiter
		words = line.split()
		num_words += len(words)


print("Number of lines: {}".format(num_lines))
print("Number of words: {0:5d}".format(num_words))
print("Number of Characters: %8.2f" % num_chars)

# Invoke Unix utility 'ws' through shell command for comparision
from subprocess import call
call(['wc', sys.argv[1]])   # command in a list

import os
os.system('wc ' + sys.argv[1])



"""
html escape - Escape the given html file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Replace the HTML reserved characters by their corresponding HTML entities

" is replaced with &quot;
& is replaced with &amp;
< is replaced with &lt;
> is replaced with &gt
Usage: htmlescape.py infile outfile
"""

"""

import sys

if len(sys.argv) != 3:
	print("Usage: ./htmpescape.py infile outfile")
	sys.exit(1)

with open(sys.argv[1]) as infile, open(sys.argv[2]) as outfile:
	for line in infile:
		line = line.rstrip()

		#Encode HTML &, <, >, ". The order of substitution is important
		line = line.replace('&', '&amp')
		line = line.replace('<', '&lt')
		line = line.replace('>', '&gt')
		line = line.replace('"', '&quot')
		outfile.write('%s\n' % line)    # write() does not support newline
"""