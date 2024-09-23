

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   isAnagram.py
@Time    :   2024/09/23 22:32:57
@Author  :   Zihao Zheng 
@Email   :   zhengzihao718@163.com
'''

from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)

from collections import Counter
class Solution():
    def isAnagram(self,s:str,t:str)->bool:
        record =[0]*26 #为26个字母开辟空间
        for i in s:
            record[ord(i)-ord('a')] +=1
        for i in t:
            record[ord(i)-ord('a')] -=1
        for i in record:
            if i !=0:
                return False
        return True
    
    def isAnagram(self,s:str,t:str)->bool:

        cnts = Counter(s) #用哈希表来完成 
        cntt = Counter(t) #用哈希表来完成 
        if cnts==cntt:
            return True
        return False
    
    
    def isAnagram(self,s:str,t:str)->bool:
        from collections import defaultdict
        dict_s=defaultdict(int)
        dict_t=defaultdict(int)
        for i in s:
            dict_s[i]+=1
        for i in t:
            dict_t[i]+=1
        if dict_s==dict_t:
            return True
        return False

    
    
