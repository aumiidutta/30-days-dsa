class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        seen = set()

        for ele in A:
            if ele in seen:
                a = ele
            seen.add(ele)
        
        for i in range(1, n+1):
            if i not in A:
                b = i

        return a, b
