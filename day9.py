class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        if not A:
            return 0
        
        n = len(A)
        l_max = 0
        r_max = 0
        l = 0
        r = n-1
        trapped = 0
        
        while l<r:
            if A[l]<A[r]:
                if A[l]>l_max:
                    l_max = A[l]
                else:
                    trapped += l_max - A[l]
                l += 1
            
            else:
                if A[r]>r_max:
                    r_max = A[r]
                else:
                    trapped += r_max - A[r]
                r -= 1
        
        return trapped
