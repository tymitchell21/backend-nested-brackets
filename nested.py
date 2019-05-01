#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "tymitchell21"

import sys

def valid_parentheses(string):
    openers = ["(", "[", "{", "<", "(*"]
    closers = [")", "]", "}", ">", "*)"]
    index = 0
    pos = 0
    bracketIndex = []

    while index < len(string):
        pos += 1
        if index + 1 < len(string):
            char = string[index] + string[index + 1]
            if char in openers:
                bracketIndex.append(openers.index(char))
                index += 2
                continue
            elif char in closers:
                if closers.index(char) != bracketIndex[-1]:
                    return "NO " + str(pos)
                bracketIndex.pop()
                index += 2
                continue
        char = string[index]
        if char in openers:
            bracketIndex.append(openers.index(char))
            index += 1
        elif char in closers:
            if closers.index(char) != bracketIndex[-1]:
                return "NO " + str(pos)
            bracketIndex.pop()
            index += 1
        else:
            index += 1


    if len(bracketIndex) == 0:
        return "YES"
    else:
        return "NO " + str(index)
        
def main(args):
    """Add your code here"""
    if len(sys.argv) != 2:
        print 'usage: python nested.py file-to-read'
        sys.exit(1)

    with open(args[1], 'r') as f:
        contents = f.readlines()
        with open("output.txt", "w") as w:
            for line in contents:
                w.write(valid_parentheses(line) + '\n')


if __name__ == '__main__':
    main(sys.argv)