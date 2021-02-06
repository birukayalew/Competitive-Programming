#!/bin/python3

import math
import os
import random
import re
import sys
import heapq as h

# Complete the minimumLoss function below.
def minimumLoss(price):
    ans=[]
    minimum = float('inf')
    for i in range(len(price)):
        ans.append([price[i],i+1])
    ans.sort(key = lambda x:x[0])
    for i in range(len(ans)-1,0,-1):
        if ans[i][1] < ans[i-1][1]:
            diff = ans[i][0] - ans[i-1][0]
            minimum = min(minimum,diff)  
    return minimum
        
    
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
