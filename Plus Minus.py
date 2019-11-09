#!/bin/python3
#https://www.hackerrank.com/rest/contests/master/challenges/plus-minus/download_pdf?language=English

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p=n=z=0
    for i in arr:
        if i>0:
            p+=1
            continue
        elif i<0:
            n+=1
            continue
        z+=1
    print('{:6}'.format(p/len(arr)))
    print('{:6}'.format(n/len(arr)))
    print('{:6}'.format(z/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
