# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:32:50 2021

@author: admin
"""
def shortestPalindrome( s):
        """
        :type s: str
        :rtype: str
        """
        def getPrefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j > -1 and pattern[j+1] != pattern[i]:
                    j = prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        if not s:
            return s
            
        A = s + s[::-1]
        prefix = getPrefix(A)
        i = prefix[-1]
        while i >= len(s):
            i = prefix[i]
        return s[i+1:][::-1] + s
    
s = "abcdc"
print(shortestPalindrome(s))
