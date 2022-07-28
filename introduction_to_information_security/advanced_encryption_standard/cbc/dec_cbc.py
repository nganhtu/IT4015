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


Sbox_inv = (
    "52", "09", "6A", "D5", "30", "36", "A5", "38", "BF", "40", "A3", "9E", "81", "F3", "D7", "FB",
    "7C", "E3", "39", "82", "9B", "2F", "FF", "87", "34", "8E", "43", "44", "C4", "DE", "E9", "CB",
    "54", "7B", "94", "32", "A6", "C2", "23", "3D", "EE", "4C", "95", "0B", "42", "FA", "C3", "4E",
    "08", "2E", "A1", "66", "28", "D9", "24", "B2", "76", "5B", "A2", "49", "6D", "8B", "D1", "25",
    "72", "F8", "F6", "64", "86", "68", "98", "16", "D4", "A4", "5C", "CC", "5D", "65", "B6", "92",
    "6C", "70", "48", "50", "FD", "ED", "B9", "DA", "5E", "15", "46", "57", "A7", "8D", "9D", "84",
    "90", "D8", "AB", "00", "8C", "BC", "D3", "0A", "F7", "E4", "58", "05", "B8", "B3", "45", "06",
    "D0", "2C", "1E", "8F", "CA", "3F", "0F", "02", "C1", "AF", "BD", "03", "01", "13", "8A", "6B",
    "3A", "91", "11", "41", "4F", "67", "DC", "EA", "97", "F2", "CF", "CE", "F0", "B4", "E6", "73",
    "96", "AC", "74", "22", "E7", "AD", "35", "85", "E2", "F9", "37", "E8", "1C", "75", "DF", "6E",
    "47", "F1", "1A", "71", "1D", "29", "C5", "89", "6F", "B7", "62", "0E", "AA", "18", "BE", "1B",
    "FC", "56", "3E", "4B", "C6", "D2", "79", "20", "9A", "DB", "C0", "FE", "78", "CD", "5A", "F4",
    "1F", "DD", "A8", "33", "88", "07", "C7", "31", "B1", "12", "10", "59", "27", "80", "EC", "5F",
    "60", "51", "7F", "A9", "19", "B5", "4A", "0D", "2D", "E5", "7A", "9F", "93", "C9", "9C", "EF",
    "A0", "E0", "3B", "4D", "AE", "2A", "F5", "B0", "C8", "EB", "BB", "3C", "83", "53", "99", "61",
    "17", "2B", "04", "7E", "BA", "77", "D6", "26", "E1", "69", "14", "63", "55", "21", "0C", "7D"
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


def AESDec(y, key):
    B = C = ""
    A = y
    k = key

    # Generate key list
    key_list = [k, ]
    k1 = k[0:32]
    k2 = k[32:64]
    k3 = k[64:96]
    k4 = k[96:128]
    for i in range(10):
        k1 = xor_str(k1, g(k4, i + 1))
        k2 = xor_str(k1, k2)
        k3 = xor_str(k2, k3)
        k4 = xor_str(k3, k4)
        k = k1 + k2 + k3 + k4
        key_list.append(k)

    # First Key Addition
    C = xor_str(A, key_list[10])

    for i in range(10):

        # Inv MixColumn
        after_SR = ""
        if i == 0:
            after_SR = C
        else:
            for j in range(0, 128, 32):

                after_SR += xor_str(xor_str(xor_str(
                    GFmul(14, C[j:j + 8]),
                    GFmul(11, C[j + 8:j + 16])),
                    GFmul(13, C[j + 16:j + 24])),
                    GFmul(9, C[j + 24:j + 32]))

                after_SR += xor_str(xor_str(xor_str(
                    GFmul(9, C[j:j + 8]),
                    GFmul(14, C[j + 8:j + 16])),
                    GFmul(11, C[j + 16:j + 24])),
                    GFmul(13, C[j + 24:j + 32]))

                after_SR += xor_str(xor_str(xor_str(
                    GFmul(13, C[j:j + 8]),
                    GFmul(9, C[j + 8:j + 16])),
                    GFmul(14, C[j + 16:j + 24])),
                    GFmul(11, C[j + 24:j + 32]))

                after_SR += xor_str(xor_str(xor_str(
                    GFmul(11, C[j:j + 8]),
                    GFmul(13, C[j + 8:j + 16])),
                    GFmul(9, C[j + 16:j + 24])),
                    GFmul(14, C[j + 24:j + 32]))

        # Inv ShiftRows
        B = ""

        B += after_SR[0:8]
        B += after_SR[104:112]
        B += after_SR[80:88]
        B += after_SR[56:64]

        B += after_SR[32:40]
        B += after_SR[8:16]
        B += after_SR[112:120]
        B += after_SR[88:96]

        B += after_SR[64:72]
        B += after_SR[40:48]
        B += after_SR[16:24]
        B += after_SR[120:128]

        B += after_SR[96:104]
        B += after_SR[72:80]
        B += after_SR[48:56]
        B += after_SR[24:32]

        # Inv Byte Substitution
        A = ""
        for j in range(0, 128, 8):
            tmp = str(bin(int(Sbox_inv[int(B[j:j + 8], base=2)], base=16)))[2:]
            while len(tmp) < 8:
                tmp = "0" + tmp
            A += tmp

        # Key Addition
        C = xor_str(key_list[9 - i], A)

    return C


def main():

    # Entering ciphertext
    read_ctbin = open(
        "introduction_to_information_security\\advanced_encryption_standard\\cbc\\ctbin.txt", "r")
    ctbin = read_ctbin.read().replace(" ", "").replace("\n", "")
    read_ctbin.close()

    # Padding
    if len(ctbin) % 128 != 0:
        ctbin += "1"
    while len(ctbin) % 128 != 0:
        ctbin += "0"
    print("ctbin is", ctbin)

    # Entering key
    read_key = open(
        "introduction_to_information_security\\advanced_encryption_standard\\cbc\\key.txt", "r")
    key = bin(int(read_key.read().replace("\n", ""), base=16))[2:]
    read_key.close()
    while len(key) < 128:
        key = "0" + key
    print("Key is", key)

    # Entering IV
    read_IV = open(
        "introduction_to_information_security\\advanced_encryption_standard\\cbc\\IV.txt", "r")
    IV = read_IV.read().replace("\n", "")
    read_IV.close()
    print("IV is", IV)

    # Encoding
    ptbin = ""
    pad = IV
    for i in range(0, len(ctbin), 128):
        ctblock = ctbin[i:i + 128]
        ptblock = xor_str(AESDec(ctblock, key), pad)
        pad = ctblock
        ptbin += ptblock
    print("Ptbin is", ptbin)


if __name__ == '__main__':
    main()
