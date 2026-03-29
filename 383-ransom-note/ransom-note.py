class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        freq_ransom = {}
        freq_magazine = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in freq_ransom:
                freq_ransom[ransomNote[i]] = 1
            else:
                freq_ransom[ransomNote[i]] += 1

        for i in range(len(magazine)):
            if magazine[i] not in freq_magazine:
                freq_magazine[magazine[i]] = 1
            else:
                freq_magazine[magazine[i]] += 1

        for char in freq_ransom:
            if char not in freq_magazine:
                return False
            elif freq_ransom.get(char) > freq_magazine.get(char):
                return False
        return True