class Solution:
  # @param A: list of integers
  # @return an integer
  def solve(self, A):
    A= list(set(A))
    A.sort()
    n = len(A)
    max = 0
    for i in range(n):
      for j in range(i+1, n):
        mod = A[i] % A[j]
        if mod>max:
          max = mod
    return max
