import hashlib
from itertools import count


def main():
    bin_str= input("Enter binary: ")

    bin_1_hash = hashlib.sha3_512(bin_str.encode()).hexdigest()

    bin_arr = list(bin_str)

    if bin_arr[0] == str(1):
        bin_arr[0] = str(0)
    else:
        bin_arr[0] = str(1)

    bin_res = ''.join(bin_arr)

    bin_2_hash = hashlib.sha3_512(bin_res.encode()).hexdigest()

    bin_1_int = int(bin_1_hash, 16)
    bin_1_bin = bin(bin_1_int)[2:].zfill(512)

    bin_2_int = int(bin_2_hash, 16)
    bin_2_bin = bin(bin_2_int)[2:].zfill(512)

    xor = "".join(str(int(x) ^ int(y)) for x, y in zip(bin_1_bin, bin_2_bin))

    ones = xor.count("1")

    print(f"Counted ones: {ones}")
    print(f"Percentage of changes: {(ones/512)*100}%")


if __name__ == '__main__':
    main()

