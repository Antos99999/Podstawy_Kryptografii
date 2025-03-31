import hashlib

def MD5(text1, text2):
    md5_1 = hashlib.md5(text1.encode()).hexdigest()
    md5_1_int = int(md5_1,16)
    md5_1_bin = bin(md5_1_int)[2:].zfill(1281)

    md5_2 = hashlib.md5(text2.encode()).hexdigest()
    md5_2_int = int(md5_2,16)
    md5_2_bin = bin(md5_2_int)[2:].zfill(128)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(md5_1_bin, md5_2_bin))

    one_in_xor = xor.count("1")

    procent_of_one = (one_in_xor/128)*100

    return procent_of_one

def SHA1(text1, text2):
    sha1_1 = hashlib.sha1(text1.encode()).hexdigest()
    sha1_1_int = int(sha1_1, 16)
    sha1_1_bin = bin(sha1_1_int)[2:].zfill(160)

    sha1_2 = hashlib.sha1(text2.encode()).hexdigest()
    sha1_2_int = int(sha1_2, 16)
    sha1_2_bin = bin(sha1_2_int)[2:].zfill(160)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(sha1_1_bin, sha1_2_bin))

    one_in_xor = xor.count("1")

    procent_of_one = (one_in_xor / 160) * 100

    return procent_of_one

def SHA224(text1, text2):
    sha224_1 = hashlib.sha224(text1.encode()).hexdigest()
    sha224_1_int = int(sha224_1, 16)
    sha224_1_bin = bin(sha224_1_int)[2:].zfill(224)

    sha224_2 = hashlib.sha224(text2.encode()).hexdigest()
    sha224_2_int = int(sha224_2, 16)
    sha224_2_bin = bin(sha224_2_int)[2:].zfill(224)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(sha224_1_bin, sha224_2_bin))

    one_in_xor = xor.count("1")

    procent_of_one = (one_in_xor / 224) * 100

    return procent_of_one

def SHA256(text1, text2):
    sha256_1 = hashlib.sha256(text1.encode()).hexdigest()
    sha256_1_int = int(sha256_1, 16)
    sha256_1_bin = bin(sha256_1_int)[2:].zfill(256)

    sha256_2 = hashlib.sha256(text2.encode()).hexdigest()
    sha256_2_int = int(sha256_2, 16)
    sha256_2_bin = bin(sha256_2_int)[2:].zfill(256)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(sha256_1_bin, sha256_2_bin))

    one_in_xor = xor.count("1")

    procent_of_one = (one_in_xor / 256) * 100

    return procent_of_one

def SHA384(text1, text2):
    sha384_1 = hashlib.sha384(text1.encode()).hexdigest()
    sha384_1_int = int(sha384_1, 16)
    sha384_1_bin = bin(sha384_1_int)[2:].zfill(384)

    sha384_2 = hashlib.sha384(text2.encode()).hexdigest()
    sha384_2_int = int(sha384_2, 16)
    sha384_2_bin = bin(sha384_2_int)[2:].zfill(384)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(sha384_1_bin, sha384_2_bin))

    one_in_xor = xor.count("1")

    procent_of_one = (one_in_xor / 384) * 100

    return procent_of_one

def SHA512(text1, text2):
    sha512_1 = hashlib.sha512(text1.encode()).hexdigest()
    sha512_1_int = int(sha512_1, 16)
    sha512_1_bin = bin(sha512_1_int)[2:].zfill(512)

    sha512_2 = hashlib.sha512(text2.encode()).hexdigest()
    sha512_2_int = int(sha512_2, 16)
    sha512_2_bin = bin(sha512_2_int)[2:].zfill(512)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(sha512_1_bin, sha512_2_bin))

    one_in_xor = xor.count("1")

    procent_of_one = (one_in_xor / 512) * 100

    return procent_of_one

def SHA_3_224(text1, text2):
    sha3_224_1 = hashlib.sha3_224(text1.encode()).hexdigest()
    sha3_224_1_int = int(sha3_224_1, 16)
    sha3_224_1_bin = bin(sha3_224_1_int)[2:].zfill(224)

    sha3_224_2 = hashlib.sha3_224(text2.encode()).hexdigest()
    sha3_224_2_int = int(sha3_224_2, 16)
    sha3_224_2_bin = bin(sha3_224_2_int)[2:].zfill(224)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(sha3_224_1_bin, sha3_224_2_bin))

    one_in_xor = xor.count("1")

    procent_of_one = (one_in_xor / 224) * 100

    return procent_of_one

