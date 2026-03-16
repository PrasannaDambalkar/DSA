class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        x1=points[0][0]
        y1=points[0][1]
        x2=points[1][0]
        y2=points[1][1]
        x3=points[2][0]
        y3=points[2][1]

        if (y3-y1)*(x2-x1) != (y2-y1)*(x3-x1):
            return True
        return False