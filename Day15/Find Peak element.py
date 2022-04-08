class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start,end=0,len(nums)-1
        if len(nums)==1:
            return 0
        while start<end:
            mid=(end+start)//2
            if nums[mid]>nums[mid+1]:
                end=mid
            else:
                start=mid+1
        return start