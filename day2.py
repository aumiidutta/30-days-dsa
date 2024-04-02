class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        n = len(A)
        mi = min(A)
        ma = max(A)
        for i in range(n):
            if A[i]>mi and A[i]<ma:
                count +=1
        return count
