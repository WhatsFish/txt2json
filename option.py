#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:48:15 2020

@author: lihaoyang03
"""

def guide_info(message):
    if message == 0:
        print("Usage of main.py:")
        print("    --input: specify file path")
        print("")
        print("Examples:")
        print("    1. print usage:")
        print("       python main.py --help")
        print("    2. specify input file: conf/student_info.txt")
        print("")
        print("       python main.py --input=\"onf/student_info.txt\"")
    elif message == 1:
        print("welcome to help page")
        print("        python main.py --input=file_path")
    elif message == 2:
        print("please type in as follows:")
        print("        python main.py --help")
        print("        python main.py --input=file_path")
      