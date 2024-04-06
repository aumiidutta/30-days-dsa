class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        row = [1]
        for i in range(1, A+1):
            row = [1] + [row[j] + row[j+1] for j in range(i-1)] + [1]
        return row
