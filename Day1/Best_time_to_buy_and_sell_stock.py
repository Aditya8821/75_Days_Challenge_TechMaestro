class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minsofar=prices[0]
        for i in range(len(prices)):
            minsofar=min(minsofar,prices[i])
            maxprofit=max(maxprofit,prices[i]-minsofar)
        return maxprofit