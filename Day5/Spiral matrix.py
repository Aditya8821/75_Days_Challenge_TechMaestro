class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        rowbeg,rowend=0,len(matrix)-1
        colbeg,colend=0,len(matrix[0])-1
        while rowbeg<=rowend and colbeg<=colend:
            for i in range(colbeg,colend+1):
                res.append(matrix[rowbeg][i])
            rowbeg+=1
            for i in range(rowbeg,rowend+1):
                res.append(matrix[i][colend])
            colend-=1
            if rowbeg<=rowend:
                for i in range(colend,colbeg-1,-1):
                    res.append(matrix[rowend][i])
                rowend-=1
            if colbeg<=colend:
                for i in range(rowend,rowbeg-1,-1):
                    res.append(matrix[i][colbeg])
                colbeg+=1
        return res
    