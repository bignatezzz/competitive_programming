class Solution:
    def isHappy(self, n: int) -> bool:
        Set = set()
        while True:
            sum = 0
            while n > 0:
                sum = sum + (n%10)*(n%10)

                n = n//10
            if sum == 1:
                    return True
            if sum in Set:
                    return False
            
            Set.add(sum)

            n = sum
