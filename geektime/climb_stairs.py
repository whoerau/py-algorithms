def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    mem = [1, 2]
    for i in range(2, n):
        mem.append(mem[i - 1] + mem[i - 2])
    return mem[n - 1]


def climb_stairs_1(n: int) -> int:
    x, y = 1, 1
    for _ in range(1, n):
        x, y = y, x + y
    return y


if __name__ == '__main__':
    print(climb_stairs(9))
    print(climb_stairs_1(9))
