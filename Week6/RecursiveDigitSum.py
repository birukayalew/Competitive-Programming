#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    x = total(n)
    return total(x*k)
def total(n):
    summ=0
    if len(n)==1:
        return n
    for i in range(len(n)):
        summ+=int(n[i])
    return total(str(summ))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
