class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i,j=len(nums)-1,-1
        while i>0:
            if nums[i]>nums[i-1]:
                j=i-1
                break
            i-=1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
                nums[j+1:]=sorted(nums[j+1:])
                return 