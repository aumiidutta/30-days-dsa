class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        n = len(A)
        for i in range(n-1):
            if (A[i] + A[i+1])%2==0:
                count += 1
        ans = n - count
        return ans
