#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   radix.py
@Time    :   2025/01/10 11:28:21
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def radix_sort(arr):
    digit=0
    maxValue=max(arr)
    max_digit=0
    while 10**max_digit<=maxValue:
        max_digit+=1
#先根据个位数排序，再根据十位数排序，直到最高位数排序结束   
    while digit<max_digit:
        buckets=[[] for _ in range(10)]
        for num in arr:
            digit_value=num//(10**digit)%10  # int((num/10**digit)%10)
        buckets[digit_value].append(num)
        arr_new=[]
        for bucket in buckets:
            for i in bucket:
                arr_new.append(i)
        arr=arr_new
        digit+=1
    return arr