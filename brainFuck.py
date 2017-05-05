#! /usr/bin/python3
# A simple brainfuck interpreter
# 15 Dec 2016

import sys
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

brain = ['+','-','>','<','.',',','[',']']

# Accept the input from either the stdio or from a file name

if (len(sys.argv) == 2):
    file = open(sys.argv[1])
    data = file.read()
else:
    data = sys.stdin.readlines()

logging.debug('Data input completed! ' + str(data))

strr = ''

for i in data:
    if i != '\n':
        if i != ' ':
            if i != '\r':
                if i != '\f':
                    strr+=i

data = strr[:-1]

# Check the input for inconsistencies

logging.debug('Consistency check begun')

for i in data:
    if i not in brain:
        print("Inconsistent data: Invalid character detected.")
        print(i)
        exit()

logging.debug('This is data: ' + str(data))

# Check for loop balancing

logging.debug('Loop balancing check')



# Clean-up the given input

# Establish an array with the help of source.

# Process the input

