class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {")" : "(", "]" : "[", "}" : "{"}
        seen = []
        
        for char in s:
            
            if char in "([{":
                seen.append(char)
            else:
                if not seen or seen[-1] != pair[char]:
                    return False
                
                seen.pop()

        return len(seen) == 0