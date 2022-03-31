class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        previous={nums[0]}
        final_set=set()
        for n in nums[1:]:
            if n-k in previous:
                final_set.add((n-k,n))
            if n+k in previous:
                final_set.add((n,n+k))
            previous.add(n)
        return len(final_set)