class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # This is the O(nm) solution
        n = len(matrix)
        #for row in matrix:
        #    for j in row:
        #        if j == target: return(True)

        #return(False)

        # now for a faster solution
        search = n-1
        for i in range(n):
            if target < matrix[i][0]:
                
                print(target, "is less than", matrix[i][0])
                search = i-1
                break
        if search > n-1: return(False)
        if search < 0: return(False)
        print(matrix[search])
        for i in matrix[search]:
            if i == target: return(True)
        return(False)
        
         
        