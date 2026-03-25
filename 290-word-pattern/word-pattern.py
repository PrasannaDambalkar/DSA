class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        freq = {}
        final = []
        word = ""
        for i in range(len(s)):
            if s[i] != " ":
                word += s[i]
            else:
                final.append(word)
                word = ""
        final.append(word)
        if len(pattern) != len(final):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in freq:
                freq[pattern[i]] = final[i]
            else:
                if freq[pattern[i]] != final[i]:
                    return False
        duplicate = list(freq.values())
        if len(duplicate) != len(list(set(duplicate))):
            return False
        return True
