def convert(string: str) -> int:
    result = 0
    bool_negative = False
    if string.startswith("-"):
        bool_negative = True
        string = string[1:]
    length = len(string)
    for c in string:
        if ord(c) >= ord("9") or ord(c) <= ord("0"):
            return 0
        result += int(c) * (10 ** (length - 1))
        length -= 1
    if (not bool_negative and result > 2 ** 31 - 1) or (bool_negative and result > 2 ** 31):
        return 0
    else:
        return -result if bool_negative else result


if __name__ == '__main__':
    s = str(2 ** 31 - 1)
    print(convert(s))
    s = "12345676543212345"
    print(convert(s))
    s = "-" + str(2 ** 31)
    print(convert(s))
