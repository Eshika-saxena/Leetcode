class Solution:
    def isPalindrome(self, s: str) -> bool: 
        newstr = ''.join(c.lower() for c in s if c.isalnum())
        n=len(newstr)
        i=0
        j=n-1
        while i<j:
            if newstr[i]!=newstr[j]:
                return False
            i+=1
            j-=1
        return True