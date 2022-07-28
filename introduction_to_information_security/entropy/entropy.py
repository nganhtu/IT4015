import math


def main():
    """
    Return entropy of a text.
    About entropy in information theory:
    https://cs.nyu.edu/faculty/davise/ai/entropy.pdf
    http://rosettacode.org/wiki/Entropy
    https://vi.wikipedia.org/wiki/Entropy_th%C3%B4ng_tin
    """
    text = input()
    H = 0

    charCnt = {}
    for c in text:
        if c in charCnt.keys():
            charCnt[c] += 1
        else:
            charCnt[c] = 1

    for symbol in charCnt:
        prob = charCnt[symbol] / len(text)
        H -= prob * math.log2(prob)

    print(charCnt)
    print("Intensive entropy: ", H, "bits/symbol")
    print("Extensive entropy: ", H * len(text), "bits")


if __name__ == "__main__":
    main()
