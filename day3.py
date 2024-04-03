class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        even = sum(1 for num in A if num%2 ==0)
        n = len(A)
        odd = n - even
        return min(even, odd)
