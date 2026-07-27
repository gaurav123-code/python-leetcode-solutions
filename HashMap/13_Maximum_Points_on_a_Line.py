"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.
"""

class Solution(object):
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        ans = 0

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

                key = (dy, dx)

                if key in slopes:
                    slopes[key] += 1
                else:
                    slopes[key] = 1

                ans = max(ans, slopes[key] + 1)

        return ans

    def gcd(self, a, b):
        a = abs(a)
        b = abs(b)

        while b:
            a, b = b, a % b

        return a
    
print(Solution().maxPoints([[1,1],[2,2],[3,3]])) 