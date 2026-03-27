class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s

        final = [""]*numRows
        curr = 0
        going = False

        for char in s:
            final[curr] += char

            if curr == 0 or curr == numRows-1:
                going = not going

            curr += 1 if going else -1
        return "".join(final)