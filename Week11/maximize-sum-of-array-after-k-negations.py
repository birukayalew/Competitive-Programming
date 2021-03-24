class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i in range(len(A)):
            if K == 0:
                return sum(A)
            elif A[i] < 0:
                A[i] = A[i] * -1
            else:
                if K % 2 == 0:
                    return sum(A)
                return (sum(A) - (min(A) * 2))
                
            K -= 1
                
        
