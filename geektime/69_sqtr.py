class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 0, x
        rsp = -1
        while left <= right:
            m = (left + right) // 2
            if m * m == x:
                rsp = m
                break
            elif m * m > x:
                right = m - 1
            elif m * m < x:
                rsp = m
                left = m + 1
        return rsp


if __name__ == '__main__':
    s = Solution()
    m = s.mySqrt(8)
    print(type(m), m)
