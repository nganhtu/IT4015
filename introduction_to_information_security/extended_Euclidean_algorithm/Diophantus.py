# giải thuật Euclid được sử dụng để giải phương trình Diophantus: ax + by = c

def gcd(a, b):
    while a != b:
        if a > b:
            a %= b
            if a == 0:
                return b
        else:
            b %= a
            if b == 0:
                return a
    return -1


def gcdExtended(a, b):
    # giải phương trình ax + by = d với d = (a, b)
    if a == 0:
        return 0, 1
    x, y = gcdExtended(b % a, a)
    return y - (b // a) * x, x


def main():
    a, b = (int(input()) for _ in range(2))
    print(gcd(a, b))
    print(gcdExtended(a, b))


if __name__ == "__main__":
    main()
