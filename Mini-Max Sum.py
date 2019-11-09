#!/bin/python3
#https://www.hackerrank.com/rest/contests/master/challenges/mini-max-sum/download_pdf?language=English

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    mi=ma=0
    for i in arr[0:-1]:
        mi+=i
    arr.reverse()
    for i in arr[:-1]:
        ma+=i
    print(mi,ma)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
