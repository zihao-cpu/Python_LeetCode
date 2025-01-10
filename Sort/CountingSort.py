#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   CountingSort.PY
@Time    :   2025/01/10 11:07:22
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
#计数排序
#统计各个数字出现的次数，然后根据次数将数字分配到相应的位置
def counting_sort(arr):
    maxValue=max(arr)
    bucket=[0]*maxValue
    for i in range(len(arr)):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1

    SortedIndex=0
    for i in range(len(bucket)):
        while bucket[i]>0:
            arr[SortedIndex]=i
            SortedIndex+=1
            bucket[i]-=1
    return arr
