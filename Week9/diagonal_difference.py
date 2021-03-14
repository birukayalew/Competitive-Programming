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
    
    primary_diagonal = 0
    secondary_diagonal = 0
    last_index = len(arr) - 1 
    for i in range(len(arr)):
        primary_diagonal += arr[i][i]
    for i in range(len(arr)):
        secondary_diagonal += arr[i][last_index]
        last_index -= 1
    return abs(primary_diagonal - secondary_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
