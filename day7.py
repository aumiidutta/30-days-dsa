class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        #simply transpose and reverse rows
        n = len(A)

        #transpose
        for i in range(n):
            for j in range(i, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]

        #reverse
        for lst in A:
            lst.reverse()

        return A
