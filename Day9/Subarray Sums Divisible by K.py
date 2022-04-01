class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder={}
        remainder[0]=1
        s=0
        count=0
        for i in range(len(nums)):
            s+=nums[i]
            if s%k in remainder:
                count+=remainder[s%k]
                remainder[s%k]+=1
            else:
                remainder[s%k]=1
        return count