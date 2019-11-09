#https://www.hackerrank.com/rest/contests/master/challenges/diagonal-difference/download_pdf?language=English

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    a=b=range(len(arr))
    l=r=0
    for i,j in zip(a,b):
        l+=arr[i][j]
        r+=arr[abs(i-(len(arr)-1))][j]
    return abs(l-r)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
