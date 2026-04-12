class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # This is the O(nm) solution
        n = len(matrix)
        for row in matrix:
            for j in row:
                if j == target: return(True)

        return(False)
        