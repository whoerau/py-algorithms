import heapq


def k_max_number(l1: list, k: int) -> int:
    h = []
    for t in l1:
        heapq.heappush(h, t)
    return heapq.nlargest(k, h)[k - 1]


if __name__ == '__main__':
    l1 = [3, 98, 2, 6, 103, 2, 9]
    k = 3
    print(k_max_number(l1, k))
