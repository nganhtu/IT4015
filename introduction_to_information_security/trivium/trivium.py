import random
import binascii


def xor(a, b):  # xor 2 strings of binary with same length
    res = ""
    for i in range(len(a)):
        if (a[i] == b[i]):
            res += "0"
        else:
            res += "1"
    return res


def and_bit(a, b):  # and 2 strings of binary with same length
    res = ""
    for i in range(len(a)):
        if (a[i] == b[i] == "1"):
            res += "1"
        else:
            res += "0"
    return res


def main():

    # Generate registers

    IV = ""
    for _ in range(80):
        IV += f'{round(random.random())}'
    A = IV + "0000000000000"

    key = open("introduction_to_information_security\\trivium\\key.txt", "r")
    B = bin(int(key.read()[0:-1], base=16))[2:]  # key.txt ends with a "\n"
    while len(B) < 80:
        B = "0" + B
    B += "0000"
    key.close()

    C = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111"

    # Convert plaintext to binary

    pt = open("introduction_to_information_security\\trivium\\plaintext.txt", "r")
    plaintext = pt.read()[0:-1]  # plaintext.txt ends with a "\t"
    pt_bin = ''.join(format(ord(c), '08b') for c in plaintext)

    # Generate keystream

    keystream = ""
    for _ in range(1152 + len(pt_bin)):
        k1 = xor(and_bit(A[90],  A[91]),  xor(A[65], A[92]))
        k2 = xor(and_bit(B[81],  B[82]),  xor(B[68], B[83]))
        k3 = xor(and_bit(C[108], C[109]), xor(C[65], C[110]))
        keystream += xor(xor(k1, k2), k3)
        a1 = xor(A[68], k3)
        a2 = xor(B[77], k1)
        a3 = xor(C[86], k2)
        A = a1 + A[:-1]
        B = a2 + B[:-1]
        C = a3 + C[:-1]
    keystream = keystream[1152:]

    # Encoding

    ct_bin = xor(pt_bin, keystream)
    ciphertext = binascii.unhexlify('%x' % int("0b" + ct_bin, 2))
    print("IV = ", IV)
    print("ciphertext = ", ciphertext)  # some characters are unprintable


if __name__ == "__main__":
    main()
