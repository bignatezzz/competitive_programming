class Solution:
    def monkeyMove(self, n: int) -> int:
        finalans = 1
        ans = 2
        i = 1
        while (i < n):
            if (2*i <= n):
                i *= 2
                ans *= ans 
                ans = ans % 1000000007
            
            else:
                n -= i
                i = 1
                finalans *= ans
                ans = 2
                finalans = finalans % 1000000007

        finalans *= ans
        finalans = finalans % 1000000007
        if finalans < 2:
            return finalans + 1000000005

        return finalans-2
