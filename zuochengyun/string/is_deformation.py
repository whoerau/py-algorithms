def is_deformation(str1: str, str2: str) -> bool:
    dict1 = dict()
    dict2 = dict()
    for c in str1:
        if c not in dict1:
            dict1[c] = 1
        else:
            dict1[c] += 1
    for c in str2:
        if c not in dict2:
            dict2[c] = 1
        else:
            dict2[c] += 1
    return dict1 == dict2


if __name__ == '__main__':
    str1 = '123'
    str2 = '231'
    print(is_deformation(str1, str2))
    str2 = '2331'
    print(is_deformation(str1, str2))
