class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        moves = 0 
        A.sort() 
        for i in range(len(A)-1):
            if A[i] == A[i+1] or A[i] > A[i+1]: 
                moves += A[i] + 1 - A[i + 1]  
                A[i+1] =  A[i] + 1
        return moves
