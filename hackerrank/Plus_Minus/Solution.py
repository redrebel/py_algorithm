#!/bin/python3
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
zero = 0
minus = 0
plus = 0
for i in arr:
    if i==0 :
        zero += 1
    elif i<0 :
        minus += 1
    else :
        plus += 1

print('%f' % float(plus/n))
print('%f' % float(minus/n))
print('%f' % float(zero/n))