# x = 15 * (y - 22) mod 26

# có thể viết hàm encode tại đây

def decode(c):
    return chr(15 * (ord(c) - ord("a") - 22) % 26 + ord("a"))


def main():
    cipher = "falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj"
    plain = ""
    for c in cipher:
        plain += decode(c)
    print(plain)


if __name__ == "__main__":
    main()
