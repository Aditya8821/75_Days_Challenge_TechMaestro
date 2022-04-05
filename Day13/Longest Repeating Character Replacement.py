class Solution:
    def characterReplacement(self, arr: str, k: int) -> int:
        
        def solve(a_dictionary):
            # arr = sorted(d.values(), reverse=True)
            # return sum(arr[1:])
            all_values = a_dictionary.values()
            return max(all_values)
        
        s = 0 
        e = 0
        ans = 0 
        n = len(arr)
        d = {}
        while e<=n-1:
            d[arr[e]] = d.get(arr[e],0)+1 
            
            if len(d)==1:
                ans = max(ans,e-s+1)
                e+=1
            else:
                if (e-s+1)-solve(d)<=k:   #solve(d)<=k for upper commented function
                    ans = max(ans,e-s+1)
                    e+=1 
                else:
                    if d[arr[s]]==1:
                        del d[arr[s]]
                        s+=1
                        e+=1 
                    else:
                        d[arr[s]]-=1 
                        s+=1
                        e+=1
        return ans