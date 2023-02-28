#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
question_one.py

'''
from typing import List

def find_max(numbers: List[int])->int:
    tmp = 0
    for i in numbers:
        if i > tmp:
            tmp = i
    return tmp

def find_position(numbers: List[int], target: int)->int:
    tmp = 0
    while tmp < len(numbers):
        if target == numbers[tmp]:
            return tmp
        tmp += 1
    return -1

if __name__ == "__main__":
    print(find_max([1, 2, 4, 5]))
    print(find_max([5, 2, 7, 1, 6]))
    print(find_position([5, 2, 7, 1, 6], 5))
    print(find_position([5, 2, 7, 1, 6], 7))
    print(find_position([5, 2, 7, 7, 7, 1, 6], 7))
    print(find_position([5, 2, 7, 1, 6], 8))
