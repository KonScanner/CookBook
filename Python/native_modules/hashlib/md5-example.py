import hashlib
import sys


def main(text):
    textEncoded = text.encode("utf-8")

    hashedText = hashlib.md5(textEncoded)
    hexaText = hashedText.hexdigest()

    print(hexaText)
    return


if __name__ == "__main__":
    text = str(sys.argv[1])
    main(text)
