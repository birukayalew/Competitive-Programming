#!/bin/python3

import os
import sys
import heapq as heap
#
# Complete the cookies function below.
#

def cookies(k, A):
    operations=0
    heap.heapify(A)
    while len(A)>1 and A[0]<k:
        leastSweatCookie=heap.heappop(A)
        secondLeastSweatCookie=heap.heappop(A)
        heap.heappush(A,1*leastSweatCookie + 2* secondLeastSweatCookie)
        operations+=1
    if A[0]<k:
        return -1
    return operations
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
