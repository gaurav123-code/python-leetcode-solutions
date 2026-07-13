"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.
"""

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        ans = 1

        for i in range(n):
            slopes = {}

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                g = self.gcd(dx, dy)

                dx //= g
                dy //= g

                
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slope = (dy, dx)

                if slope in slopes:
                    slopes[slope] += 1
                else:
                    slopes[slope] = 1

            if slopes:
                ans = max(ans, max(slopes.values()) + 1)

        return ans
print(Solution().maxPoints([[1,1],[2,2],[3,3]]))