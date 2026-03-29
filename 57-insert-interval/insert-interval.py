class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        final = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                final.append(interval)
            elif interval[0] > newInterval[1]:
                final.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        
        final.append(newInterval)

        return final