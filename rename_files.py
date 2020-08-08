#!/usr/bin/python

"""
Problem: Rename files
~~~~~~~~~~~~~~~~~~~~~
Rename all files in the given directory (default to current directory)
 matching the regular expression from_regex by to_regex.

 Usage: rename_files.py from_regex to_regex [dir|.]

 example:
 rename 0 - 9 with _0 to _9 via back reference in the current directory:
 .rename_files.py '([0-9])' '_\1'

"""

import sys, os, re

if not(3 <= len(sys.argv) <= 4):
	print("Usage: ./rename_files.py from_regex to_regex [dir|.]")
	sys.exit(1)

if len(sys.argv) == 4:
	dir = sys.argv[3]
	os.chdir(dir)      # change current working directory

count = 0
for oldfile in os.listdir():
	if os.path.isfile(oldfile):
		newfile = re.sub(sys.argv[1], sys.argv[2], oldfile)
		if oldfile != newfile:
			count += 1
			os.rename(oldfile, newfile)
			print(oldfile, '->', newfile)

print("Number of files renamed: ", count)