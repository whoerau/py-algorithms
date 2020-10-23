def remove_k_zeros(s: str, k: int) -> str:
    string0 = ''
    for i in range(k):
        string0 += "0"
    li = s.split(string0)
    return ''.join(li)


if __name__ == '__main__':
    s = "A00B0"
    print(remove_k_zeros(s, 2))
