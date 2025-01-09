#堆排序 
#1.生成最小堆，每一个父节点的值都小于等于它的子节点的值。
#2.将堆顶元素与最后一个元素交换，然后将堆的大小减一，并对新的堆顶元素进行调整，使其满足最小堆的性质。
#3.重复步骤2，直到堆的大小为1。
#4.将堆中的元素逐个输出。
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   heapSort.py
@Time    :   2025/01/09 21:13:06
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''


#数组生成堆的形式
arr=[4,7,3,2,1]
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
def upheap(arr,i):
    parent=(i-1)//2
    if parent>=0 and arr[i]<arr[parent]:
        swap(arr,i,parent)  
        upheap(arr,parent)
    return arr


def buildheap(arr):
    n=len(arr)
    arr_new=[]
    for i in range(n):
        arr_new.append(arr[i])
        arr_new=upheap(arr_new,i)
    return arr_new

def buildheap(arr):
    n=len(arr)  
    for i in range(n):
        arr=upheap(arr,i)
    return arr


def downheap(arr,i,n):
    left=2*i+1
    right=2*i+2
    smallest=i
    if  left<n and arr[left]<arr[smallest]:
        smallest=left
    if  right<n and arr[right]<arr[smallest]:
        smallest=right       
    if smallest!=i:
        swap(arr,i,smallest)
        downheap(arr,smallest,n)
    return arr

# arr=buildheap(arr)
# arr_new=[]
# while arr:
#     swap(arr,0,len(arr)-1)
#     arr_new.append(arr.pop())
#     arr=downheap(arr,0,len(arr)-1)
def heapSort(arr):
    arr=buildheap(arr)
    arr_new=[]
    while arr:
        swap(arr,0,len(arr)-1)
        arr_new.append(arr.pop())
        arr=downheap(arr,0,len(arr)-1)
    return arr_new

if __name__ == '__main__':
    arr=[10,5,4,7,3,2,1]
    print(heapSort(arr))
