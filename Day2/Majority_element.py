class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element,count=0,0
        for ele in nums:
            if element == ele:
                count+=1
            elif count==0:
                element,count=ele,1
            else:
                count-=1
        return element