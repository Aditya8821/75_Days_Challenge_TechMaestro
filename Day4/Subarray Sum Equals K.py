class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        running_sum=0
        count=0
        for num in nums:
            running_sum+=num
            if running_sum-k in d:
                count+=d[running_sum-k]
            if running_sum in d:
                d[running_sum]+=1
            else:
                d[running_sum]=1
        return count