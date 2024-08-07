class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mapp={}
        l=[]
        for i in arr:
            if i in mapp:
                mapp[i]+=1
            else:
                mapp[i]=1
        for key , values in mapp.items():
            if values==1:
                l.append(key)
        if len(l)<k:
            return ""
        else:
            return l[k-1]
             
        
        
        