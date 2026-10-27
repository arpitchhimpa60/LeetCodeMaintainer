# Runtime: 88 ms
# Memory: 53.6 MB

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[0])
        ans = 1
        start = points[0][0]
        end = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > end:
                ans+=1
                start = points[i][0]
                end = points[i][1]
            else:
                # start = points[i][0]
                end = min(end, points[i][1])
        return ans