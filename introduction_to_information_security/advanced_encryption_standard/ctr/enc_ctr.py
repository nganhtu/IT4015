import random


Sbox = (
    "63", "7C", "77", "7B", "F2", "6B", "6F", "C5", "30", "01", "67", "2B", "FE", "D7", "AB", "76",
    "CA", "82", "C9", "7D", "FA", "59", "47", "F0", "AD", "D4", "A2", "AF", "9C", "A4", "72", "C0",
    "B7", "FD", "93", "26", "36", "3F", "F7", "CC", "34", "A5", "E5", "F1", "71", "D8", "31", "15",
    "04", "C7", "23", "C3", "18", "96", "05", "9A", "07", "12", "80", "E2", "EB", "27", "B2", "75",
    "09", "83", "2C", "1A", "1B", "6E", "5A", "A0", "52", "3B", "D6", "B3", "29", "E3", "2F", "84",
    "53", "D1", "00", "ED", "20", "FC", "B1", "5B", "6A", "CB", "BE", "39", "4A", "4C", "58", "CF",
    "D0", "EF", "AA", "FB", "43", "4D", "33", "85", "45", "F9", "02", "7F", "50", "3C", "9F", "A8",
    "51", "A3", "40", "8F", "92", "9D", "38", "F5", "BC", "B6", "DA", "21", "10", "FF", "F3", "D2",
    "CD", "0C", "13", "EC", "5F", "97", "44", "17", "C4", "A7", "7E", "3D", "64", "5D", "19", "73",
    "60", "81", "4F", "DC", "22", "2A", "90", "88", "46", "EE", "B8", "14", "DE", "5E", "0B", "DB",
    "E0", "32", "3A", "0A", "49", "06", "24", "5C", "C2", "D3", "AC", "62", "91", "95", "E4", "79",
    "E7", "C8", "37", "6D", "8D", "D5", "4E", "A9", "6C", "56", "F4", "EA", "65", "7A", "AE", "08",
    "BA", "78", "25", "2E", "1C", "A6", "B4", "C6", "E8", "DD", "74", "1F", "4B", "BD", "8B", "8A",
    "70", "3E", "B5", "66", "48", "03", "F6", "0E", "61", "35", "57", "B9", "86", "C1", "1D", "9E",
    "E1", "F8", "98", "11", "69", "D9", "8E", "94", "9B", "1E", "87", "E9", "CE", "55", "28", "DF",
    "8C", "A1", "89", "0D", "BF", "E6", "42", "68", "41", "99", "2D", "0F", "B0", "54", "BB", "16"
)


def xor_str(a, b):
    """xor 2 strings of binary digits with same length."""
    res = ""
    for i in range(len(a)):
        if (a[i] == b[i]):
            res += "0"
        else:
            res += "1"
    return res


def and_str(a, b):
    """and 2 strings of binary digits with same length."""
    res = ""
    for i in range(len(a)):
        if (a[i] == b[i] == "1"):
            res += "1"
        else:
            res += "0"
    return res


def GFmul(i, s):
    """
    Multiply an integer with a string in Galois field.

    Keyword arguments:

    i -- the integer in decimal base, in list [1, 2, 3, 9, 11, 13, 14]

    s -- the 8-bit length string
    """
    if i == 1:
        return s
    if i == 2:
        str = s[1:] + "0"
        return str
    if i == 4:
        str = s[2:] + "00"
        return str
    if i == 8:
        str = s[3:] + "000"
        return str

    if i == 3:
        return xor_str(GFmul(2, s), s)
    if i == 9:
        return xor_str(GFmul(8, s), s)
    if i == 11:
        return xor_str(xor_str(GFmul(8, s), GFmul(2, s)), s)
    if i == 13:
        return xor_str(xor_str(GFmul(8, s), GFmul(4, s)), s)
    if i == 14:
        return xor_str(xor_str(GFmul(8, s), GFmul(4, s)), GFmul(2, s))

    return "unknown"


def RC(i):
    switcher = {
        1: "00000001", 2: "00000010", 3: "00000100", 4: "00001000",
        5: "00010000", 6: "00100000", 7: "01000000", 8: "10000000",
        9: "00011011", 10: "00110110"
    }
    return switcher.get(i, "unknown")


def g(string, roundofRC):
    V = string
    V = V[8:32] + V[0:8]
    key = ""
    for i in range(0, 32, 8):
        tmp = str(bin(int(Sbox[int(V[i:i + 8], base=2)], base=16)))[2:]
        while len(tmp) < 8:
            tmp = "0" + tmp
        key += tmp
    key = xor_str(V[0:8], RC(roundofRC)) + key[8:32]
    return key


