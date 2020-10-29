# 自底向上，状态压缩
def minimumTotal(triangle: list) -> int:
    rsp = triangle[-1]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            rsp[j] = min(rsp[j], rsp[j + 1]) + triangle[i][j]
    return rsp[0]


if __name__ == '__main__':
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(minimumTotal(triangle))
