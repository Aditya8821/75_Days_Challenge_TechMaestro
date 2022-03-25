class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n-1,-1,-1):    #this loop is run till -1 to access the 0th index also 
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        digits.insert(0,1)
        return digits