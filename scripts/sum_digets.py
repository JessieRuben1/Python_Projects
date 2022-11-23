# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:15:52 2021

@author: admin
"""

#def solution(n):
#    sum = 0
#     while(sum != 0):
 #        sum = sum + (n%10)
  #       n = n//10
   #  return sum

#print(solution(29))
def getSum(n):
    
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum
   
n = 29
print(getSum(n))