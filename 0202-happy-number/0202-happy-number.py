class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            digits=str(n)
            square=[int(digit)**2 for digit in digits]
            return sum(square)
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n=sum_of_squares(n)
        return n==1


        