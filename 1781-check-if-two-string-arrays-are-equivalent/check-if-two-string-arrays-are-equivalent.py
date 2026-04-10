class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        first = ""
        second = ""

        for i in range(len(word1)):
            first += word1[i]
        
        for i in range(len(word2)):
            second += word2[i]

        if first == second:
            return True
        else:
            return False