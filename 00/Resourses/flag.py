def main(s):
    ret_str = list(map(ord, s))
    static_str = '0123456'
    print(ret_str)
    num = 0
    for i in range(len(s)):
        if num == 6:
            num = 0
        if (i & 1) != 0:
            j = 0
            while ord(static_str[num]) > j:
                j += 1
                ret_str[i] += 1
                if ret_str[i] == 127:
                    ret_str[i] = 32
        else:
            k = 0
            while ord(static_str[num]) > k:
                k += 1
                ret_str[i] -= 1
                if ret_str[i] == 31:
                    ret_str[i] = 126
        num += 1
    fin = ''.join(list(map(chr, ret_str)))
    print(list(fin))
    print(fin)

if __name__ == '__main__':
    s = input()
    main(s)
