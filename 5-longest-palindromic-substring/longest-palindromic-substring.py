class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                curr = s[i:j]
                if curr == curr[::-1] and len(curr) > len(longest):
                    longest = curr
        return longest