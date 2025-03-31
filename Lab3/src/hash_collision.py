import hashlib
import random

def main():
    collisions_12 = 0
    collisions_20 = 0
    collisions_50 = 0
    entry = input("Enter integer: ").encode()
    entry_hash = hashlib.md5(entry).hexdigest()
    entry_12_first_bit = entry_hash[:3]
    entry_20_first_bit = entry_hash[:5]
    entry_50_first_bit = entry_hash[:13]
    range_to_for = int(input("Enter range: "))
    for i in range(range_to_for):
        random_data = str(random.getrandbits(160)).encode()
        hash_value  = hashlib.md5(random_data).hexdigest()
        random_12_first_bit = hash_value [:3]
        random_20_first_bit = hash_value [:5]
        random_50_first_bit = hash_value [:13]
        if entry_12_first_bit == random_12_first_bit:
            collisions_12 += 1
        if entry_20_first_bit == random_20_first_bit:
            collisions_20 += 1
        if entry_50_first_bit == random_50_first_bit:
            collisions_50 += 1

    print(f"Collisions found od first 12 bits: {collisions_12}")
    print(f"Collisions found od first 20 bits: {collisions_20}")
    print(f"Collisions found od first 50 bits: {collisions_50}")
if __name__ == '__main__':
    main()