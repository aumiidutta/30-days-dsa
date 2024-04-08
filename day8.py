class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        sum = A[0]
        current = A[0]
        for i in A[1:]:
            current = max(i, current + i)
            sum = max(sum, current)
        return sum
