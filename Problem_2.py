# We use Dp for this program.
# Time complexity = O(n*n)
# Space Complexity = O(n*n)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        dp_matrix = [[None for i in range(0,n)] for j in range(0,n)]

        for i in range(0,n):
            dp_matrix[0][i] = matrix[0][i]
        for i in range(1,n):
            for j in range(0,n):

                if j==0:
                    dp_matrix[i][j] = matrix[i][j] + min(dp_matrix[i-1][j],dp_matrix[i-1][j+1])
                elif j==n-1:
                    dp_matrix[i][j] = matrix[i][j] + min(dp_matrix[i-1][j],dp_matrix[i-1][j-1])
                else:
                    dp_matrix[i][j] = matrix[i][j] + min(dp_matrix[i-1][j],min(dp_matrix[i-1][j-1],dp_matrix[i-1][j+1]))
        
        return min(dp_matrix[n-1])




        