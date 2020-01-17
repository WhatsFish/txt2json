#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:05:43 2020

@author: lihaoyang03
"""
def asc_sort(ages):
    list.sort(ages)
    return ages;

def desc_sort(ages):
    list.sort(ages,reverse = True)
    return ages;

def test_asc_sort(ages):
    for i in range(len(ages)-1):
        if ages[i] > ages[i+1]:
            return False
    return True

def test_desc_sort(ages):
    for i in range(len(ages)-1):
        if ages[i] < ages[i+1]:
            return False
    return True


    
