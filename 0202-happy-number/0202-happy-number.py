class Solution:
    def isHappy(self, n: int) -> bool:
        while n>9:
            res = 0
            while n>0:
                rem = n%10
                res = res + rem**2
                n//=10
            n = res
        if n==1 or n==7:
            return True
        else:
            return False