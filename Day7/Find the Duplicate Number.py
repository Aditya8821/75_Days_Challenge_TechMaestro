class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited=[False]*len(nums)
        for num in nums:
            if visited[num]:
                return num
            else:
                visited[num]=True