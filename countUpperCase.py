#!/usr/bin/python

filename = test.txt
with open(filename) as fh:
    count = 0
    text = fh.read()
    for char in text:
        if char.isUpper():
            count += 1


