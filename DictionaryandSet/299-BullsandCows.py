class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = {}
        for i in secret:
            if i in dic:
                dic[i] = dic[i] +1

            else:
                dic[i] = 1

        cows = 0
        bulls = 0 
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                cows += 1

        for j in guess:
            if j in dic and dic[j] > 0:
                bulls += 1
                dic[j] = dic[j] - 1

        bulls -= cows
        return f"{cows}A{bulls}B"
