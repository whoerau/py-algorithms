# dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + li[i][j]

def min_path_sum1(li: list) -> int:
    dp = [[0 for _ in li[0]] for _ in li]
    dp[0][0] = li[0][0]
    for i in range(1, len(li)):
        dp[i][0] = dp[i - 1][0] + li[i][0]
    for j in range(1, len(li[0])):
        dp[0][j] = dp[0][j - 1] + li[0][j]

    for i in range(1, len(li)):
        for j in range(1, len(li[0])):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + li[i][j]

    return dp[len(li) - 1][len(li[0]) - 1]


if __name__ == '__main__':
    li = [[1, 3, 5, 9],
          [8, 1, 3, 4],
          [5, 0, 6, 1],
          [8, 8, 4, 0]]
    print(min_path_sum1(li))
