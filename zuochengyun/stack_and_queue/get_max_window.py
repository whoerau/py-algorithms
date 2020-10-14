def get_max_window_heapq(arr: list, w: int) -> list:
    import heapq
    rsp, tmp = [], []
    for i, v in enumerate(arr):
        heapq.heappush(tmp, (-v, i))
        if i + 1 >= w:
            # 只需判断堆顶在不在窗口即可，不在则弹出堆
            if tmp and tmp[0][1] < i - w + 1:
                heapq.heappop(tmp)
            rsp.append(-tmp[0][0])
    return rsp


def get_max_window_deque(arr: list, w: int) -> list:
    from collections import deque
    rsp = []
    tmp = deque()
    for i, v in enumerate(arr):
        # 窗口滑动，leftpop
        if i >= w and tmp[0] < i - w + 1:
            tmp.popleft()
        # 如果 新值 > right, rightpop旧值
        while tmp and v >= arr[tmp[-1]]:
            tmp.pop()
        tmp.append(i)
        if i + 1 >= w:
            rsp.append(arr[tmp[0]])
    return rsp


if __name__ == '__main__':
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    print("heapq", get_max_window_heapq(arr, 3))
    print("deque", get_max_window_deque(arr, 3))
