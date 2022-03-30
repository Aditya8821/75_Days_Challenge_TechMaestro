class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        total_sum=sum(card)
        l,r=0,len(card)-k-1
        window_sum=sum(card[0:r+1])
        s=total_sum-window_sum
        l,r=l+1,r+1
        while r<len(card):
            window_sum=window_sum-card[l-1]+card[r]
            s=max(s,total_sum-window_sum)
            l,r=l+1,r+1
        return s