class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        total=0
        n=len(mat)
        for i in range(n):
            if i==n-1-i:
                total+=mat[i][i]
            else:
                total+=mat[i][i] + mat[i][n-1-i]
        return total
