#!/usr/bin/python3
## Script to reverse a string entered either through the terminal or from a file. Use: "./reverse.py < file.txt"

from sys import argv, stdin, stdout

string=[]

for line in stdin:
    stdout.write(line)
    string.append(line)
    print(string)

for ele in string:
    ele=ele.strip()
    print(ele)
    ele = ele[::-1]
    print(ele)
