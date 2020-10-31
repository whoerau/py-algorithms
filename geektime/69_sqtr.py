class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            m = (left + right) / 2
            if m == x / m:
                return m
            elif m > x / m:
                right = m
            elif m < x / m:
                left = m
        return m


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(5))
