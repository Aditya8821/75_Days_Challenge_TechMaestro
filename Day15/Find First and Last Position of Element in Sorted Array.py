class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        ans=-1       
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=int(low+(high-low)/2)
            if nums[mid]==target:
                ans=mid   
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        l.append(ans)
        ans=-1       
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=int(low+(high-low)/2)
            if nums[mid]==target:
                ans=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        l.append(ans)
        return l