#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SortArrrayByPairtyII.py
@Time    :   2025/01/13 21:06:02
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''
def sortArrayByParityII(nums):
    # 初始化结果数组，用于存储按奇偶性排序后的元素
    result=[]
    # 初始化奇数索引，指向结果数组中下一个存放奇数的位置
    oddIndex=1
    # 初始化偶数索引，指向结果数组中下一个存放偶数的位置
    evenIndex=0
    # 遍历输入数组中的每个数字
    for num in nums:
        # 如果数字是偶数，将其放置在偶数索引位置，并更新偶数索引
        if num%2==0:
            result[evenIndex]=num
            evenIndex+=2
        # 如果数字是奇数，将其放置在奇数索引位置，并更新奇数索引
        else:
            result[oddIndex]=num
            oddIndex+=2
    # 返回按奇偶性排序后的结果数组
    return result

