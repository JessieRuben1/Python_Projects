#Return the second highest score
'''
n = int(input())
arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])
'''
arr = [5,6,8,8,10,78,5,100]
#sort the array, then display second last value
arr.sort()
print(arr[-2])