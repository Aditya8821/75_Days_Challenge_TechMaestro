class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        visited={}
        for index,val in enumerate(nums):
            if val not in visited:
                visited[val]=index
        for i in range(1,len(nums)+1):
            if i not in visited:
                return i
        return len(nums)+1