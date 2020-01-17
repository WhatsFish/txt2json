#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:49:52 2020

@author: lihaoyang03
"""
import option
import student_info
import Util

import sys
import os
import pandas as pd
import json


# 读取参数
# 如果参数是--help，则跳转到help模块，如果是地质，则读取地址，如果都不是，则显示error
if len(sys.argv)==1:
    option.guide_info(0)
    sys.exit(0)
elif sys.argv[1] == '--help':
    option.guide_info(1)
    sys.exit(0)
elif str.split(sys.argv[1],'=')[0] == "--input":
    path  = str.split(sys.argv[1],'=')[1]
else:
    option.guide_info(2)
    sys.exit(0)

# 获取txt文件信息
# 输入： 文件地址
# 输出： 文件内信息解析结果
info = student_info.txt2json(path)

# 读取年龄
ages = [i[1] for i in info]
# 读取学校  {"school_name":population}
school = {}
for line in info:
    #print(line)
    school_name = line[2]
    student_name = line[0]
    if school_name in school.keys():
        school[school_name] = school[school_name] + 1
    else:
        school[school_name] = 1
# 年龄排序
asc_ages = Util.asc_sort(ages.copy())
desc_ages = Util.desc_sort(ages.copy())

# 单元测试
try:
    if Util.test_asc_sort(asc_ages) and Util.test_desc_sort(desc_ages):
        pass
    else:
        sys.exit(0)
except:
    print("do not pass the unit-test!")

# 生成文档
school_info = {}
school_info["total_count"] = len(school)
school_info["detail"] = school
res = {}
res["school"] = school_info
res["asc_age_list"] = asc_ages
res["desc_age_list"] = desc_ages

print(res)

with open('./result.json','w') as fp:
    fp.write(json.dumps(res))

