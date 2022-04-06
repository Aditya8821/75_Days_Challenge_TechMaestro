class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start,end=0,len(arr)-1
        while start<end:
            mid=(start+end)//2
            if arr[mid]>arr[mid+1]: 
                #It means you are in the decreasing part of the array
                #This may be the answer but there may be any other also before that so end=mid
                end=mid
            else:
                #It means you are in the decreasing part of the array
                #This is the because we know that mid<mid+1 so it means that mid can't be the peak so,
                start=mid+1
        return start