def AESEnc(x, key):
    A = B = ""
    C = x
    k = key

    # k = 128 bit => 10 rounds
    RC = ("00000001", "00000010", "00000100", "00001000",
          "00010000", "00100000", "01000000", "10000000",
          "00011011", "00110110")

    # First Key Addition Layer, W[0..3] = k
    A = xor_str(C, k)

    for i in range(10):

        # Byte Substitution
        B = ""
        for j in range(0, 128, 8):
            tmp = str(bin(int(Sbox[int(A[j:j + 8], base=2)], base=16)))[2:]
            while len(tmp) < 8:
                tmp = "0" + tmp
            B += tmp

        # ShiftRows
        after_SR = ""

        after_SR += B[0:8]
        after_SR += B[40:48]
        after_SR += B[80:88]
        after_SR += B[120:128]

        after_SR += B[32:40]
        after_SR += B[72:80]
        after_SR += B[112:120]
        after_SR += B[24:32]

        after_SR += B[64:72]
        after_SR += B[104:112]
        after_SR += B[16:24]
        after_SR += B[56:64]

        after_SR += B[96:104]
        after_SR += B[8:16]
        after_SR += B[48:56]
        after_SR += B[88:96]

        # MixColumn
        if i == 9:
            C = after_SR
        else:
            C = ""
            for j in range(0, 128, 32):

                C += xor_str(xor_str(xor_str(
                    GFmul(2, after_SR[j:j + 8]),
                    GFmul(3, after_SR[j + 8:j + 16])),
                    after_SR[j + 16:j + 24]),
                    after_SR[j + 24:j + 32])

                C += xor_str(xor_str(xor_str(
                    after_SR[j:j + 8],
                    GFmul(2, after_SR[j + 8:j + 16])),
                    GFmul(3, after_SR[j + 16:j + 24])),
                    after_SR[j + 24:j + 32])

                C += xor_str(xor_str(xor_str(
                    after_SR[j:j + 8],
                    after_SR[j + 8:j + 16]),
                    GFmul(2, after_SR[j + 16:j + 24])),
                    GFmul(3, after_SR[j + 24:j + 32]))

                C += xor_str(xor_str(xor_str(
                    GFmul(3, after_SR[j:j + 8]),
                    after_SR[j + 8:j + 16]),
                    after_SR[j + 16:j + 24]),
                    GFmul(2, after_SR[j + 24:j + 32]))

        # Key Addition
        k1 = k[0:32]
        k2 = k[32:64]
        k3 = k[64:96]
        k4 = k[96:128]

        k1 = xor_str(k1, g(k4, i + 1))
        k2 = xor_str(k1, k2)
        k3 = xor_str(k2, k3)
        k4 = xor_str(k3, k4)

        k = k1 + k2 + k3 + k4
        A = xor_str(k, C)

    return A


def main():

    # Entering plaintext
    read_ptbin = open(
        "introduction_to_information_security\\advanced_encryption_standard\\ctr\\ptbin.txt", "r")
    ptbin = read_ptbin.read().replace(" ", "").replace("\n", "")
    read_ptbin.close()

    # Padding
    if len(ptbin) % 128 != 0:
        ptbin += "1"
    while len(ptbin) % 128 != 0:
        ptbin += "0"
    print("Ptbin is", ptbin)

    # Entering key
    read_key = open(
        "introduction_to_information_security\\advanced_encryption_standard\\ctr\\key.txt", "r")
    key = bin(int(read_key.read().replace("\n", ""), base=16))[2:]
    read_key.close()
    while len(key) < 128:
        key = "0" + key
    print("Key is", key)

    # Initialization value
    nonce = ""
    for _ in range(64):
        nonce += f'{round(random.random())}'
    print("Nonce is", nonce)

    # Encoding
    ctbin = ""
    ctr = 0
    for i in range(0, len(ptbin), 128):
        ptblock = ptbin[i:i + 128]
        ctr_str = str(bin(ctr))[2:]
        while len(ctr_str) < 64:
            ctr_str = "0" + ctr_str
        ctblock = xor_str(AESEnc(nonce + ctr_str, key), ptblock)
        ctbin += ctblock
        ctr += 1
    print("Ctbin is", ctbin)


if __name__ == '__main__':
    main()
