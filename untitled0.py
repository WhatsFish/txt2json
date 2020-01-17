#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:47:38 2020

@author: lihaoyang03
"""
b = ['30', '30', '27', '27', '25', '24', '24', '24', '24', '23', '23', '23']
c = {'Peking University\n': 2, 'Northwestern Polytechnical University\n': 2, 'Xidian University\n': 2, 'Wuhan University\n': 2, 'Tsinghua University\n': 3, 'Fudan University\n': 1}
for (key,value) in c.items():
    print(key)
    print(value)
    
    
filename = 'test.txt'
with open(filename, 'w') as file_object:
    file_object.writelines(b)
    

filename = 'result.json'
with open(filename, 'w') as file_object:
    file_object.write("{\n")
    file_object.write("    \"school_info\" : {\n")
    file_object.write("                     \"total_count\": {0},\n".format(len(school)))
    file_object.write("                     \"detail\"     : {\n")
    for (k,v) in school.items():
        file_object.write("                                      \"{0}\": {1},\n".format(k.strip('\n'),v))
    file_object.write("                                     },\n")
    file_object.write("    \"asc_age_list\" : [")
    for ages in range(len(asc_ages)-1):
        file_object.write(asc_ages[ages])
        file_object.write(", ")
    file_object.write(asc_ages[-1])
    file_object.write("],\n")
    file_object.write("    'desc_age_list': [")
    for ages in range(len(desc_ages)-1):
        file_object.write(desc_ages[ages])
        file_object.write(", ")
    file_object.write(asc_ages[-1])
    file_object.write("]\n")
    file_object.write("}")