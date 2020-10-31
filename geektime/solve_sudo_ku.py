# 暴力dfs
class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.slove(board)

    def slove(self, board) -> bool:
        s = "123456789"
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    for c in s:
                        if self.check_valid(board, i, j, c):
                            board[i][j] = c
                            if self.slove(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def check_valid(self, board, i, j, c) -> bool:
        for m in range(len(board)):
            # 判定列
            if board[i][m] != '.' and board[i][m] == c:
                return False
            # 判定行
            if board[m][j] != '.' and board[m][j] == c:
                return False
        # 判定小九宫格
        # sq 为小九宫格中位于 右下 的格子位置坐标
        sq = self.get_mini_squared(i, j)
        for ti in range(sq[0] - 3, sq[0]):
            for tj in range(sq[1] - 3, sq[1]):
                if board[ti][tj] != "." and board[ti][tj] == c:
                    return False
        return True

    def get_mini_squared(self, i, j) -> (int, int):
        def fm(m) -> int:
            if m < 3:
                return 3
            elif m < 6:
                return 6
            elif m < 9:
                return 9

        return fm(i), fm(j)


### 记录已经存在的值，空间换时间 dfs
class Solution1:
    def __init__(self):
        self.numbers = set([c for c in "123456789"])
        self.row = [set() for _ in self.numbers]
        self.colunm = [set() for _ in self.numbers]
        self.minisq = [[set() for _ in range(3)] for _ in range(3)]
        self.black = []

    def solveSudoku(self, board) -> None:
        # init data
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    self.black.append((i, j))
                else:
                    self.row[i].add(c)
                    self.colunm[j].add(c)
                    self.minisq[i // 3][j // 3].add(c)
        self._solve(board)

    def _solve(self, board, index=0) -> bool:
        if index == len(self.black):
            return True
        i, j = self.black[index]
        available_numbers = self.numbers - self.row[i] - self.colunm[j] - self.minisq[i // 3][j // 3]
        if not available_numbers:
            return False
        for c in available_numbers:
            board[i][j] = c
            self.row[i].add(c)
            self.colunm[j].add(c)
            self.minisq[i // 3][j // 3].add(c)
            if self._solve(board, index + 1):
                return True
            else:
                # board[i][j] = '.'
                self.row[i].discard(c)
                self.colunm[j].discard(c)
                self.minisq[i // 3][j // 3].discard(c)
                continue
        return False


if __name__ == '__main__':
    li = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    # s = Solution()
    # s.solveSudoku(li)
    # for i in li:
    #     print(i)

    s1 = Solution1()
    s1.solveSudoku(li)
    for i in li:
        print(i)
