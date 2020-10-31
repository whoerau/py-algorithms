class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        sample = dict({
            "}": "{",
            "]": "[",
            ")": "(",
        })
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in sample:
                    if stack.pop() != sample[c]:
                        return False
                    else:
                        continue
                else:
                    stack.append(c)
        return not stack


if __name__ == '__main__':
    s = "[{()}]"
    obj = Solution()
    print(obj.is_valid(s))
