class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            leftVal = nums[left]
            midVal = nums[mid]
            if midVal == target:
                return mid
        
            if (leftVal < midVal and leftVal <= target < midVal):
                # leftVal and midVal are within one section
                # target is in the current section
                right = mid - 1
            elif (leftVal > midVal and (target < midVal or target >= leftVal)):
                # leftVal and midVal span both sections, but
                # target is between them
                right = mid - 1    
            else:
                # target is not in the current range
                left = mid + 1
        return -1