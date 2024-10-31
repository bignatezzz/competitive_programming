class Solution:
    def losingPlayer(self, x: int, y: int) -> str:

        n =min(x, y//4)

        if n%2 == 1:
            return "Alice"

        return "Bob"
        
