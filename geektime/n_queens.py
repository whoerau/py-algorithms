def solveNQueens(n: int) -> list:
    def dfs(Q: list, left: list, right: list):
        p = len(Q)  # 递归所在层数（行数）
        if n == p:
            result.append(Q)
            return
        for column in range(n):
            if column not in Q and p - column not in left and p + column not in right:
                dfs(Q + [column], left + [p - column], right + [p + column])

    result = []
    dfs([], [], [])
    return [["." * i + "Q" + "." * (n - i - 1) for i in li] for li in result]


if __name__ == '__main__':
    for i in solveNQueens(4):
        print(i)
