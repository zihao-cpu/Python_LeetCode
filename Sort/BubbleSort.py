#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   BubbleSort.PY
@Time    :   2025/01/07 16:07:00
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr