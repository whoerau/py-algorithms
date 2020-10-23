def is_rotation(str1: str, str2: str) -> bool:
    return (str2 + str2).find(str1) != -1


if __name__ == '__main__':
    a = "cdab"
    b = "abcd"
    print(is_rotation(a, b))
    a = "1ab2"
    b = "ab12"
    print(is_rotation(a, b))
