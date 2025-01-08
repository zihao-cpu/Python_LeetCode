#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   QuickSort.py
@Time    :   2025/01/08 19:31:23
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def quick_sort(arr):

    left=0
    right=len(arr)-1
    partition_index=partition(arr, left, right)
    quick_sort(arr,left,partition_index-1)
    quick_sort(arr,partition_index+1,right) 

    return arr

#最终的index前的数都比index小，index后面的数都比index大
def partition(arr, left, right):
    pivot = arr[left]
    index=pivot+1
    i= index
    while i<=right:
        if arr[i]<arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr, pivot, index-1)
    return index-1 
def swap(arr, i, j):
    arr[i],arr[j]=arr[j],arr[i]           
