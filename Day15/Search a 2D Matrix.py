class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res=[j for i in matrix for j in i]
        if target in res:
            return True
        else:
            return False