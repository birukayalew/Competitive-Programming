#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    d ={}
    ans = []
    for i in range(len(arr)):
        if len(d)>0:
            for key in d:
                if (m-arr[i]) == d[key][0]:
                    ans.append(d[key][1])
                    ans.append(i+1)
                    ans.sort()
                    break
            else:
                d[i] = [arr[i],i+1]
        else:
            d[i] = [arr[i],i+1]
    print(ans)
    return ans
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
