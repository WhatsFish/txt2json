#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:48:35 2020

@author: lihaoyang03
"""


def txt2json(file_path):
    data = []
    for line in open(file_path,"r"):
        data.append(str.split(line,';'))
    return data