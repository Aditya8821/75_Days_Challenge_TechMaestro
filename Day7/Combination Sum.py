class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final=[]
        def solve(index,candidates,tar,final,res):
            if index==len(candidates):
                if tar==0:
                    final.append(res.copy())
                    return
                return 
            if candidates[index]<=tar:
                res.append(candidates[index])
                solve(index,candidates,tar-candidates[index],final,res)
                res.pop()
            solve(index+1,candidates,tar,final,res)
        solve(0,candidates,target,final,[])
        return final