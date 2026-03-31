class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = 0

        for i in range(len(s)):
            if s[i] == "A":
                countA += 1
                if countA == 2:
                    return False
            elif s[i] == "L":
                if i < len(s)-2:
                    sample = s[i:i+3]
                    if sample == "LLL":
                        return False

        return True