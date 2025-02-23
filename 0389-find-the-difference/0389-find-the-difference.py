class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap1={}
        hashmap2={}
        for i in s:
            if i in hashmap1:
                hashmap1[i]+=1
            else:
                hashmap1[i]=1
        for i in t:
            if i in hashmap2:
                hashmap2[i]+=1
            else:
                hashmap2[i]=1
        for key in hashmap2 or hashmap[key]>1:
            if key not in hashmap1 or hashmap2[key] > hashmap1.get(key, 0):
                return key
        
        
        