def SHA_3_256(text1, text2):
    sha3_256_1 = hashlib.sha3_256(text1.encode()).hexdigest()
    sha3_256_1_int = int(sha3_256_1, 16)
    sha3_256_1_bin = bin(sha3_256_1_int)[2:].zfill(256)

    sha3_256_2 = hashlib.sha3_256(text2.encode()).hexdigest()
    sha3_256_2_int = int(sha3_256_2, 16)
    sha3_256_2_bin = bin(sha3_256_2_int)[2:].zfill(256)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(sha3_256_1_bin, sha3_256_2_bin))

    one_in_xor = xor.count("1")

    procent_of_one = (one_in_xor / 256) * 100

    return procent_of_one

def SHA_3_384(text1, text2):
    sha3_384_1 = hashlib.sha3_384(text1.encode()).hexdigest()
    sha3_384_1_int = int(sha3_384_1, 16)
    sha3_384_1_bin = bin(sha3_384_1_int)[2:].zfill(384)

    sha3_384_2 = hashlib.sha3_384(text2.encode()).hexdigest()
    sha3_384_2_int = int(sha3_384_2, 16)
    sha3_384_2_bin = bin(sha3_384_2_int)[2:].zfill(384)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(sha3_384_1_bin, sha3_384_2_bin))

    one_in_xor = xor.count("1")

    procent_of_one = (one_in_xor / 384) * 100

    return procent_of_one

def SHA_3_512(text1, text2):
    sha3_512_1 = hashlib.sha3_512(text1.encode()).hexdigest()
    sha3_512_1_int = int(sha3_512_1, 16)
    sha3_512_1_bin = bin(sha3_512_1_int)[2:].zfill(512)

    sha3_512_2 = hashlib.sha3_512(text2.encode()).hexdigest()
    sha3_512_2_int = int(sha3_512_2, 16)
    sha3_512_2_bin = bin(sha3_512_2_int)[2:].zfill(512)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(sha3_512_1_bin, sha3_512_2_bin))

    one_in_xor = xor.count("1")

    procent_of_one = (one_in_xor / 512) * 100

    return procent_of_one



def main():
    while True:
        print("\nChoose hash Aglorithms\n")
        print("1. MD5")
        print("2. SHA-1")
        print("3. SHA-224")
        print("4. SHA-256")
        print("5. SHA-384")
        print("6. SHA-512")
        print("7. SHA-3-224")
        print("8. SHA-3-256")
        print("9. SHA-3-384")
        print("10. SHA-3-512")
        print("11. Exit\n")

        option = input("Enter your choice: ")
        if option == "11":
            break
        text1 = input("Enter text 1: ")
        text2 = input("Enter text 2: ")

        if option == "1":
            procent_of_one = MD5(text1, text2)
            print(f"\nPercentage of bits changed: {procent_of_one}%")
        elif option == "2":
            procent_of_one = SHA1(text1, text2)
            print(f"\nPercentage of bits changed: {procent_of_one}%")
        elif option == "3":
            procent_of_one = SHA224(text1, text2)
            print(f"\nPercentage of bits changed: {procent_of_one}%")
        elif option == "4":
            procent_of_one = SHA256(text1, text2)
            print(f"\nPercentage of bits changed: {procent_of_one}%")
        elif option == "5":
            procent_of_one = SHA384(text1, text2)
            print(f"\nPercentage of bits changed: {procent_of_one}%")
        elif option == "6":
            procent_of_one = SHA512(text1, text2)
            print(f"\nPercentage of bits changed: {procent_of_one}%")
        elif option == "7":
            procent_of_one = SHA_3_224(text1, text2)
            print(f"\nPercentage of bits changed: {procent_of_one}%")
        elif option == "8":
            procent_of_one = SHA_3_256(text1, text2)
            print(f"\nPercentage of bits changed: {procent_of_one}%")
        elif option == "9":
            procent_of_one = SHA_3_384(text1, text2)
            print(f"\nPercentage of bits changed: {procent_of_one}%")
        elif option == "10":
            procent_of_one = SHA_3_512(text1, text2)
            print(f"\nPercentage of bits changed: {procent_of_one}%")


if __name__ == "__main__":
    main()