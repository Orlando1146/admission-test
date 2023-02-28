#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
question_two.py

'''
from typing import List
from typing import Dict

def count(input: List[int])->Dict[str, int]:
    tmp = {}
    for ch in input:
        if ch in tmp.keys():
            tmp[ch] += 1
        else:
            tmp[ch] = 1
    return tmp

def group_by_key(input: List[Dict])->Dict[str, int]:
    tmp = {}
    for dic in input:
        if dic['key'] in tmp.keys():
            tmp[dic['key']] += dic['value']
        else:
            tmp[dic['key']] = dic['value']
    return tmp

if __name__ == "__main__":
    input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
    input2 = [{'key': 'a', 'value': 3},
            {'key': 'b', 'value': 1},
            {'key': 'c', 'value': 2},
            {'key': 'a', 'value': 3},
            {'key': 'c', 'value': 5}]
    print(count(input1))
    print(group_by_key(input2))
