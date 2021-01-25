#!/bin/python3

import os
import sys
import math
import heapq as heap
#
# Complete the runningMedian function below.
#
def balance(minheap,maxheap):
    if len(maxheap)>len(minheap):
        if len(minheap)==0:
            heap.heapify(minheap)
        poped=heap.heappop(maxheap)
        heap.heappush(minheap,-1*poped)
    elif len(minheap)>len(maxheap):
        poped=heap.heappop(minheap)
        heap.heappush(maxheap,-1*poped)
def runningMedian(a):
    ans=[]
    minheap=[]
    maxheap=[]
    for i in range(len(a)):
        if i==0:
            heap.heapify(maxheap)
            heap.heappush(maxheap,-1*a[i])
        else:
            if a[i]<(-1*maxheap[0]):
                heap.heappush(maxheap,-1*a[i])
            else:
                if len(minheap)==0:
                    heap.heapify(minheap)
                heap.heappush(minheap,a[i])
        if math.fabs((len(minheap)-len(maxheap)))==2:
            balance(minheap,maxheap)
        if len(minheap)==len(maxheap):
            ans.append(((minheap[0]+(-1*maxheap[0]))/2)*1.0)
        elif len(minheap)>len(maxheap):
            ans.append(minheap[0]*1.0)
        else:
            ans.append((-1*maxheap[0])*1.0)   
    return ans
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
