class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        final = []
        intervals.sort()

        for start,end in intervals:
            if not final or final[-1][1] < start:
                final.append([start,end])
            else:
                final[-1][1] = max(final[-1][1], end)
        return final