#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SelectionSort.py
@Time    :   2025/01/07 16:12:27
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

def SelecectionSort(arr):
    n=len(arr)
    for i in range(n):
        #记录最小数的索引
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
        
